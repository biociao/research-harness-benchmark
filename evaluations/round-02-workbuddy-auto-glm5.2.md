# Round 02 增补 — workbuddy（auto 模式）× GLM-5.2 评测记录（Tyson 2004 / 01）

## 基本信息

| 项 | 值 |
|---|---|
| Round | R02 增补 |
| Benchmark | Tyson2004-v1（01） |
| Harness | workbuddy（auto 模式，自动调度） |
| LLM | GLM-5.2（auto 模式自动调用） |
| 被评报告 | E01_reproduction_report(1).html |
| 评审 | GPT-5.6 审稿 |
| 日期 | 2026-08-16 |
| 评分口径 | `总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%` |
| 评审结论 | ⚠️ **Major Revision / Reproduction Claim Not Established（复现未成立）** |

## 五维评分（0–10 制 → 0–100 制）

| 维度 | 得分 /10 | 折算 /100 | 权重 | 加权 |
|---|---:|---:|---:|---:|
| ① 文献检索与获取 | 7.0 | 70 | 15% | 10.5 |
| ② 内容理解与逻辑推理 | 5.5 | 55 | 30% | 16.5 |
| ③ 代码生成与复现规范 | 4.0 | 40 | 25% | 10.0 |
| ④ 实验设计与结果可视化 | 5.5 | 55 | 20% | 11.0 |
| ⑤ 研究过程与效率 | 5.0 | 50 | 10% | 5.0 |
| **项目分** | | | | **53.0 / 100** |

> 注：评审标题曾写 "56 / 100"，但按其自身 rubric 复算与最终评分卡均为 **53.0**，榜单以 53.0 为准。

## 评审核心发现（摘要）

1. **核心复现 claim 不成立（循环论证）**：报告声称"完整重建论文 5 个基因组 bins"，但 scaffold → organism 的 assignment 直接取自 NCBI GenBank 既有记录，而非按 Tyson 2004 的 GC% + coverage + 系统发育标记方法独立 binning——"5 bins 覆盖 100% 序列"由既有标签汇总得出，不能作为独立验证。
2. **数据来源链断裂**：gene prediction 表中 Leptospirillum II / III、Ferroplasma II 均为 0 个预测基因，后续代谢重建却给这些 bin 大量 Calvin cycle / 固氮基因命中，报告自身无法解释其来源。
3. **不可比指标被标为 Match**：scaffold 序列占比与论文 coverage-based 丰度不直接可比，却被标记为 "✓ Match"。
4. **过程证据缺失**：无 wall-clock / 资源消耗 / 失败重试 / 人工干预记录。

## 榜单处理

- 01 项目分 **53.0** 计入榜单；02（Auton 2015）未实测，综合总分暂按 01 计入（53.0‡），暂列综合榜第 5。
- 评审认为关键问题修复前不应进入正式排名；经用户决定收录入榜，并以 ⚠️ 状态明确标注"复现未成立"。
- 对照意义：与 C（dsh-science × GLM-5.2，01 项目 91.0）同模型不同 Harness，分差 38 分，进一步支持"Harness 结构差异主导科研可信度"的 R02 结论。

## 细节报告

- 评审全文：[benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)
- 完整榜单与更新记录：[docs/leaderboard.md](../docs/leaderboard.md)
