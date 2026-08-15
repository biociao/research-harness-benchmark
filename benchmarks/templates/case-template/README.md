# Benchmark Case 模板（通用骨架）

> 复制本目录到 `benchmarks/<case-id>/` 并填充。字段含义见 `docs/benchmark-protocol.md`。
> 已完成的参考 case：`benchmarks/tyson2004/`。

## 1. 固定输入（Fixed Inputs）

| 项 | 定义 |
|---|---|
| task prompt | （待填：给 Agent 的任务描述，含可复现目标） |
| source paper(s) | （待填：论文全称、年份、期刊、DOI） |
| permitted data sources | （待填：SRA/GEO/FTP 等公开源，是否禁止第三方预处理数据） |
| permitted software | （待填：工具白名单/黑名单，版本要求） |
| time budget | （待填） |
| compute budget | （待填：CPU/内存/GPU、磁盘） |
| internet policy | （待填：允许联网检索？） |
| human intervention policy | （待填：人工介入上限） |

## 2. Agent 交付物（Deliverables）

```text
report/
  final_report.md
  claims.yaml          # 逐条填写 claim 级结果
  evidence.md
  figures/
code/                  # 实际执行的代码
environment/           # 依赖锁定 / 容器 / conda env
logs/                  # 执行日志
results/               # 结果工件
provenance/            # 数据来源、下载校验（checksum）
```

## 3. Claim 模板（`claims.yaml`）

```yaml
benchmark: <case-id>-v1
title: <论文简称> computational reproduction
claims:
  - claim_id: C01
    statement: <可计算验证的科学论断>
    category: <如 variant_calling / cell_typing / differential_expression>
  - claim_id: C02
    statement: <...>
    category: <...>
    expected: <可选：对复现预期的提示，如 data_availability_must_be_verified>
```

## 4. 评分映射（与 `docs/rubric.md` 对齐）

| 维度 | 本 case 的落点 |
|---|---|
| D1 文献检索与获取 | 找到论文 + 原始数据源 + accession 链 |
| D2 理解与推理 | claims 拆解、结果/解释区分、边界识别 |
| D3 代码与复现规范 | pipeline 真执行、环境锁定、R0–R4 |
| D4 实验设计与可视化 | 与论文结果定量对比、误差/不确定性报告 |
| D5 过程与效率 | runtime / 成本 / 人工介入 / 闭环 |

## 5. 验收（Acceptance）

- [ ] 核心 claims 每一条有 E2+ 证据
- [ ] 代码可重跑（环境锁定）
- [ ] paper-vs-reproduction 对比表
- [ ] 自动评分指标（如有 gold standard）已定义
