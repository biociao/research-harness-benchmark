# Round 01 — Tyson2004-v1 评测评价

## 基本信息

| 项 | 值 |
|---|---|
| Round | R01 |
| Benchmark | Tyson2004-v1（Tyson et al. 2004 AMD 微生物组/基因组重建复现） |
| 日期 | 仓库初始化期 |
| 评测方式 | 首轮内部基准（审稿式评分 + claim-level 证据核查） |
| 状态 | ✅ 完成 |

## 参与系统与评分

| Rank | System | Harness | LLM | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | R 等级 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 🥇 1 | DSH 科研代理 | DSH | 待补录 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | R3 |
| 🥈 2 | Claude Science | Claude Science | 待补录 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | R2 |

> 加权公式见 [docs/rubric.md](../docs/rubric.md)；精确值：DSH 9.095→9.10，Claude Science 7.99→8.00。

## Claim 级对比（答卷：[DSH](../benchmarks/tyson2004/reports/dsh-reproduction-report.md) / [Claude Science](../benchmarks/tyson2004/reports/claude-science-reproduction-report.md)）

| claim_id | claim | DSH | Claude Science |
|---|---|---|---|
| C01 | 低多样性群落解析为五个主要 genome bins | ✅ reproduced | ✅ reproduced |
| C02 | scaffold composition / GC / 16S 验证 bin 归属 | ✅ reproduced | ✅ reproduced |
| C03 | 关键碳/氮固定与能量代谢从基因组证据重验 | ✅ reproduced | ✅ reproduced |
| C04 | SNP/重组依赖原始 reads 可独立重算 | ⚠️ partially（reads 部分可得） | ❌ not_reproduced（Sanger reads 不可得） |
| — | unsupervised binning | — | ⚠️ 部分复现（细节偏差） |

## 评审意见

**DSH 科研代理（9.10）**
- 优势：D3（9.3）领先——原始 reads + 现代开源工具链端到端重建，环境/pipeline/结果/artifact/checksum 完整闭环；C04 数据可得性受限时如实标记部分复现，符合"failure is evidence"。
- 短板：D4（8.8）实验设计与可视化的定量对比略弱。
- 建议：核心结论已 E3，正式公开榜单前建议完成一次独立 clean-room verification（E4）。

**Claude Science（8.00）**
- 优势：D2（8.8）领先——科学内容理解、证据辨析、对不可复现结论（C04）的边界识别明确，未隐瞒失败。
- 短板：D3（7.0）明显偏低——无端到端 pipeline，unsupervised binning 仅部分复现，artifact 闭环不完整。
- 建议：补环境锁定与可重跑代码以提升至 E3。

## 遗留问题

1. Harness / LLM 具体版本未记录（待补录）。
2. 正式公开榜单前建议 clean-room verification（E4 独立复现）。
3. 排行榜规则要求同版比较——后续重测不得更换 benchmark version。

## 下期（R02）改进

- 使用已发布的多组学考题（humangenomics / love2014 / zeisel2015）评测新系统。
- 提交时强制填写 `submission.yaml` 的 system.version / token / runtime，补全 D5 证据。
