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
