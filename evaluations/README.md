# 每期评测评价（Evaluation Rounds）

每期（round）对应一次对同一 benchmark version 的评测活动，记录：参与系统、评分、证据等级、优缺点、评审意见与下期改进。

| Round | Benchmark | 参与系统 | 结果 | 状态 |
|---|---|---|---|---|
| [R01](round-01-tyson2004-v1.md) | Tyson2004-v1 | DSH 科研代理 / Claude Science | 9.10 / 8.00 | ✅ 完成 |
| [R02](round-02-two-project-combined.md) | 双项目综合（Tyson2004-v1 + Auton2015） | D·dsh-science×GLM-5.3 / C·dsh-science×GLM-5.2 / A·dsh-science×DeepSeek-V1-Flash / B·Claude Science×DeepSeek-V1-Flash | 93.3† / 91.8 / 90.8 / 85.8 | ✅ 完成（D 为暂定第一，02 待实测） |
| [R03](round-03-six-system-combined.md) | 双项目复评（Tyson2004-v1 + Auton2015） | A–F 六组合 × 2 论文（12 份报告；新增 F·dsh-science×kimi k3；D/E 的 02 首次实测） | C 93 / D 92.5 / A 91 / F 87 / B 84 / E 81.5⚠️ | ✅ 完成（入库时勘误 D02/E02 标注互换；D 的 02 实测后 R02 暂定第一关闭；E01 与 R02 结论冲突待裁决） |
| [R04](round-04-glm-5.3-flash.md) | GLM-5.3-Flash 单系统 × 3 篇（Tyson2004 + Love2014 + Zeisel2015；**无 Auton/1000G**） | dsh-science × GLM-5.3-Flash | Tyson 43.25⚠️ / Love 52.0⚠️ / Zeisel 51.5⚠️ | ✅ 完成（GPT-5.6-sol 审稿式评分；**不入综合排名**——无 case 02；judge 对参照 bins 判定与 R03 同侪不一致待裁决；Love 评审方差 55.8/52.0 建议第二评审） |
| [R05](round-05-glm-5.3-flash-case02.md) | GLM-5.3-Flash 补做 **case 02**（Auton 2015 / 1000 Genomes Phase 3，chr21）——R04 遗留 #3 | dsh-science × GLM-5.3-Flash（headless 一次性任务，0 人工介入，2 h 34 min） | **02 = 72.5**（GPT-5.6-sol 双样本均值 72.20/72.80，Major Revision，E2；C01 reproduced / C03 partial / C02、C05 unverifiable / C04 not_reproduced）；综合 =（43.25+72.5）/2 = **57.9** | ✅ 复现完成、评审完成；✅ **已并入综合榜**（[leaderboard R05 节](../docs/leaderboard.md)，第 7 位，GPT-5.6-sol 口径，与 R03 评审口径不可直接互比） |
| [R07](round-07-gpt5.6-sol-rosalind-e01review.md) | 两份**异构文档**（① Tyson 2004 **复现报告**；② GPT-5.6 对 workbuddy E01 的**评审稿**） | ① ChatGPT-Rosalind-5.6Sol ② GPT-5.6 | ① 67.5（Major Revision；部分复现成功）② 53.5（Major Revision；不判定复现成功；被评稿自身 56 vs 53 口径矛盾重算） | ✅ 完成（GPT-5.6-sol 审稿式评分；**不入综合排名**——非同类型对象、均非 01+02 完整答卷，与 R06 课件类处理一致） |

## 规则

- 每期必须固定 benchmark version（同版才能横向比较，见 [docs/benchmark-protocol.md](../docs/benchmark-protocol.md)）。
- 评分必须绑定证据（E0–E4），缺证据用 N/A，不得主观补分。
- 模型答卷（复现报告 md）存放于 `benchmarks/<case>/reports/`。
