# 科研场景 Harness 能力排行榜

> 当前为 v0.1 初始化榜单。
> 版本说明：Harness / LLM 列为评测时未记录字段，以"待补录"标注；重测时按 submission.yaml 的 `system.version` 补全。

| Rank | System | Harness | LLM | Type | Benchmark | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | Status | 复现报告 |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 🥇 1 | DSH 科研代理 | DSH (DeepSeek Harness) | 待补录 | Agent | Tyson2004-v1 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | baseline | [报告](../benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | 待补录 | Agent | Tyson2004-v1 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | baseline | [报告](../benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

## 解读

DSH 的主要优势来自 D3：完整的数据→环境→pipeline→结果→artifact 闭环。

Claude Science 的主要优势在 D2：科学内容理解、证据辨析和对不可复现结论的边界识别。

## 注意

本榜单不是模型能力总榜，也不是通用 intelligence 排名。

它评价的是：

> 在指定科研任务、指定规则和指定证据要求下，一个 Harness/Agent/LLM/Skill 完成可靠科研工作的能力。

## 更新记录

- **v0.1（初始）**：Tyson2004-v1，DSH 科研代理 9.10 vs Claude Science 8.00；新增 Harness/LLM 版本列（待补录）。
- 多组学 case（humangenomics / love2014 / zeisel2015）已发布为考题，评测完成后按同一 rubric 追加。
