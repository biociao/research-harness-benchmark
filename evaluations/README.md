# 每期评测评价（Evaluation Rounds）

每期（round）对应一次对同一 benchmark version 的评测活动，记录：参与系统、评分、证据等级、优缺点、评审意见与下期改进。

| Round | Benchmark | 参与系统 | 结果 | 状态 |
|---|---|---|---|---|
| [R01](round-01-tyson2004-v1.md) | Tyson2004-v1 | DSH 科研代理 / Claude Science | 9.10 / 8.00 | ✅ 完成 |
| [R02](round-02-two-project-combined.md) | 双项目综合（Tyson2004-v1 + Auton2015） | D·DSH×GLM-5.3 / C·DSH×GLM-5.2 / A·DSH×DeepSeek-V1-Flash / B·Claude Science×DeepSeek-V1-Flash | 93.3† / 91.8 / 90.8 / 85.8 | ✅ 完成（D 为暂定第一，02 待实测） |
| R03（规划） | 待定（建议扩大项目样本 / 增加重复） | 待定 | — | ⏳ 待评测 |

## 规则

- 每期必须固定 benchmark version（同版才能横向比较，见 [docs/benchmark-protocol.md](../docs/benchmark-protocol.md)）。
- 评分必须绑定证据（E0–E4），缺证据用 N/A，不得主观补分。
- 模型答卷（复现报告 md）存放于 `benchmarks/<case>/reports/`。
