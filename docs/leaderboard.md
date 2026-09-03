# 科研场景 Harness 能力排行榜

> 榜单规则：同版 benchmark 才能横向比较；评分必须绑定证据（E0–E4），见 [benchmark-protocol.md](benchmark-protocol.md) 与 [rubric.md](rubric.md)。
> 评分口径（R02 起）：五维加权 0–100 制，`总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`；综合总分 = 已完成 01、02 两项目的项目分平均值；未完成项目暂按已完成项目分数占位计入（待实测后更新，排名为暂定）。R03 起六组合均已完成两项目实测，无占位分。
>
> **Harness 说明**：榜单中的 **dsh-science**（早期记录写作 DSH / dsh）是运行于 DeepSeek Harness 之上的科研场景插件，负责执行本仓库的评测任务；源码与文档见 <https://github.com/biociao/dsh-science>。R02 起统一使用 dsh-science 表述，历史轮次（R01）保留原始记录。

## Round 07 & Round 08 — 01 Tyson 2004 复现报告 GPT-5.6-sol 评测排名（单论文榜）

> **口径**：这三份**都是 01 Tyson 2004 复现报告**，全部由 **GPT-5.6-sol**（codex CLI，与 R04/R05 同判读口径）逐份五维 0–10 制评分 ×10 折算——**同评审者、同框架、同对象，分值直接可比**，故纳入「01 Tyson 2004」**单论文排名**。它们**不是「01 Tyson + 02 Auton」双项目完整答卷**，因此**不计综合排行榜总分**（综合榜需 01+02 两项目），但在 01 单论文维度上给名次。评测记录见 [evaluations/round-08-biomni-dcscloud.md](../evaluations/round-08-biomni-dcscloud.md) 与 [evaluations/round-07-gpt5.6-sol-rosalind-e01review.md](../evaluations/round-07-gpt5.6-sol-rosalind-e01review.md)。

**01｜Tyson 2004 复现报告单论文排名（GPT-5.6-sol）**

| Rank | 复现报告 | 加权分 /100 | D1 | D2 | D3 | D4 | D5 | 审稿结论与关键判定 |
|:--:|---|---:|---:|---:|---:|---:|---:|---|
| 🥇 1 | ChatGPT-Rosalind-5.6Sol · `tyson2004_reproduction.html` | **67.5** | 7 | 8 | 6 | 6 | 6 | Major Revision · 部分复现成功；D2=8 把握证据边界（能复现/独立复现/仅原文复核），深至 2004 contig 批次与\"共识序列不可用于重估 SNP 率\"；但 SNP/重组/FISH/ORF/代谢仅原文复核 |
| 🥈 2 | phylo-biomni-standard · `tyson2004_reproduction.html` | **52.5** | 8 | 5 | 5 | 3 | 7 | Major Revision · 真实端到端复现尝试但部分复现；**唯一从原始 Sanger reads 起算**（D1/D5=8/7 最高），但 **7 图全 broken** 致 D4=3，单一 `nifH` 命中过度升为机制结论 |
| 🥉 3 | dcsCloud · `Tyson2004_Reproduction.html` | **41.5** | 5 | 3 | 4 | 5 | 5 | Major Revision · **非端到端复现**（基于论文已发布重构基因组再分析，未从 reads 起算）；碳固定\"未检出\"与论文不符、nif 归因偷换、e-value 误当复现显著 |

> 📌 **补充参考**：R04 的 dsh-science×GLM-5.3-Flash 也以 GPT-5.6-sol 得到 **01 Tyson = 43.25**（见综合榜第 7 行），介于 dcsCloud（41.5）与 Biomni（52.5）之间，属同一 GPT-5.6-sol 口径的 01 单论文分数。
> ⚠️ **与 R03 六组合不混排**：R03 六组合（01 分 94/93/91/83/82/77）出自 R03 外部评审、且为双项目完整答卷，与上方 GPT-5.6-sol 单论文榜**非同口径、非同类对象**，故只并列不混排。

> **⚠️ 对比提醒**：Rosalind（67.5）与 dcsCloud（41.5）同为\"成品/半成品复现报告\"类，但 Rosalind 深至 2004 contig 批次与 SNP 方法学判断（D2=8），dcsCloud 仅两基因组再注释（D2=3）；Biomni（52.5）是三者中**唯一真正从原始 reads 起算的端到端尝试**（D1=8/D5=7 最高），却因图全部缺失被砍到 D4=3。

## Round 07（非排名）— 一份评审文档 GPT-5.6-sol 五维评测留存

> **不入综合排行榜**：本项被评对象是 **GPT-5.6 对 workbuddy E01 的评审稿**（`Review_E01_不建议判定为“论文复现成功”.md`）——这是**评审文档**，不是复现报告，也不是双项目答卷，故与 R06（课件类交付物）一致、仅作逐份五维评测留存。**注**：R07 同时评的另一份 ChatGPT-Rosalind 复现报告（67.5）已在上面「01 Tyson 2004 单论文排名」中排入，此处不再重复。评测方式：GPT-5.6-sol（codex CLI，`codex exec -s read-only`，与 R04–R06 同口径）逐份 0–10 制评分 ×10 折算。记录见 [evaluations/round-07-gpt5.6-sol-rosalind-e01review.md](../evaluations/round-07-gpt5.6-sol-rosalind-e01review.md)。

| 文档 | 类型 | 加权总分 /100 | 审稿结论 | D1 | D2 | D3 | D4 | D5 | 关键判定 |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---|
| GPT-5.6 · `Review_E01_不建议判定为“论文复现成功”.md` | 评审文档 | **53.5** | Major Revision | 7 | 6 | 4 | 5 | 5 | 循环验证/来源链断裂/指标错配三处硬伤；被评稿自身 56 vs 53 口径矛盾，按整数分重算 53.5 |
## Round 03 — 六系统双项目复评榜（Tyson2004-v1 + Auton2015 / 1000 Genomes Phase 3）

> R03 为外部评审对 12 份复现报告（6 组合 × 2 论文）的逐份审稿式复评：评审按 0–10 制打分，本榜 ×10 换算为 0–100 制；综合总分取评审给出的综合分（D/E 因勘误互换按两项目平均重算）。组合字母沿用 R02 编号（A–E 身份经报告内容核对沿用；**F 为新增组合（dsh-science × kimi k3，身份已补录）**）。**D 的 02 为本轮首次实测**，R02 的 93.3† 占位值由此关闭。**勘误（2026-08-17）**：评审原文将 D02 与 E02 标注互换（ARI 0.9106 / vcftools 逐位一致的报告实为 D02、ARI 0.872 的报告实为 E02），入库时已按正确归属调换：D02=92 / E02=86。评测记录：[evaluations/round-03-six-system-combined.md](../evaluations/round-03-six-system-combined.md)。

| Rank | Harness | LLM | 01 项目分 | 02 项目分 | **综合总分 /100** | 显著特点 |
|---:|---|---|---:|---:|---:|---|
| 🥇 1 | dsh-science | GLM-5.2 | 94 | 92 | **93** | 最均衡，科研复现工程化程度最高：provenance 链、oracle 式交叉验证（Fst 与 vcftools 逐位一致 0.02388 / n=7,335）、环境锁定与单机重跑说明 |
| 🥈 2 | dsh-science | GLM-5.3 | 93 | 92 | **92.5** | 两个项目都强：Tyson（H1–H4→E01–E04 结构、nif 归属科学修正）+ 1000G claim-level 全 PASS（ARI 0.9106、WC84 Fst 与 vcftools 逐位一致），留存 bug 修复 provenance |
| 🥉 3 | dsh-science | DeepSeek-V1-Flash | 91 | 91 | **91** | 科学推理强：发现 GenBank 沉积组装与论文不一致并独立重组装；方法学差异披露与结果验证充分 |
| 4 | dsh-science | kimi k3 | 83 | 90 | **87** | 严谨：未获全文/canu→miniasm 等边界如实披露；显式环境锁定、自实现 WC84 Fst、下载截断 Content-Length 校验重试；4/5 claim 支持 |
| 5 | Claude Science | DeepSeek-V1-Flash | 82 | 86 | **84** | 科学判断不错（ARI 0.87 未强行 PASS），但工程化证据链明显落后 |
| 6 | workbuddy（auto 模式） | GLM-5.2 | 77 | 86 | **81.5⚠️** | Tyson 报告"仪表盘化"、深度不足；1000G（86）好于 01，C4 ARI 0.872 未达 0.9 阈值但如实报告并解释 AMR 原因 |

**⚠️ E01 评审冲突**：R03 评审给出 E01 = 77，其关键数值（2,731 scaffolds / 16.5 Mb / 5 bins / 18,214 genes）与 R02 收录的 workbuddy 同一提交完全一致，而 R02 的 GPT-5.6 审稿判定该提交 **53.0 / Major Revision（复现未成立）**（binning 采用 NCBI 既有 assignment、数据来源链断裂，见[评审全文](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)）。R03 评审未涉及上述问题；两轮结论冲突，E 的分数与名次待第三方评审 / clean-room 核验裁决，暂按 R03 评审收录、R02 结论保留在案。另：按两项目平均 E 综合为 81.5、按固定公式复算为 82.5，均为第 6。

### 分项目评分

**01｜Tyson 2004**

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| C | dsh-science | GLM-5.2 | 95 | 96 | **97** | 93 | 88 | **94** |
| D | dsh-science | GLM-5.3 | 94 | 96 | 95 | **94** | 88 | **93** |
| A | dsh-science | DeepSeek-V1-Flash | 90 | 94 | 92 | 90 | 87 | **91** |
| F | dsh-science | kimi k3 | 80 | 87 | 84 | 82 | 80 | **83** |
| B | Claude Science | DeepSeek-V1-Flash | 80 | 87 | 81 | 82 | 80 | **82** |
| E | workbuddy（auto） | GLM-5.2 | 75 | 82 | 75 | 78 | 76 | **77⚠️** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| C | dsh-science | GLM-5.2 | 90 | **94** | **96** | **92** | **88** | **92** |
| D | dsh-science | GLM-5.3 | **91** | **94** | **96** | **92** | 87 | **92** |
| A | dsh-science | DeepSeek-V1-Flash | 90 | **94** | 94 | 90 | 87 | **91** |
| F | dsh-science | kimi k3 | 90 | 93 | 92 | 91 | 85 | **90** |
| B | Claude Science | DeepSeek-V1-Flash | 87 | 89 | 88 | 86 | 80 | **86** |
| E | workbuddy（auto） | GLM-5.2 | 82 | 90 | 89 | 88 | 80 | **86** |

## Round 05（最新）— GLM-5.3-Flash 补测 case 02 并入综合榜（Auton 2015 / 1000 Genomes Phase 3）

> **说明**：R05 补齐 R04 遗留的 case 02 缺口——dsh-science × **GLM-5.3-Flash** 以 headless 一次性任务完成 Auton 2015 / 1000 Genomes Phase 3（chr21）独立复现（**0 人工介入，2 h 34 min**），GPT-5.6-sol **双独立样本**评审（72.20 / 72.80，方差 0.6，verdict 均为 Major Revision，证据等级 E2），**官方采用 72.5**。本次评审输入为**答卷全文 + 完整代码 + 环境锁 + 执行证据**（全代码口径），D3 = 7.6（均值）显著高于 R04 的 4.5–6.0，证实 R04「D3 受截断影响」的判断。评审记录见 [evaluations/round-05-glm-5.3-flash-case02.md](../evaluations/round-05-glm-5.3-flash-case02.md)，评审全文见 [evaluations/gpt5.6-review-glm5.3flash-case02.md](../evaluations/gpt5.6-review-glm5.3flash-case02.md)。

| GLM-5.3-Flash 双项目 | 加权总分 /100 | 审稿结论 | 证据等级 | D1 | D2 | D3 | D4 | D5 | 关键判定 |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| 01 Tyson 2004（R04 评） | **43.25⚠️** | Major Revision | E1 | 6.0 | 4.0 | 4.5 | 4.0 | 3.0 | 参照 bins 判输入违规 |
| 02 Auton 2015 / 1000G（R05 评，双样本均值） | **72.5** | Major Revision | E2 | 8.4 | 6.5 | 7.6 | 6.7 | 8.0 | C01 reproduced；C03 partial；C02/C05 unverifiable（Supp Table 1 勘误成立但替代判据不等价）；C04 not_reproduced（ARI 0.8742<0.9） |
| **综合总分 =（43.25 + 72.5）/ 2** | **57.9** | — | — | — | — | — | — | — | GPT-5.6-sol 口径 |

### 综合排行榜（R05 更新，7 系统）

| Rank | Harness | LLM | 01 项目分 | 02 项目分 | **综合总分 /100** | 评审口径 |
|---:|---|---|---:|---:|---:|---|
| 🥇 1 | dsh-science | GLM-5.2 | 94 | 92 | **93** | R03 评审 |
| 🥈 2 | dsh-science | GLM-5.3 | 93 | 92 | **92.5** | R03 评审 |
| 🥉 3 | dsh-science | DeepSeek-V1-Flash | 91 | 91 | **91** | R03 评审 |
| 4 | dsh-science | kimi k3 | 83 | 90 | **87** | R03 评审 |
| 5 | Claude Science | DeepSeek-V1-Flash | 82 | 86 | **84** | R03 评审 |
| 6 | workbuddy（auto 模式） | GLM-5.2 | 77 | 86 | **81.5⚠️** | R03 评审 |
| 7⚠️ | dsh-science | **GLM-5.3-Flash** | 43.25 | 72.5 | **57.9⚠️** | **GPT-5.6-sol（01=R04 单样本；02=R05 双样本均值）** |

**⚠️ 口径警告（必读）**：GLM-5.3-Flash 是目前**唯一**被 GPT-5.6-sol 完整评审双项目的系统，其 57.9 与 R03 六组合的分数**出自不同评审口径，不可直接同台比较**——R03 评审未核查参照 bins 独立性等问题（同家族 dsh-science×GLM-5.3 的 Tyson 得 93，而 GPT-5.6-sol 对方法类似的 GLM-5.3-Flash Tyson 判 43.25，分差 ~50，见 R04 一致性警告）。R05 的 72.5 为全代码口径双样本均值，已是更严格的评审基线；**严格的同台排名需以 GPT-5.6-sol 全代码口径复评 R03 六组合**（后续工作）。本榜按分值排序仅供展示，名次解读须结合口径列。

## Round 04 — GLM-5.3-Flash 三篇复现 GPT-5.6 评测（01 Tyson 部分；case 02 已于 R05 补测）

> **说明**：R04 为单系统（dsh-science × **GLM-5.3-Flash**）× 3 篇独立复现报告（**Tyson 2004 / Love 2014 DESeq2 / Zeisel 2015**）的 GPT-5.6-sol 审稿式评分。GLM-5.3-Flash 当时**未完成** Auton 2015 / 1000 Genomes Phase 3（=R03 的 case 02），故 R04 无法按「01 Tyson + 02 Auton」口径并入综合排行榜——**该缺口已于 R05 补齐（02 = 72.5，见上），并入完成**。
>
> **评测方式**：GPT-5.6-sol（codex CLI，`codex exec -s read-only`）逐份五维 0–10 制评分，加权折算 0–100；评审输入为**报告叙述 + 交付物清单**（代码/日志内联被概括省略，judge 据此压低 D3——R05 全代码口径下 D3 回升到 7.6，印证该影响）。评审记录见 [evaluations/round-04-glm-5.3-flash.md](../evaluations/round-04-glm-5.3-flash.md)。

| GLM-5.3-Flash 复现报告 | 加权总分 /100 | 审稿结论 | 推荐评级 | D1 | D2 | D3 | D4 | D5 | 关键 integrity flag |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| **Tyson 2004** | **43.25⚠️** | Major Revision | Weak | 6.0 | 4.0 | 4.5 | 4.0 | 3.0 | `prohibited_reference_use`（参照 bins 支撑结论） |
| **Love 2014 (DESeq2)** | **52.0⚠️** | Major Revision | Developing | 6.0 | 5.0 | 6.0 | 5.0 | 3.0 | `claim_substitution`（统计核心命题被替换） |
| **Zeisel 2015** | **51.5⚠️** | Major Revision | Developing | 6.0 | 4.5 | 6.0 | 5.0 | 4.0 | `evaluation_label_leakage`（评分标签参与选分辨率） |

**⚠️ 一致性警告**：R03 中 dsh-science×GLM-5.3 的 Tyson 得 **93**，而该报告同样引用 NCBI 参照 bins；GPT-5.6-sol 却把 GLM-5.3-Flash 的"参照 bins 支撑结论"判为**输入违规**并压到 43（分差 ~50）。需人工复核判定是否一致（可能是 judge 更严，也可能 GLM-5.3-Flash 更依赖参照）。另 Love 两次采样 55.8 / 52.0，评审方差已显现，建议第二评审。

## Round 02 — 双项目综合榜（Tyson2004-v1 + Auton2015 / 1000 Genomes Phase 3）

> 历史轮次，最新结果以 Round 03 为准。D 的 02 已在 R03 首次实测（92 → 综合 92.5），本榜的 93.3† 暂定值与"暂列第一"状态已被 R03 结果取代。

| Rank | System | Harness | LLM | 01 项目分 | 02 项目分 | **综合总分 /100** | Status | 显著特点 |
|---:|---|---|---|---:|---:|---:|---|---|
| 🥇 1 | D · dsh-science | dsh-science | GLM-5.3 | 93.3 | 93.3† | **93.3†** | 暂列综合 Rank #1（02 未出，暂按 01 计） | 01 表现突出；科学判断、结果复现、研究状态管理最强 |
| 🥈 2 | C · dsh-science | dsh-science | GLM-5.2 | 91.0 | 92.5 | **91.8** | 综合 Rank #2 | 科研复现工程最完整；claim-level 验证、交叉工具、环境锁定、artifact/provenance 最成熟 |
| 🥉 3 | A · dsh-science | dsh-science | DeepSeek-V1-Flash | 90.6 | 91.0 | **90.8** | 综合 Rank #3 | 综合科研能力很强；两个领域任务都稳定，方法学差异披露尤其好 |
| 4 | B · Claude Science | Claude Science | DeepSeek-V1-Flash | 84.4 | 87.1 | **85.8** | 综合 Rank #4 | 科研分析不错，但 Harness 工程化弱一档 |
| 5 | E · workbuddy | workbuddy（auto 模式） | GLM-5.2 | 53.0‡ | — | **53.0‡** | ⚠️ 复现未成立（Major Revision），暂列榜末 | 核心 binning 直接采用 NCBI 既有 organism assignment，复现 claim 不成立；gene prediction 与代谢重建存在数据来源链断裂 |

**†** D 的 02（Auton 2015）结果尚未产出，暂按 01 分数（93.3）计入；综合总分 93.3 为**暂定值**，待 02 实测后更新，届时排名可能变动。

**‡** E（workbuddy × GLM-5.2）仅完成 01（Tyson 2004），评审（GPT-5.6 审稿）结论为 **Major Revision / 复现未成立**：五维得分 文献 7.0 / 理解 5.5 / 复现 4.0 / 实验 5.5 / 效率 5.0（0–10 制），加权 **53.0 / 100**（评审标题曾写 56，按其自身 rubric 复算与最终评分卡为 53.0，以 53.0 为准）。评审认为关键问题（binning 非独立复现、结果来源链断裂）修复前不应进入正式排名；此处按用户要求收录并明确标注状态。评审全文见 [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)。

### 分项目评分

**01｜Tyson 2004**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| A · dsh-science | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| B · Claude Science | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| D · dsh-science | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |
| E · workbuddy（auto） | GLM-5.2 | 70 | 55 | 40 | 55 | 50 | **53.0‡** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| A · dsh-science | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| B · Claude Science | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| D · dsh-science | GLM-5.3 | — | — | — | — | — | **93.3†** |
| E · workbuddy（auto） | GLM-5.2 | — | — | — | — | — | **53.0‡** |

**†** D 的 02 结果尚未产出，暂按 01 分数（93.3）计入，待实测后更新。

## Round 01（初始）— Tyson2004-v1

> 历史轮次（0–10 制），Harness / LLM 列为评测时未记录字段，以"待补录"标注。

| Rank | System | Harness | LLM | Type | Benchmark | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | Status | 复现报告 |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 🥇 1 | DSH 科研代理 | DSH (DeepSeek Harness) | 待补录 | Agent | Tyson2004-v1 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | baseline | [报告](../benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | 待补录 | Agent | Tyson2004-v1 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | baseline | [报告](../benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

## 解读

**Round 03**

- **R02 的 93.3† 占位关闭，C 确认榜首**：D 的 02（Auton 2015）首次实测得 92，综合 **92.5（第 2）**，与 C（93）仅差 0.5——名次顺序在评审间方差（±3 分）内，不宜过度解读。R02"待实测后更新排名"的谨慎表述被证明是必要的。
- **推荐梯队（评审）：第一梯队 C ≈ A ≈ D**——C 工程型冠军（provenance/交叉验证最完整）、A 推理型冠军（数据沉积异常发现）、D 深度科研型冠军（Tyson 分析深度 + 1000G claim-level 全 PASS）；F 严谨但产品化略逊；B 工程证据链弱一档；E 任务完成合格但 Tyson 报告深度不足。勘误互换后分值顺序为 C 93 > D 92.5 > A 91（前三差距在评审方差内）> F 87 > B 84 > E 81.5。
- **证据闭环拉开差距**：高分组合的共同点是 `claim → 数据 → 代码 → 独立验证 → 局限` 闭环（C02 Fst 与 vcftools 逐位交叉验证 0.02388 / n=7,335；D02 记录 bug 修复后重跑）；"发现复现失败并如实报告"（B02 ARI 0.87、E02 ARI 0.872、F02 4/5 claim）被评审认定为高分行为。
- **最大共同问题——chr21 近似被表述为全基因组复现**：多数 1000G 报告以 chr21 支撑全基因组 / 26×26 claim；评审建议正式结论严格区分 "claim supported" 与 "paper-level exact reproduction"，这是本轮 1000G 单项无人满分的原因。
- **评审间方差 ±3 分**：同一提交在 R02/R03 两轮评审下项目分差 ±3 以内（C01 91.0→94、D01 93.3→93、A01 90.6→91、B01 84.4→82），唯 E01 例外（53.0→77，R03 评审未核查 binning 独立性）。单人评审下 1–2 分的名次差异不足以定性。

**Round 02**

- **Harness Effect ≈ +5 分**：A 与 B 同为 DeepSeek-V1-Flash，dsh-science（90.8）比 Claude Science（85.8）高 5.0 分，说明 benchmark 测到的主要是 Harness 结构差异。
- **同一 Harness 换模型仅 +1.0 分**：A → C（DeepSeek-V1-Flash → GLM-5.2），90.8 → 91.8；科研长任务中 Harness 的作用可能比模型本身更显著。
- **D（GLM-5.3）暂列综合第一（待 02 确认）**：在 Tyson 2004 单项目取得当前最高分 93.3；02（Auton 2015）结果未出，暂按 01 分数计入，综合总分暂定 93.3，待实测后更新。
- **E（workbuddy auto × GLM-5.2）53.0：一次"未成立"的复现**：与 C 同用 GLM-5.2，但 01 项目仅 53.0（vs C 的 91.0）。评审指出其核心问题不是报告质量，而是方法学层面——5 个 organism bins 直接取自 NCBI GenBank 既有 assignment 而非按论文方法独立 binning，使"重建 5 bins"成为循环论证；且 gene prediction 表中 3 个 bin 为 0 基因、后续代谢重建却给出大量功能基因命中，数据来源链断裂。这从反面说明：同一模型在不同 Harness/运行模式下，科研可信度可以出现断崖式差距。

**Round 01**

- DSH 的主要优势来自 D3：完整的数据→环境→pipeline→结果→artifact 闭环。
- Claude Science 的主要优势在 D2：科学内容理解、证据辨析和对不可复现结论的边界识别。

## 注意

本榜单不是模型能力总榜，也不是通用 intelligence 排名。

它评价的是：

> 在指定科研任务、指定规则和指定证据要求下，一个 Harness/Agent/LLM/Skill 完成可靠科研工作的能力。

## 更新记录

- **R08（2026-09-03）**：两份 **Tyson 2004 AMD 复现报告**的 GPT-5.6-sol 五维评测（**作为 01 Tyson 单论文报告排名入档**）——① phylo-biomni-standard 的 `tyson2004_reproduction.html`（Biomni 标准，**真实端到端复现**：原始 Sanger reads → 重组装 → 分箱 → 注释 → SNP）**52.5**（Major Revision；D1=8/D5=7 最高，但 **7 张图全部 broken** 致 D4=3，且单一 nifH 命中被过度升为"可能改写固氮分工"，bin 大小/ORF 明显偏小却未标"未复现"）；② dcsCloud 的 `Tyson2004_Reproduction.html`（DCS Cloud/Genpilot）**41.5**（Major Revision；**非端到端复现**，基于论文已发布重构基因组再注释，碳固定"未检出"与论文不符、nif 归因偷换、图 5.1 同轴/5.3 论文数据重绘当复现、e-value 误当"复现成功的统计显著"）。①为端到端尝试、②为成品再分析，两者深度不对等；均非双项目答卷，不入综合榜。已与 R07 的 Rosalind（67.5）排入 leaderboard 顶部「01｜Tyson 2004 复现报告单论文排名（GPT-5.6-sol）」，三者分值：Rosalind 67.5 > Biomni 52.5 > dcsCloud 41.5。记录见 [evaluations/round-08-biomni-dcscloud.md](../evaluations/round-08-biomni-dcscloud.md)。
- **R07（2026-09-02）**：两份**异构文档**的 GPT-5.6-sol 五维评测（**①为 01 Tyson 复现报告、排入单论文榜；②为评审文档、仅留存**）——① ChatGPT-Rosalind-5.6Sol 的 `tyson2004_reproduction.html`（Tyson 2004 复现报告）**67.5**（Major Revision；部分复现成功，D2=8 逻辑严密，但 SNP/重组/FISH/ORF/代谢仅原文复核、工程复现与证据定位不足）；② GPT-5.6 对 workbuddy E01 的评审稿 `Review_E01_不建议判定为“论文复现成功”.md` **53.5**（Major Revision；抓住循环验证/来源链断裂/指标错配三处硬伤，但被评稿自身 56 vs 53 口径矛盾、按整数分重算 53.5）。①为复现报告、②为评审文档，非同类型对象，分值不可互比。记录见 [evaluations/round-07-gpt5.6-sol-rosalind-e01review.md](../evaluations/round-07-gpt5.6-sol-rosalind-e01review.md)。
- **R05（2026-09-02）**：GLM-5.3-Flash 补测 case 02（Auton 2015 / 1000 Genomes Phase 3）并以 **GPT-5.6-sol 双样本评审（72.20 / 72.80 → 官方 72.5）**，综合分 **（43.25 + 72.5）/ 2 = 57.9** 正式并入综合榜（第 7 位，带口径警告——其分数为 GPT-5.6-sol 全代码口径，与 R03 六组合的评审口径不可直接互比）。复现本身：headless 一次性任务、0 人工介入、2 h 34 min；9 claims 自评 8 PASS + 1 PARTIAL，judge 严格口径为 C01 reproduced / C03 partial / C02、C05 unverifiable（Supp Table 1 逐染色体计数表确实不存在——对 benchmark 的引用勘误发现）/ C04 not_reproduced（ARI 0.8742<0.9，no-AMR 4 群 0.9898）。记录见 [evaluations/round-05-glm-5.3-flash-case02.md](../evaluations/round-05-glm-5.3-flash-case02.md)。
- **R04（2026-09-02）**：GLM-5.3-Flash（dsh-science × GLM-5.3-Flash）单系统 × 3 篇复现报告的 GPT-5.6-sol 审稿式评测——**Tyson 2004 = 43.25⚠️ / Love 2014 (DESeq2) = 52.0⚠️ / Zeisel 2015 = 51.5⚠️**，均 Major Revision。因缺 Auton/1000G（case 02）**不入综合排名**；judge 对"参照 bins 支撑结论"判定为输入违规（Tyson 由此从同侪的 93 骤降至 43），与 R03 dsh-science×GLM-5.3（也用 NCBI 参照 bins，得 93）不一致，需人工复核；Love 两次采样 55.8/52.0 显示评审方差，建议第二评审。评审记录见 [evaluations/round-04-glm-5.3-flash.md](../evaluations/round-04-glm-5.3-flash.md)，三份评审全文见 `evaluations/gpt5.6-review-glm5.3flash-*.md`。（**R05 后续**：case 02 已补测并入综合榜，见 R05 条目。）
- **R03（最新，2026-08-17）**：六系统双项目复评入榜——外部评审 12 份报告（A–F × 2 论文，0–10 制 ×10 换算；**入库时勘误：评审原文 D02/E02 标注互换，已按正确归属调换**，D02=92 / E02=86）：**C·dsh-science×GLM-5.2 综合 93 第一**，D·dsh-science×GLM-5.3 **92.5** 第二（02 首次实测 92，R02 的 93.3† 占位关闭），A **91** 第三，新增组合 F（dsh-science × kimi k3）**87** 第四，B **84** 第五，E·workbuddy **81.5⚠️** 第六（E01 与 R02 GPT-5.6 审稿的 53.0 Major Revision 结论冲突，同一提交两轮分差 24 分，待第三方裁决）。评审全文见 [evaluations/round-03-A-F.md](../evaluations/round-03-A-F.md)（顶部附勘误说明），评测记录见 [evaluations/round-03-six-system-combined.md](../evaluations/round-03-six-system-combined.md)。
- **R02 增补（2026-08-16）**：收录 workbuddy（auto 模式）× GLM-5.2 的 01（Tyson 2004）评审——GPT-5.6 审稿，五维加权 **53.0 / 100**，结论 Major Revision / 复现未成立，暂列综合榜第 5（02 未测）。评审全文见 [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](../benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)，评测记录见 [evaluations/round-02-workbuddy-auto-glm5.2.md](../evaluations/round-02-workbuddy-auto-glm5.2.md)。
- **R02（最新）**：双项目综合评测（Tyson2004-v1 + Auton2015），评分口径固定为 0–100 制五维加权；D·dsh-science×GLM-5.3 **93.3†** 暂列综合第一（02 未出、暂按 01 计入，待实测更新），C·dsh-science×GLM-5.2 **91.8** 第二，A·dsh-science×DeepSeek-V1-Flash **90.8** 第三，B·Claude Science **85.8** 第四。完整审稿记录见 [benchmarks/Review/260816 bench.txt](../benchmarks/Review/260816%20bench.txt)，评测记录见 [evaluations/round-02-two-project-combined.md](../evaluations/round-02-two-project-combined.md)。
- **v0.1（初始）**：Tyson2004-v1，DSH 科研代理 9.10 vs Claude Science 8.00；新增 Harness/LLM 版本列（待补录）。
- 多组学 case（humangenomics / love2014 / zeisel2015）已发布为考题，评测完成后按同一 rubric 追加。
