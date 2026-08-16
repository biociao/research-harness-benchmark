# Research Harness Benchmark

> 🌐 Language / 语言：English ｜ [**中文**](README.md)

An open evaluation framework for the research capabilities of **Agent / LLM / Skill / Harness** systems.

The goal is not to judge "who chats smarter", but to evaluate whether a system can complete real research tasks:

> Literature understanding → Data acquisition → Experiment design → Code execution → Result verification → Scientific argumentation → Reproducible delivery

This repository provides:
- Five-dimension research capability evaluation framework
- Research credibility-weighted scoring
- Standard benchmark case template
- Tyson et al. (2004) reproduction case
- Leaderboard data format for Agent / LLM / Skill
- Peer-review-style scoring template
- Extensible automated scoring scripts

## Five-Dimension Evaluation Framework

| Dimension | Meaning | Research credibility weight |
|---|---:|---:|
| D1 | Literature search & acquisition | 15% |
| D2 | Content understanding & logical reasoning | 30% |
| D3 | Code generation & reproduction standards | 25% |
| D4 | Experiment design & result visualization | 20% |
| D5 | Research process & efficiency | 10% |

### Weighted Research Score

`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`

Scoring scale: Round 01 (initial) used 0–10; from Round 02 onward the scale is unified to 0–100 (weights unchanged, scoring convention fixed).

## Evaluation Rounds

### Round 02 (Latest) — Two-Project Combined Evaluation

> **Scoring convention (fixed)**: five-dimension weighted score `Total = Literature×15% + Understanding×30% + Reproduction×25% + Experiments/Visualization×20% + Process×10%` (0–100 scale).
> **Combined total = average of the project scores across completed projects 01 and 02**; an unfinished project is provisionally counted at the completed project's score (see D's 02) and updated after actual measurement — the ranking is provisional.

This round covers two classic paper reproduction projects:

| Project | Paper | Core research task |
|---|---|---|
| **01** | [Tyson et al. 2004, *Nature*](benchmarks/tyson2004/) | AMD environmental metagenomics: microbial genome reconstruction, binning, metabolism & population variation |
| **02** | [Auton et al. 2015, *Nature*](benchmarks/humangenomics/) | Independent reproduction of 1000 Genomes Phase 3 population genetics claims (VCF computation / PCA / Fst) |

#### Official Combined Leaderboard (R02)

| Rank | Harness | LLM | Total /100 | Project scores | Highlights |
|---|---:|---|---|---|---|
| 🥇 **1** | **dsh-science** | **GLM-5.3** | **93.3†** | 01 **93.3** / 02 **93.3†** | **Provisionally #1**; outstanding 01, 02 not yet available — counted at 01's score |
| 🥈 **2** | **dsh-science** | **GLM-5.2** | **91.8** | 01 **91.0** / 02 **92.5** | Most complete research reproduction engineering; claim-level verification, cross-tooling, environment pinning, mature artifact/provenance |
| 🥉 **3** | **dsh-science** | **DeepSeek-V1-Flash** | **90.8** | 01 **90.6** / 02 **91.0** | Strong overall research capability; stable across both domains, especially good disclosure of methodological differences |
| 4 | **Claude Science** | **DeepSeek-V1-Flash** | **85.8** | 01 **84.4** / 02 **87.1** | Decent research analysis, but harness engineering one tier weaker |

**†** D's 02 (Auton 2015) result is not yet available; it is provisionally counted at the 01 score (93.3). The combined total of 93.3 is a **provisional value** and will be updated once 02 is actually measured — the ranking may change.

#### Total Score Ladder Chart

```text
Research Harness Leaderboard (R02 · Combined Total /100)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

D  DSH × GLM-5.3
█████████████████████████████████████████████  93.3†
        ↑ Provisional combined Rank #1 (02 pending, counted at 01)

C  DSH × GLM-5.2
████████████████████████████████████████████  91.8
        ↑ Combined Rank #2

A  DSH × DeepSeek-V1-Flash
███████████████████████████████████████████  90.8
        ↑ Combined Rank #3

B  Claude Science × DeepSeek-V1-Flash
█████████████████████████████████████████  85.8
        ↑ Combined Rank #4

       80      85      90      95      100
```

#### Per-Project Scores

**01｜Tyson 2004**

| Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---:|---:|---:|---:|---:|---:|
| C · DSH | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| A · DSH | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| B · Claude Science | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| D · DSH | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |

**02｜Auton 2015 (1000 Genomes Phase 3)**

| Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---:|---:|---:|---:|---:|---:|
| C · DSH | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| A · DSH | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| B · Claude Science | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| D · DSH | GLM-5.3 | — | — | — | — | — | **93.3†** |

**†** D's 02 result is not yet available; provisionally counted at the 01 score (93.3), to be updated after actual measurement.

#### Key Conclusions of This Round

- **Harness Effect ≈ +5 points**: A and B use the same LLM (DeepSeek-V1-Flash); DSH (90.8) beats Claude Science (85.8) by **5.0 points** — this benchmark measures harness structure differences, not just LLM differences.
- **Swapping to a stronger model on the same harness gains only 1.0 point**: A → C (DeepSeek-V1-Flash → GLM-5.2 on DSH), 90.8 → 91.8. In long research tasks, the harness may matter more than simply switching models.
- **GLM-5.3 provisionally #1 (pending 02)**: D01 = 93.3 is outstanding; 02 (Auton 2015) is not yet available and is counted at the 01 score, giving a provisional combined total of **93.3**. This is a provisional ranking — until 02 is actually measured, "GLM-5.3 is definitely #1" cannot be treated as settled.

#### Detail Report Entry Points

| Content | Link |
|---|---|
| Full peer-review evaluation (scoring rationale, claim-level evidence, methodological disclosures, leaderboard) | [benchmarks/Review/260816 bench.txt](benchmarks/Review/260816%20bench.txt) |
| Round 02 evaluation record (structured) | [evaluations/round-02-two-project-combined.md](evaluations/round-02-two-project-combined.md) |
| Full leaderboard & changelog | [docs/leaderboard.md](docs/leaderboard.md) |
| Case details: Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case details: 1000 Genomes Phase 3 (Auton 2015) | [benchmarks/humangenomics/](benchmarks/humangenomics/) |

> **Join the evaluation**: You are welcome to reproduce the tasks above with your own LLM (Claude, GPT, etc.) × Harness tool and submit your report to this repository, so we can benchmark it together for a more comprehensive reference.

### Round 01 (Initial Baseline) — Tyson2004-v1

> Historical round; for the latest results see Round 02 above.

Task: independently reproduce the computational reconstruction of the environmental microbiome/genome work in Tyson et al. 2004.

| Rank | System | Harness | LLM | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | Report |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 🥇 1 | DSH Research Agent | DSH (DeepSeek Harness) | TBD | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | [Report](benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | TBD | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | [Report](benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

> Weighted formula: `Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5` (computed by `scripts/score.py`; Claude Science exact value 7.99, shown as 8.00; R01 used the 0–10 scale).
>
> This is the case baseline from repository initialization and does not represent a permanent ranking. All new systems should be re-evaluated on the same case, the same rubric, and the same evidence requirements, with reproduction reports submitted to `benchmarks/<case>/reports/`.
>
> Full leaderboard (with changelog) at [docs/leaderboard.md](docs/leaderboard.md); per-round evaluation notes at [evaluations/](evaluations/).

## Core Principles

1. **Claim-first**: define the scientific claims to verify before evaluating the agent.
2. **Evidence-first**: scores must be tied to evidence, not just the final report.
3. **Execution matters**: whether the code actually ran and whether results come from execution are core metrics.
4. **Reproducibility is graded**: reproduction is not binary but a continuous grade.
5. **Failure is evidence**: clearly identifying non-reproducible parts does not cost "scientific integrity" points; concealing failure should.
6. **Independent verification**: high scores should support third-party clean-environment reruns.
7. **Versioned benchmark**: benchmarks, data, scoring rules, and leaderboards are versioned.

## Recommended Ratings

| Score | Grade | Meaning |
|---:|---|---|
| 9.0–10.0 | Excellent | Near independent research execution / audit-grade |
| 8.0–8.9 | Strong | High-quality research assistant / agent |
| 7.0–7.9 | Good | Completes most research analyses, but gaps in the closed loop |
| 6.0–6.9 | Developing | Notable research execution weaknesses |
| <6.0 | Weak | Not suitable as a reliable research execution system |

## Why Reproducibility Matters

The credibility of computational research cannot rest on "well-written reports" alone. Nature Methods has proposed a progressive Bronze/Silver/Gold standard for computational reproducibility; the Gold standard requires the entire analysis to run automatically.

This project therefore incorporates code, dependencies, environment, data provenance, execution logs, result artifacts, and third-party verification into the evaluation.

## Roadmap

- [x] Five-dimension scoring framework
- [x] Tyson 2004 initial benchmark
- [x] Research credibility-weighted leaderboard
- [x] Second life-science benchmark (multi-omics: human genomics [humangenomics](benchmarks/humangenomics/) + transcriptomics [love2014](benchmarks/love2014/) + single-cell [zeisel2015](benchmarks/zeisel2015/))
- [x] Round 02 two-project combined evaluation (R02: Tyson2004 + 1000 Genomes Phase 3, four-system A/B/C/D comparison, 0–100 scoring convention fixed)
- [ ] Chemistry / materials benchmark
- [ ] Clinical literature & data analysis benchmark
- [ ] Unified submission format for Agent / LLM / Skill
- [ ] Automated artifact validator
- [ ] Clean-room reproduction
- [ ] GitHub Pages leaderboard
- [ ] Benchmark versioning + leaderboard history

## License

Suggested MIT; specific benchmark data and paper-derived materials should follow their original licenses and copyright requirements.
