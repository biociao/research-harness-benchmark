# 每期评测评价（Evaluation Rounds）

每期（round）对应一次对同一 benchmark version 的评测活动，记录：参与系统、评分、证据等级、优缺点、评审意见与下期改进。

| Round | Benchmark | 参与系统 | 结果 | 状态 |
|---|---|---|---|---|
| [R01](round-01-tyson2004-v1.md) | Tyson2004-v1 | DSH 科研代理 / Claude Science | 9.10 / 8.00 | ✅ 完成 |
| [R02](round-02-two-project-combined.md) | 双项目综合（Tyson2004-v1 + Auton2015） | D·dsh-science×GLM-5.3 / C·dsh-science×GLM-5.2 / A·dsh-science×DeepSeek-V1-Flash / B·Claude Science×DeepSeek-V1-Flash | 93.3† / 91.8 / 90.8 / 85.8 | ✅ 完成（D 为暂定第一，02 待实测） |
| [R03](round-03-six-system-combined.md) | 双项目复评（Tyson2004-v1 + Auton2015） | A–F 六组合 × 2 论文（12 份报告；新增 F·dsh-science×kimi k3；D/E 的 02 首次实测） | C 93 / D 92.5 / A 91 / F 87 / B 84 / E 81.5⚠️ | ✅ 完成（入库时勘误 D02/E02 标注互换；D 的 02 实测后 R02 暂定第一关闭；E01 与 R02 结论冲突待裁决） |
| [R04](round-04-glm-5.3-flash.md) | GLM-5.3-Flash 单系统 × 3 篇（Tyson2004 + Love2014 + Zeisel2015；**无 Auton/1000G**） | dsh-science × GLM-5.3-Flash | Tyson 43.25⚠️ / Love 52.0⚠️ / Zeisel 51.5⚠️ | ✅ 完成（GPT-5.6-sol 审稿式评分；**不入综合排名**——无 case 02；judge 对参照 bins 判定与 R03 同侪不一致待裁决；Love 评审方差 55.8/52.0 建议第二评审） |
| [R05](round-05-glm-5.3-flash-case02.md) | GLM-5.3-Flash 补做 **case 02**（Auton 2015 / 1000 Genomes Phase 3，chr21）——R04 遗留 #3 | dsh-science × GLM-5.3-Flash（headless 一次性任务，0 人工介入，2 h 34 min） | **02 = 72.5**（GPT-5.6-sol 双样本均值 72.20/72.80，Major Revision，E2；C01 reproduced / C03 partial / C02、C05 unverifiable / C04 not_reproduced）；综合 =（43.25+72.5）/2 = **57.9** | ✅ 复现完成、评审完成；✅ **已并入综合榜**（[当前总榜](../docs/leaderboard.md)，R05 入榜时第 7 位，GPT-5.6-sol 口径，与 R03 评审口径不可直接互比） |
| [R06](round-06-codedecks-gpt5.6-sol.md) | 两份科研 Harness 培训课件 | Research-Harness-Training-90min / AI-BI-SCI-Claude-Science-Aesthetics | **55.8 / 47.8** | ✅ 完成；课件类交付物，非 Harness 复现方案，不入天梯榜 |
| [R07](round-07-gpt5.6-sol-rosalind-e01review.md) | 两份**异构文档**（① Tyson 2004 **复现报告**；② GPT-5.6 对 workbuddy E01 的**评审稿**） | ① ChatGPT-Rosalind-5.6Sol ② GPT-5.6 | ① 67.5（Major Revision；部分复现成功）② 53.5（Major Revision；不判定复现成功；被评稿自身 56 vs 53 口径矛盾重算） | ✅ 完成（GPT-5.6-sol 审稿式评分；**不入综合排名**——非同类型对象、均非 01+02 完整答卷，与 R06 课件类处理一致） |
| [R08](round-08-biomni-dcscloud.md) | 两份 Tyson 2004 复现报告 | Biomni 标准 / DCS Cloud·Genpilot | **52.5 / 41.5** | ✅ 完成；已纳入 Tyson 单论文分榜，非双项目答卷 |
| [R09](round-09-chatgpt-rosalind-5.6sol-two-reports.md) | 双项目复评（Tyson 2004 + Auton 2015 chr21） | ChatGPT-Rosalind-5.6Sol | **01 = 67.5 / 02 = 68.5 / 综合 = 68.0** | ✅ 完成；GPT-5.6-sol 最终报告口径，两项均 Major Revision |
| [R10](round-10-genpilot-ds-v4-flash.md) | 双项目已有评估归档（Tyson 2004 + Auton 2015 chr21） | Genpilot × DeepSeek-v4-Flash | 原评 79.0 / 78.0；固定权重复算 **78.75 / 78.00**，综合 **78.38** | ✅ 归档；评审者未署名，未本地重跑，已入总榜第 7，不覆盖 R08 |
| [R11](round-11-dsh-science-workdir-audit.md) | **工作目录代码级重评**（Tyson 2004 + Auton 2015 双项目；证据=脚本/日志/中间件/环境，非 HTML） | dsh-science 四家双项目（glm-5.2 / glm-5.3 / kimi-k3 / glm-5.3-flash；deepseek-v4-flash 的 Tyson 目录未存档） | 双项目综合 **76.0 / 75.0 / 70.5 / 66.0**（Tyson 73/69/69/58 + Auton 79/81/72/74）；deepseek 仅 Auton 75 入单项。R03 四家 90–92 下修 13–35 分，R04 flash Tyson 43.25 上修至 69 | ✅ 完成；GLM-5.3-Flash 署名评审 + 评审者独立 clean-room 重算与 13 项载荷抽查（全证实）；**已入总榜**（R11 口径四行）；产出 4 条 humangenomics + 3 条 tyson2004 benchmark 修订证据 |
| [R12](round-12-rosalind-6astra-workdir-audit.md) | 双项目完整工作目录评估（Tyson 2004 + Auton 2015 chr21） | Rosalind × GPT-6 Astra | **Tyson 89.25 / Auton 92.50 / 综合 90.88** | ✅ 完成并入总榜；报告+脚本+数据+环境锁+日志+测试+provenance 口径；静态入口和输入哈希独立核查，未做全量 clean-room 重算 |

## 规则

- 每期必须固定 benchmark version（同版才能横向比较，见 [docs/benchmark-protocol.md](../docs/benchmark-protocol.md)）。
- 评分必须绑定证据（E0–E4），缺证据用 N/A，不得主观补分。
- 模型答卷（复现报告 md）存放于 `benchmarks/<case>/reports/`。

## 其他入口

- [历史评审原稿](reviews/README.md)
- [当前总榜](../docs/leaderboard.md)
- [评分口径与跨轮次争议](../docs/leaderboard-notes.md)
- [培训课件及附件](../materials/README.md)
- [归档约定](../docs/repository-layout.md)
