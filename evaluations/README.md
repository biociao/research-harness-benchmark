# 每期评测评价（Evaluation Rounds）

每期（round）对应一次对同一 benchmark version 的评测活动，记录：参与系统、评分、证据等级、优缺点、评审意见与下期改进。

| Round | Benchmark | 参与系统 | 结果 | 状态 |
|---|---|---|---|---|
| [R01](round-01-tyson2004-v1.md) | Tyson2004-v1 | DSH 科研代理 / Claude Science | 9.10 / 8.00 | ✅ 完成 |
| [R02](round-02-two-project-combined.md) | 双项目综合（Tyson2004-v1 + Auton2015） | D·dsh-science×GLM-5.3 / C·dsh-science×GLM-5.2 / A·dsh-science×DeepSeek-V1-Flash / B·Claude Science×DeepSeek-V1-Flash | 93.3† / 91.8 / 90.8 / 85.8 | ✅ 完成（D 为暂定第一，02 待实测） |
| [R03](round-03-six-system-combined.md) | 双项目复评（Tyson2004-v1 + Auton2015） | A–F 六组合 × 2 论文（12 份报告；新增 F·dsh-science×kimi k3；D/E 的 02 首次实测） | C 93 / D 92.5 / A 91 / F 87 / B 84 / E 81.5⚠️ | ✅ 完成（入库时勘误 D02/E02 标注互换；D 的 02 实测后 R02 暂定第一关闭；E01 与 R02 结论冲突待裁决） |
| R04（规划） | 待定 | 待定 | — | ⏳ 待评测（建议：E01 冲突第三方裁决；重复评审/实验与置信区间；chr21 近似 vs 全基因组的计分口径） |

## 规则

- 每期必须固定 benchmark version（同版才能横向比较，见 [docs/benchmark-protocol.md](../docs/benchmark-protocol.md)）。
- 评分必须绑定证据（E0–E4），缺证据用 N/A，不得主观补分。
- 模型答卷（复现报告 md）存放于 `benchmarks/<case>/reports/`。
