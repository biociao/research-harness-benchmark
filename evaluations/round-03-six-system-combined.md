# Round 03 — 六系统双项目复评记录（A–F × Tyson 2004 + 1000 Genomes Phase 3）

## 基本信息

| 项 | 值 |
|---|---|
| Round | R03 |
| Benchmark | 双项目复评：Tyson2004-v1（01）+ Auton 2015 / 1000 Genomes Phase 3（02，humangenomics） |
| 日期 | 2026-08-17 |
| 被评对象 | 12 份复现报告：6 组合（A–F）× 2 论文（A01–F02） |
| 评审 | 外部评审（未署名，评审模型待补录）；评审全文见 [round-03-A-F.md](round-03-A-F.md) |
| 评测方式 | 审稿式逐份评分：五维 0–10 制 Rubric（《科研 Agent 五维评价框架》）；评审自述"第⑤维效率按报告中可验证的效率证据给分" |
| 状态 | ✅ 完成 |
| 评分口径 | 评审按 0–10 制打分，本记录 ×10 换算为 R02 起固定的 0–100 制（五维权重不变）；单报告分采用评审推荐的"12 份报告的单份评分"总表；**综合总分见下方「换算与复算说明」（含 D02/E02 勘误互换重算）**，另附按固定公式复算值供核查 |

## 组合身份对照（字母沿用 R02 编号）

| 组合 | Harness | LLM | 身份依据（R03 ↔ R02 内容核对） |
|---|---|---|---|
| A | dsh-science | DeepSeek-V1-Flash | R03 A01 的方法学披露（trim-15 近似、LpII 多态率 ~0.198% vs 原文 0.08%、重组窗口 10 kb→500 bp）与 R02 A01 审稿记录一致 |
| B | Claude Science | DeepSeek-V1-Flash | "科学判断不错、工程化弱一档"的两轮评审结论一致（R02 85.8 ↔ R03 84） |
| C | dsh-science | GLM-5.2 | R03 C01 脚本链 / artifact-provenance 组织、C02 vcftools 交叉验证与 R02 C 审稿记录一致 |
| D | dsh-science | GLM-5.3 | R03 D01 的 nif 归属科学修正等与 R02 D01 一致；**02 为本轮首次实测**（关闭 R02 遗留问题） |
| E | workbuddy（auto 模式） | GLM-5.2 | R03 E01 关键数值（2,731 scaffolds / 16.5 Mb / 5 bins / 18,214 protein-coding genes）与 R02 收录的 `E01_reproduction_report(1).html` 完全一致，判定为同一份报告；02 为新产出结果 |
| F | dsh-science | kimi k3 | R03 新增组合（F01：canu 超高覆盖停滞改用 miniasm、未获正文全文如实声明；F02：显式环境锁定、自实现 Weir–Cockerham Fst、下载截断后 Content-Length 校验重试） |

## 综合排行榜（R03，0–100 制换算）

| Rank | 组合 | 01 项目分 | 02 项目分 | **综合总分 /100** | 评审结论 |
|---:|---|---:|---:|---:|---|
| 🥇 1 | **C · dsh-science × GLM-5.2** | 94 | 92 | **93** | 最均衡，科研复现工程化程度最高（第一梯队） |
| 🥈 2 | **D · dsh-science × GLM-5.3** | 93 | 92 | **92.5** | 两个项目都强：Tyson 深度突出、1000G claim-level 全 PASS（第一梯队） |
| 🥉 3 | **A · dsh-science × DeepSeek-V1-Flash** | 91 | 91 | **91** | 科学推理强，结果验证充分（第一梯队） |
| 4 | **F · dsh-science × kimi k3** | 83 | 90 | **87** | 逻辑严谨、复现意识强（第二梯队） |
| 5 | **B · Claude Science × DeepSeek-V1-Flash** | 82 | 86 | **84** | 研究判断不错，但工程化不足（第三梯队） |
| 6 | **E · workbuddy（auto）× GLM-5.2** | 77⚠️ | 86 | **81.5⚠️** | 能完成任务，但 Tyson 报告深度明显不足（第四梯队）；⚠️ 与 R02 评审结论冲突，见下 |

> **换算与复算说明（含 2026-08-17 勘误）**：入库时确认评审原文将 **D02 与 E02 两份报告的标注互换**（「D02」节的 ARI 0.872 报告实为 E02，「E02」节的 ARI 0.9106 / vcftools 逐位一致报告实为 D02），按正确归属入库：**D02 = 92、E02 = 86**；D/E 综合分按两项目平均重算（D 92.5、E 81.5），C/A/F/B 沿用评审综合分（93 / 91 / 87 / 84，与其两项目平均一致或四舍五入）。若按项目固定公式（`0.15×文献 + 0.30×理解 + 0.25×复现 + 0.20×实验 + 0.10×效率`）对五维原始分复算并取两项目平均，则为 C 93.8 / D 93.6 / A 91.7 / F 87.3 / B 84.9 / E 82.5——名次与综合榜一致。

> **⚠️ E01 两轮评审结论冲突**：R03 评审给出 E01 = 77，其描述的关键数值与 R02 收录的 workbuddy 同一提交完全一致；而 R02 的 GPT-5.6 审稿对该提交判定 **53.0 / Major Revision（复现未成立）**——核心 binning 直接采用 NCBI 既有 organism assignment（循环论证）、gene prediction 与代谢重建之间数据来源链断裂（详见 [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)）。R03 评审未涉及上述两个问题。两轮对同一提交的结论冲突，**E 的分数与名次待第三方评审或 clean-room 核验裁决**；本榜暂按 R03 评审收录，R02 结论保留在案。

## 分项目评分（0–10 制 ×10 换算；五维列 = 评审原始分 ×10，项目分 = 评审单报告总评 ×10）

### 01｜Tyson 2004

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| C | dsh-science | GLM-5.2 | 95 | 96 | **97** | 93 | 88 | **94** |
| D | dsh-science | GLM-5.3 | 94 | 96 | 95 | **94** | 88 | **93** |
| A | dsh-science | DeepSeek-V1-Flash | 90 | 94 | 92 | 90 | 87 | **91** |
| F | dsh-science | kimi k3 | 80 | 87 | 84 | 82 | 80 | **83** |
| B | Claude Science | DeepSeek-V1-Flash | 80 | 87 | 81 | 82 | 80 | **82** |
| E | workbuddy（auto） | GLM-5.2 | 75 | 82 | 75 | 78 | 76 | **77⚠️** |

### 02｜Auton 2015（1000 Genomes Phase 3）

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| C | dsh-science | GLM-5.2 | 90 | **94** | **96** | **92** | **88** | **92** |
| D | dsh-science | GLM-5.3 | **91** | **94** | **96** | **92** | 87 | **92** |
| A | dsh-science | DeepSeek-V1-Flash | 90 | **94** | 94 | 90 | 87 | **91** |
| F | dsh-science | kimi k3 | 90 | 93 | 92 | 91 | 85 | **90** |
| B | Claude Science | DeepSeek-V1-Flash | 87 | 89 | 88 | 86 | 80 | **86** |
| E | workbuddy（auto） | GLM-5.2 | 82 | 90 | 89 | 88 | 80 | **86** |

## 评审要点（摘要）

- **C（93，综合第一）**：Tyson 复现组织成完整 provenance 链（AADL01 → SRR9434122–25 → binning → nif → SNP rate → abundance → reference recovery），脚本入口链明确；没有把现代数据重算值冒充论文原值，解释了 2.4× read depth 等偏差来源。1000G 把复现做成 claim-level verification：明确 chr21 v5b / 2,504 个体 / 26 人群，环境锁定、md5/SHA-256、30–60 分钟单机重跑说明；Fst 实现与 vcftools 逐位交叉验证（0.02388，n=7,335）——oracle 式独立验证。扣分：仅 chr21、SI Table 5 OCR 问题。
- **A（91）**：发现 GenBank 沉积组装与论文 scaffold 集不一致，独立 SPAdes 重组装（1,061 scaffolds / 9.39 Mb / 84.9% reads 利用 / 覆盖度 83–96%）；主动披露 trim-15、LpII 多态率 0.198% vs 0.08%、重组窗口改动等方法学差异。1000G：singleton 与 Table 1 差异 ≤3%、PCA ARI=0.905、Fst 与 SI Table 5 相关 0.997，同时披露绝对尺度差异；工程结构完整（data/code/experiments/artifacts/envs/reviews）。扣分：部分全基因组 claim 被压缩成 chr21 验证，"五项全部复现"表述偏积极。
- **D（92.5）**：Tyson 方向另一份最强报告（9.3），H1–H4 → E01–E04 → artifacts → provenance → reproduction 的研究组织；并区分"原始论文结论"与"现代科学结论"（nif 归属 L. group II → L. group III 的后续修正）。1000G（02 首次实测，9.2）：claim-level 全 PASS——singleton 误差 ≤2.5%、indel burden <2%、PCA ARI=0.9106、WC84 Fst 与 vcftools 对齐后逐位一致，并记录实际 bug（singleton index 0/1-based、PLINK bed 2-bit 基因型映射）修复后重跑的 debugging provenance。
- **F（87）**：边界意识好（正文未获取、依赖摘要/课件/数据库交叉核对；canu 停滞改用 miniasm；SNP/FerroII mosaic 未完整验证如实标记）；1000G 工程规范强（显式锁定、一键重建、自实现 WC84 Fst），下载静默截断后以临时文件 + Content-Length 校验重试；最终 4/5 claim 支持、C4 inconclusive。
- **B（84）**：科学理解正确（GC+tetranucleotide、nifH/D/K、LpIII 固氮、对 Sanger reads 不可重算的判断），但工程证据链（环境锁定、artifact、执行日志）弱一档；1000G（8.6）明显强于 Tyson（8.2），如实报告 ARI≈0.87 / 去 AMR 0.9887，交付物完整。
- **E（81.5⚠️）**：Tyson 报告"仪表盘化"（文献证据链短、偏差解释有限、代码/依赖/测试信息不足）；1000G（86）好于 01——完整 claim-level reproduction，但 C4 ARI 实际 0.872 未达 0.9 阈值（去 AMR 后 0.9887），如实报告并解释 AMR 混合祖源原因。注意：其 01 分与 R02 GPT-5.6 审稿（53.0，Major Revision）冲突，见上方说明。

## 横向发现（评审报告第四节）

1. **证据闭环拉开差距**：高分组合的共同点是 `论文 claim → 原始数据 → 代码 → 中间结果 → 独立验证 → 结论 → 局限` 的闭环（C02 vcftools 交叉验证、D02 bug 修复后重跑），比"报告写得漂亮"高一个层级。
2. **发现复现失败是高分行为**：B02（ARI 0.87 不强行 PASS）、F02（4/5 支持、1 个 inconclusive）、F01（SNP/重组直接标未复现）、A01（承认 ~2 倍方法学差异）、D01（指出 nif 归属后续修正）。
3. **最大共同问题**：多数 1000G 报告以 **chr21** 支撑 C4 PCA / burden / Fst / 部分 variant count，对应论文是全基因组 / 26×26 population analysis——评审建议正式结论严格区分 **"claim supported"** 与 **"paper-level exact reproduction"**，并把"chr21 结果表述成全基因组复现"作为重点扣分项；这也是本轮没有任何 1000G 单项给满分的原因。

## 跨轮次核对（R02 → R03）

- **D 的 02 首次实测（92）**：R02 遗留问题"暂按 01 分数占位（93.3†）"关闭。D 综合 92.5（第 2），与 C（93）仅差 0.5——R02 "待实测后更新排名"的谨慎表述是必要的：实测口径下 C 居首，但 C/D 差距在评审间方差（±3 分）内，名次顺序不宜过度解读。
- **同一提交的两轮评审方差**：C01 91.0→94、D01 93.3→93、A01 90.6→91、B01 84.4→82（±3 以内），方向一致；唯一例外是 E01 53.0→77，源于 R03 评审未核查 binning 独立性与数据来源链（见冲突说明）。提示：单人评审下 1–2 分的名次差异不足以定性，高分段建议第二评审（与 CONTRIBUTING 的要求一致）。
- **E02（86）**：workbuddy 首次 1000G 实测，好于其 01（77），将其综合分从 R02 的 53.0‡（未完成 02）抬升——但 E01 冲突未裁决前，E 名次应视为暂定。

## 遗留问题

1. R03 评审者身份待补录（F 组合身份已补录：dsh-science × kimi k3）。
2. E01 两轮评审结论冲突（53.0 Major Revision vs 77）未裁决，E 的名次与分数暂定。
3. 评审间方差 ±3 分：差距 <2 分的组合（如 R03 中 C 93 vs D 92.5）不宜下强结论，需重复评审或重复实验。
4. "chr21 近似 vs 全基因组 claim"的表述问题普遍存在，建议 R04 rubric 显式区分两档并分别计分。
5. 评审原文存在 D02/E02 标注互换（2026-08-17 勘误入库，原文顶部已附勘误说明）；后续复核请以调换后的归属为准。

## 细节报告

- R03 评审全文（12 份报告逐一评分与横向发现；顶部附 D02/E02 勘误说明）：[round-03-A-F.md](round-03-A-F.md)
- R02 评测记录（组合编号与历史分数来源）：[round-02-two-project-combined.md](round-02-two-project-combined.md)
- R02 workbuddy 评审全文（E01 冲突的另一侧证据）：[benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)
- 完整榜单与更新记录：[docs/leaderboard.md](../docs/leaderboard.md)

## 下期（R04）建议

- 补录 F 身份与 R03 评审者信息；对 E01 引入第三方评审或 clean-room 核验以裁决冲突。
- 增加重复评审 / 重复实验与置信区间，量化评审间方差（当前 ±3 分）。
- 在 rubric 中明确区分 "claim supported" 与 "paper-level exact reproduction"，对 chr21 外推表述统一计分口径。
