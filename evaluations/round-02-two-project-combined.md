# Round 02 — 双项目综合评测评价（Tyson2004 + 1000 Genomes Phase 3）

## 基本信息

| 项 | 值 |
|---|---|
| Round | R02 |
| Benchmark | 双项目：Tyson2004-v1（01）+ Auton 2015 / 1000 Genomes Phase 3（02，humangenomics） |
| 日期 | 2026-08-16 |
| 评测方式 | 审稿式评分（0–100 制五维加权）+ claim-level 证据核查 |
| 状态 | ✅ 完成 |
| 评分口径 | `总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`；综合总分 = 已完成 01、02 两项目的项目分平均值；未完成项目暂按已完成项目分数占位计入（待实测后更新，排名为暂定） |

## 参与系统与综合评分

| Rank | Harness | LLM | 01 项目分 | 02 项目分 | 综合总分 | Status |
|---:|---|---|---:|---:|---:|---|
| 🥇 1 | D · DSH | GLM-5.3 | 93.3 | 93.3† | **93.3†** | 暂列综合 Rank #1（02 未出，暂按 01 计） |
| 🥈 2 | C · DSH | GLM-5.2 | 91.0 | 92.5 | **91.8** | 综合 Rank #2 |
| 🥉 3 | A · DSH | DeepSeek-V1-Flash | 90.6 | 91.0 | **90.8** | 综合 Rank #3 |
| 4 | B · Claude Science | DeepSeek-V1-Flash | 84.4 | 87.1 | **85.8** | 综合 Rank #4 |

**†** D 的 02（Auton 2015）结果尚未产出，暂按 01 分数（93.3）计入；综合总分 93.3 为**暂定值**，待 02 实测后更新，届时排名可能变动。

## 分项目评分

### 01｜Tyson 2004

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · DSH | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| A · DSH | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| B · Claude Science | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| D · DSH | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |

### 02｜Auton 2015（1000 Genomes Phase 3）

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · DSH | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| A · DSH | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| B · Claude Science | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| D · DSH | GLM-5.3 | — | — | — | — | — | **93.3†** |

**†** D 的 02 结果尚未产出，暂按 01 分数（93.3）计入，待实测后更新。

## 关键结论

- **Harness Effect ≈ +5 分**：A 与 B 使用同一 LLM（DeepSeek-V1-Flash），DSH（90.8）比 Claude Science（85.8）高 5.0 分——benchmark 测到的是 Harness 结构差异，而非单纯 LLM 差异。
- **同一 Harness 换更强模型只提升 1.0 分**：A → C（DeepSeek-V1-Flash → GLM-5.2），90.8 → 91.8；科研长任务中 Harness 的作用可能比单纯换模型更显著。
- **GLM-5.3 暂列综合第一（待 02 确认）**：D01 = 93.3 表现突出；02（Auton 2015）结果未出，暂按 01 分数计入，综合总分暂定 **93.3**。此为暂定排名——在 02 实测前，尚不能把「GLM-5.3 一定综合第一」当作定论。

## 评审意见（摘要）

- **C（91.8）**：科研复现工程最完整——五个核心 claim（C1–C5）全部进入独立验证，关键数字经 `bcftools / vcftools` 交叉验证；对 chr21 外推全基因组的系统偏差如实标记为「部分支持」，未伪装成 fully supported。
- **A（90.8）**：两个领域任务都稳定；明确披露 trim-15、LpII 多态率、recombination window 等方法学差异，而不是把「方向一致」包装成「数字完全一致」。
- **B（85.8）**：科研分析不错，但 Harness 工程化（环境锁定、artifact、claim 级验证）弱一档。
- **D（93.3†，暂列第一）**：01 单项目最强——复现 GC-depth 分箱、5 个种群云与群体变异结论，并识别出 nif 类群归属在后续研究中发生的科学修正；02 结果未出，暂按 01 分数计入。

> 注：「显著」目前应理解为 benchmark effect / practical difference，还不能称为统计学显著（仅两个项目，无重复实验或置信区间）。

## 遗留问题

1. 综合排名基于两个项目，样本量小，尚无重复实验与置信区间。
2. D（GLM-5.3）的 02（Auton 2015）项目尚未实测，当前综合分（93.3）为暂按 01 计入的占位值，待实测后更新排名。
3. 分项目与综合评分的原始证据（artifacts / provenance）保存在各 Harness 运行产物中，仓库内以审稿记录为准。

## 细节报告

- 完整审稿式评测（评分依据、claim 级证据、方法学披露）：[benchmarks/Review/260816 bench.txt](../benchmarks/Review/260816%20bench.txt)
- Case 详情：Tyson 2004（[benchmarks/tyson2004/](../benchmarks/tyson2004/)）、1000 Genomes Phase 3（[benchmarks/humangenomics/](../benchmarks/humangenomics/)）
- 完整榜单与更新记录：[docs/leaderboard.md](../docs/leaderboard.md)

## 下期（R03）改进

- 为 D（GLM-5.3）完成 02 项目实测，替换当前占位分；或增加第三项目以扩大综合榜样本。
- 增加重复实验 / 置信区间，使「Harness Effect ≈ +5」从 practical difference 走向统计检验。
