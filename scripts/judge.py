#!/usr/bin/env python3
"""LLM-as-Judge: score a research-harness report against the benchmark rubric.

Reads the rubric, the benchmark's claims.yaml, and a report file, then calls an
OpenAI-compatible chat-completions endpoint and returns a structured scorecard
JSON that scripts/score.py can consume directly (via the "scores" key).

Backend is configured via environment variables (OpenAI-compatible):

    JUDGE_BASE_URL   e.g. https://api.deepseek.com/v1  or  https://open.bigmodel.cn/api/paas/v4
    JUDGE_API_KEY    API key for the judge backend
    JUDGE_MODEL      e.g. deepseek-chat / glm-4-plus / gpt-4o

Usage:
    python scripts/judge.py --benchmark benchmarks/tyson2004 \
        --report benchmarks/tyson2004/reports/dsh-reproduction-report.md \
        --out scorecard.json

    python scripts/judge.py --benchmark benchmarks/tyson2004 \
        --report ... --dry-run          # print the prompt, no API call

    python scripts/judge.py ... --repeat 3 --out scorecard.json
        # run N independent judgings; writes per-run card + median aggregate

Then: python scripts/score.py scorecard.json   (uses aggregate median scores)

Judge-independence note: do NOT judge a report with a model from the same
family as the harness's LLM under test (e.g. don't use GLM to judge a
GLM-run report). Record the judge model in the output for traceability.
"""

import argparse
import json
import os
import statistics
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

DIMENSIONS = ("D1", "D2", "D3", "D4", "D5")
EVIDENCE_LEVELS = ("E0", "E1", "E2", "E3", "E4")
REPRO_LEVELS = ("R0", "R1", "R2", "R3", "R4")

DEFAULT_PROMPT = os.path.join(os.path.dirname(__file__), "judge_prompt.md")
DEFAULT_RUBRIC = os.path.join(os.path.dirname(__file__), "..", "docs", "rubric.md")


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def build_prompt(template, rubric, claims, report, extra_evidence):
    extra = ""
    if extra_evidence:
        extra = "## 附加证据清单（提交者提供的 artifact/log 目录摘录）\n\n```\n%s\n```" % extra_evidence
    return (template
            .replace("{rubric}", rubric)
            .replace("{claims}", claims)
            .replace("{report}", report)
            .replace("{extra_evidence}", extra))


def extract_json(text):
    """Extract the first JSON object from the model's reply (tolerates fences)."""
    t = text.strip()
    if t.startswith("```"):
        lines = t.splitlines()
        # drop first and last fence lines
        lines = [l for l in lines if not l.strip().startswith("```")]
        t = "\n".join(lines).strip()
    start = t.find("{")
    end = t.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("no JSON object found in judge reply")
    return json.loads(t[start:end + 1])


def validate_card(card):
    """Validate structure; return list of problems (empty = ok)."""
    problems = []
    scores = card.get("scores")
    if not isinstance(scores, dict):
        return ["missing 'scores' object"]
    for d in DIMENSIONS:
        v = scores.get(d)
        if v is None:
            problems.append(f"missing score {d}")
        else:
            try:
                f = float(v)
                if not (0 <= f <= 10):
                    problems.append(f"score {d} out of range: {v}")
            except (TypeError, ValueError):
                problems.append(f"score {d} not numeric: {v}")
    ev = card.get("evidence", {})
    if ev.get("evidence_level") and ev["evidence_level"] not in EVIDENCE_LEVELS:
        problems.append(f"bad evidence_level: {ev['evidence_level']}")
    if ev.get("reproducibility_level") and ev["reproducibility_level"] not in REPRO_LEVELS:
        problems.append(f"bad reproducibility_level: {ev['reproducibility_level']}")
    return problems


def normalize_card(card):
    card["scores"] = {d: round(float(card["scores"][d]), 1) for d in DIMENSIONS}
    return card


def call_judge(prompt, base_url, api_key, model, temperature=0.2, max_tokens=4000):
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": "你是严格的科研审稿人，只输出 JSON。"},
            {"role": "user", "content": prompt},
        ],
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"judge API HTTP {e.code}: {detail}") from e
    return body["choices"][0]["message"]["content"]


def judge_once(prompt, base_url, api_key, model, retries=1):
    last_err = None
    for attempt in range(retries + 1):
        reply = call_judge(prompt, base_url, api_key, model)
        try:
            card = extract_json(reply)
        except (ValueError, json.JSONDecodeError) as e:
            last_err = f"unparseable reply (attempt {attempt + 1}): {e}"
            continue
        problems = validate_card(card)
        if not problems:
            return normalize_card(card), reply
        last_err = f"invalid card (attempt {attempt + 1}): {'; '.join(problems)}"
    raise RuntimeError(f"judge failed after {retries + 1} attempts — {last_err}")


def aggregate(cards):
    """Median across repeat runs; keeps score.py-compatible 'scores' key."""
    agg_scores = {d: round(statistics.median(c["scores"][d] for c in cards), 1) for d in DIMENSIONS}
    spread = {d: round(max(c["scores"][d] for c in cards) - min(c["scores"][d] for c in cards), 1)
              for d in DIMENSIONS}
    return {
        "scores": agg_scores,
        "aggregate": {
            "method": "median",
            "runs": len(cards),
            "score_spread_per_dimension": spread,
            "note": "spread > 1.5 的维度建议人工复核（评委分歧大）",
        },
        "runs": cards,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--benchmark", required=True, help="benchmark dir containing claims.yaml")
    p.add_argument("--report", required=True, help="report markdown file to judge")
    p.add_argument("--rubric", default=DEFAULT_RUBRIC)
    p.add_argument("--prompt-template", default=DEFAULT_PROMPT)
    p.add_argument("--evidence-file", help="optional artifact/log listing to append as extra evidence")
    p.add_argument("--system-name", default="", help="harness/system name recorded in the card")
    p.add_argument("--repeat", type=int, default=1, help="independent judging runs (aggregate by median)")
    p.add_argument("--out", help="output JSON path (default: stdout)")
    p.add_argument("--dry-run", action="store_true", help="print prompt, no API call")
    args = p.parse_args()

    claims_path = os.path.join(args.benchmark, "claims.yaml")
    template = read_text(args.prompt_template)
    rubric = read_text(args.rubric)
    claims = read_text(claims_path) if os.path.exists(claims_path) else "(no claims.yaml found)"
    report = read_text(args.report)
    extra = read_text(args.evidence_file) if args.evidence_file else ""

    prompt = build_prompt(template, rubric, claims, report, extra)

    if args.dry_run:
        sys.stdout.write(prompt)
        return

    base_url = os.environ.get("JUDGE_BASE_URL", "").strip()
    api_key = os.environ.get("JUDGE_API_KEY", "").strip()
    model = os.environ.get("JUDGE_MODEL", "").strip()
    if not (base_url and api_key and model):
        sys.exit("Set JUDGE_BASE_URL, JUDGE_API_KEY, JUDGE_MODEL (or use --dry-run).")

    cards = []
    for i in range(args.repeat):
        card, _raw = judge_once(prompt, base_url, api_key, model)
        cards.append(card)
        print(f"[judge] run {i + 1}/{args.repeat} ok: {card['scores']}", file=sys.stderr)

    result = aggregate(cards) if len(cards) > 1 else cards[0]
    result["meta"] = {
        "judge_model": model,
        "judge_base_url": base_url,
        "benchmark": args.benchmark,
        "report": args.report,
        "system_name": args.system_name,
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "prompt_template": args.prompt_template,
        "rubric": args.rubric,
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
        total = sum(result["scores"][d] * w for d, w in
                    {"D1": .15, "D2": .30, "D3": .25, "D4": .20, "D5": .10}.items())
        print(f"[judge] wrote {args.out} — weighted total = {total:.2f}", file=sys.stderr)
    else:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
