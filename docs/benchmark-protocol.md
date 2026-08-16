# Benchmark Protocol

## 1. 固定输入

每个 benchmark 必须定义：
- task prompt
- source paper(s)
- permitted data sources
- permitted software
- time budget
- compute budget
- internet policy
- human intervention policy

## 2. Agent 交付物

至少提交：

```text
report/
  final_report.md
  claims.yaml
  evidence.md
  figures/
code/
environment/
logs/
results/
provenance/
```

## 3. Claim-level evaluation

每个主要 scientific claim 使用：

```yaml
claim_id: C01
claim: "..."
paper_reference: "..."
agent_result: "..."
status: reproduced | partially_reproduced | not_reproduced | contradicted
evidence:
  - path: results/...
    type: artifact
confidence: high | medium | low
```

## 4. 复现等级

- R0：没有执行证据
- R1：部分计算复现
- R2：关键结果复现
- R3：端到端 pipeline 可复现
- R4：独立 clean-room 验证

## 5. 排行榜规则

- 同一 benchmark version 才能直接横向比较。
- benchmark version 变化后，旧成绩保留，不覆盖。
- 任何分数必须能回溯到 reviewer scorecard。
- 若证据不足，使用 `N/A`，不得用主观推断补齐。

## 6. 自动化评审（LLM-as-Judge）

`scripts/judge.py` 把 rubric + benchmark 的 claims.yaml + 被评报告组装成固定 prompt
（模板：`scripts/judge_prompt.md`），调用 OpenAI 兼容后端，输出结构化 scorecard JSON，
可直接被 `scripts/score.py` 消费。

```bash
export JUDGE_BASE_URL=https://api.deepseek.com/v1   # 任意 OpenAI 兼容端点
export JUDGE_API_KEY=sk-...
export JUDGE_MODEL=deepseek-chat

# 单次评审
python scripts/judge.py --benchmark benchmarks/tyson2004 \
  --report benchmarks/tyson2004/reports/xxx-report.md \
  --system-name "my-harness" --out scorecard.json

# 重复 3 次独立评审取中位数（评委分歧大的维度会标注，建议人工复核）
python scripts/judge.py --benchmark benchmarks/tyson2004 \
  --report benchmarks/tyson2004/reports/xxx-report.md --repeat 3 --out scorecard.json

python scripts/score.py scorecard.json   # 加权总分
```

评审纪律：

- **评委独立性**：judge 模型不得与被评 harness 所用 LLM 同家族（如不用 GLM 评 GLM 跑出的报告）；
  judge 模型会记录在 scorecard 的 `meta.judge_model` 中，随分数一并公开。
- **自动初评 + 人工终审**：judge 输出的 `integrity_flags` 非空、或 `--repeat` 中某维度
  分差 > 1.5 时，必须人工复核后才能上排行榜。
- **D5 不靠 judge**：runtime / token / 人工介入次数应从 harness 运行日志自动提取填入
  submission.yaml 的 `execution` 字段；judge 对缺少硬数据的 D5 只会给 evidence-limited 低分。
- scorecard JSON 是 reviewer scorecard 的一种，须随评测轮次存档于 `evaluations/` 以便回溯。
