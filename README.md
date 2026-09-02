# 科研场景 Harness 能力评价（Research Harness Benchmark）

> 🌐 **语言切换 / Language：** [**English**](README-en.md) ｜ 中文

一个面向 **Agent / LLM / Skill / Harness** 的科研能力公开评价框架。

目标不是评“谁聊天更聪明”，而是评价一个系统能否在真实科研任务中完成：

> 文献理解 → 数据获取 → 实验设计 → 代码执行 → 结果验证 → 科学论证 → 可复现交付

本仓库提供：
- 五维科研能力评价体系
- 科研可信度加权评分
- Benchmark case 标准模板
- Tyson et al. (2004) 复现案例
- Agent / LLM / Skill 的排行榜数据格式
- 审稿式评分模板
- 可扩展的自动评分脚本

## 五维评价体系

| 维度 | 含义 | 科研可信度权重 |
|---|---|---:|
| D1 | 文献检索与获取 | 15% |
| D2 | 内容理解与逻辑推理 | 30% |
| D3 | 代码生成与复现规范 | 25% |
| D4 | 实验设计与结果可视化 | 20% |
| D5 | 研究过程与效率 | 10% |

### 科研加权分

`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`

评分制：初始轮（R01）采用 0–10 分；R02 起统一为 0–100 分（五维权重不变，评分口径已固定；R03 入库时将 0–10 制评审分 ×10 换算）。

## 评测轮次

### Round 03（最新）— 六系统双项目复评（A–F × 2 论文）

> **评分口径**：与 R02 相同的五维加权（0–100 制）。本轮为外部评审对 **12 份复现报告**（6 组合 × 2 论文）的逐份审稿式复评；评审原文按 0–10 制打分，入库时 ×10 换算，综合总分取评审综合分（D/E 因 D02/E02 勘误互换按两项目平均重算，按固定公式复算值见评测记录）。
> **组合编号沿用 R02**：A–E 身份经报告内容核对沿用；**F 为新增组合（dsh-science × kimi k3，身份已补录）**。**D 的 02（Auton 2015）在本轮首次实测**——R02 的 93.3† 暂定值由此关闭。
> **勘误（2026-08-17）**：评审原文将 D02 与 E02 标注互换（ARI 0.9106 / vcftools 逐位一致的报告实为 D02、ARI 0.872 的报告实为 E02），入库时已按正确归属调换：D02=92 / E02=86，D/E 综合分随之重算（92.5 / 81.5）。

#### 正式综合排行榜（R03 六组合 + R05 并入的 GLM-5.3-Flash）

| Rank | 组合 | Harness | LLM | 总分 /100 | 项目分 | 综合评价 |
|---|---|---|---|---:|---|---|
| 🥇 **1** | **C** | dsh-science | GLM-5.2 | **93** | 01 **94** / 02 **92** | **最均衡，科研复现工程化程度最高**：provenance 链、oracle 式交叉验证（Fst 与 vcftools 逐位一致 0.02388 / n=7,335）、环境锁定与单机重跑说明 |
| 🥈 **2** | **D** | dsh-science | GLM-5.3 | **92.5** | 01 **93** / 02 **92** | **两个项目都强**：Tyson（H1–H4→E01–E04 结构、nif 归属科学修正）+ 1000G claim-level 全 PASS（ARI 0.9106、WC84 Fst 与 vcftools 逐位一致）；02 为首次实测 |
| 🥉 **3** | **A** | dsh-science | DeepSeek-V1-Flash | **91** | 01 **91** / 02 **91** | **科学推理强**：发现 GenBank 沉积组装与论文不一致并独立重组装；方法学差异披露与结果验证充分 |
| 4 | **F** | dsh-science | kimi k3 | **87** | 01 **83** / 02 **90** | **逻辑严谨、复现意识强**：未获全文 / canu→miniasm 等边界如实披露；显式环境锁定、自实现 WC84 Fst、下载截断校验重试；4/5 claim 支持 |
| 5 | **B** | Claude Science | DeepSeek-V1-Flash | **84** | 01 **82** / 02 **86** | 研究判断不错，但工程化明显落后 |
| 6 | **E** | workbuddy（auto） | GLM-5.2 | **81.5**⚠️ | 01 **77** / 02 **86** | 01 报告"仪表盘化"、深度不足；02 好于 01（C4 ARI 0.872 未达 0.9 阈值但如实报告）；⚠️ 与 R02 评审结论冲突，名次暂定（见下） |
| 7⚠️ | **GLM-5.3-Flash** | dsh-science | GLM-5.3-Flash | **57.9**⚠️ | 01 **43.25** / 02 **72.5** | **GPT-5.6-sol 口径**（01=R04 单样本、02=R05 双样本均值），与 R03 评审口径不可直接互比：Supp Table 1 勘误发现 + Fst 双实现逐位一致 + 全代码 D3 7.6 为真亮点；01 参照 bins 违规与 claim 判据替换为主要失分 |

> ⚠️ **口径警告**：第 7 行 GLM-5.3-Flash 的两个项目分均出自 GPT-5.6-sol 评审（R04/R05），R03 六组合出自 R03 外部评审——R03 口径明显更宽（参照 bins 等问题未扣分：同家族 dsh-science×GLM-5.3 的 Tyson 93 vs GPT-5.6-sol 对方法类似的 GLM-5.3-Flash 判 43.25）。分值排序仅供展示，严格同台需以 GPT-5.6-sol 全代码口径复评 R03 六组合。

**⚠️ E01 评审冲突**：R03 评审给出 E01 = 77，其关键数值（2,731 scaffolds / 16.5 Mb / 5 bins / 18,214 genes）与 R02 收录的 workbuddy 同一提交完全一致；而 R02 的 GPT-5.6 审稿判定该提交 **53.0 / Major Revision（复现未成立）**（binning 直接采用 NCBI 既有 assignment、数据来源链断裂）。R03 评审未涉及上述问题，两轮对同一提交结论冲突（分差 24 分），E 的分数与名次待第三方评审 / clean-room 核验裁决；本榜暂按 R03 评审收录，R02 结论保留在案。

#### 总分天梯图

```text
科研 Harness Leaderboard（R03 六组合 + R05 并入 GLM-5.3-Flash · 综合总分 /100）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C  dsh-science × GLM-5.2
██████████████████████████████████████  93
        ↑ 综合 Rank #1（工程型冠军：provenance + 交叉验证最完整）

D  dsh-science × GLM-5.3
██████████████████████████████████████  92.5
        ↑ 综合 Rank #2（02 首次实测 92；与 C 仅差 0.5，在评审方差 ±3 内）

A  dsh-science × DeepSeek-V1-Flash
█████████████████████████████████████  91
        ↑ 综合 Rank #3（推理型冠军：数据沉积异常发现）

F  dsh-science × kimi k3
██████████████████████████████████  87
        ↑ 综合 Rank #4（严谨：边界披露 + 工程规范）

B  Claude Science × DeepSeek-V1-Flash
████████████████████████████████  84
        ↑ 综合 Rank #5（科学判断好，工程化弱一档）

E  workbuddy（auto）× GLM-5.2
██████████████████████████████  81.5⚠️
        ↑ ⚠️ 与 R02 Major Revision 结论冲突，名次暂定

G  dsh-science × GLM-5.3-Flash
████████████████████████  57.9⚠️
        ↑ ⚠️ GPT-5.6-sol 口径（01 43.25 / 02 72.5），与 R03 评审口径不可直接互比；Supp Table 1
          勘误发现 + Fst 双实现逐位一致为亮点，01 参照 bins 违规与判据替换为主要失分

  50        60        70        80        90        100
```

#### 分项目成绩

**01｜Tyson 2004**

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **C** | dsh-science | GLM-5.2 | **95** | **96** | **97** | 93 | **88** | **94** |
| **D** | dsh-science | GLM-5.3 | 94 | **96** | 95 | **94** | **88** | **93** |
| **A** | dsh-science | DeepSeek-V1-Flash | 90 | 94 | 92 | 90 | 87 | **91** |
| **F** | dsh-science | kimi k3 | 80 | 87 | 84 | 82 | 80 | **83** |
| **B** | Claude Science | DeepSeek-V1-Flash | 80 | 87 | 81 | 82 | 80 | **82** |
| **E** | workbuddy（auto） | GLM-5.2 | 75 | 82 | 75 | 78 | 76 | **77⚠️** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| 组合 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **C** | dsh-science | GLM-5.2 | 90 | **94** | **96** | **92** | **88** | **92** |
| **D** | dsh-science | GLM-5.3 | **91** | **94** | **96** | **92** | 87 | **92** |
| **A** | dsh-science | DeepSeek-V1-Flash | 90 | **94** | 94 | 90 | 87 | **91** |
| **F** | dsh-science | kimi k3 | 90 | 93 | 92 | 91 | 85 | **90** |
| **B** | Claude Science | DeepSeek-V1-Flash | 87 | 89 | 88 | 86 | 80 | **86** |
| **E** | workbuddy（auto） | GLM-5.2 | 82 | 90 | 89 | 88 | 80 | **86** |

#### 本轮关键结论

- **R02 的 93.3† 占位关闭，C 确认榜首**：D 的 02 首次实测 92 → 综合 **92.5（第 2）**，与 C（93）仅差 0.5——名次顺序在评审间方差（±3 分）内，不宜过度解读。R02 "待实测后更新排名"的谨慎表述被证明是必要的。
- **证据闭环拉开差距**：高分组合的共同点是 `论文 claim → 原始数据 → 代码 → 独立验证 → 结论 → 局限` 的闭环（C02 以 vcftools 做逐位交叉验证；D02 记录 bug 修复后重跑）——"会不会写报告"不是分水岭，能否建立证据闭环才是。
- **发现复现失败是高分行为**：B02 ARI 0.87 未强行标 PASS、E02 ARI 0.872 如实报告并解释 AMR 原因、F02 4/5 claim 支持、F01 未获取全文/未复现部分如实标记、A01 披露 ~2 倍方法学差异、D01 指出 nif 归属后续被修正——与本项目 "Failure is evidence" 原则一致。
- **最大共同问题——chr21 近似被表述为全基因组复现**：多数 1000G 报告以 chr21 支撑 C4 PCA / burden / Fst / 部分 variant count，对应论文是全基因组 / 26×26 分析；评审建议严格区分 **"claim supported"** 与 **"paper-level exact reproduction"**（这也是本轮 1000G 单项无人满分的原因），R04 拟将该区分写入 rubric。
- **推荐梯队（评审）：第一梯队 C ≈ A ≈ D**（C 工程型冠军 / A 推理型冠军 / D 深度科研型冠军），第二梯队 F、第三梯队 B、第四梯队 E；勘误互换后分值顺序为 **C 93 > D 92.5 > A 91**（前三差距均在评审方差 ±3 内）> F 87 > B 84 > E 81.5。
- **评审间方差 ±3 分**：同一提交两轮评审项目分差 ±3 以内（C01 91.0→94、D01 93.3→93、A01 90.6→91、B01 84.4→82），唯 E01 例外（53.0→77）——单人评审下 1–2 分的名次差异不足以定性，高分段需第二评审。

#### 细节报告入口

| 内容 | 入口 |
|---|---|
| R03 评审全文（12 份报告逐一评分、横向发现与推荐梯队） | [evaluations/round-03-A-F.md](evaluations/round-03-A-F.md) |
| Round 03 评测记录（结构化、含组合身份核对与跨轮次核对） | [evaluations/round-03-six-system-combined.md](evaluations/round-03-six-system-combined.md) |
| Round 05 评测记录（GLM-5.3-Flash case 02 补测 + 评审 + 并入综合榜） | [evaluations/round-05-glm-5.3-flash-case02.md](evaluations/round-05-glm-5.3-flash-case02.md) |
| Round 05 评审全文（GPT-5.6-sol 双样本） | [evaluations/gpt5.6-review-glm5.3flash-case02.md](evaluations/gpt5.6-review-glm5.3flash-case02.md) |
| 完整榜单与更新记录 | [docs/leaderboard.md](docs/leaderboard.md) |
| Case 详情：Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case 详情：1000 Genomes Phase 3（Auton 2015） | [benchmarks/humangenomics/](benchmarks/humangenomics/) |
| dsh-science 插件（执行评测的 Harness 插件） | <https://github.com/biociao/dsh-science> |

> **欢迎参与评测**：欢迎用你的 LLM（Claude、GPT 等）× Harness 工具复现上述题目，将报告提交到本仓库，一起参与评测比较，提供更全面的参考。

### Round 05（最新）— GLM-5.3-Flash 补测 case 02 并入综合榜

> **R04 缺口已关闭**：dsh-science × GLM-5.3-Flash 以 headless 一次性任务补做 **Auton 2015 / 1000 Genomes Phase 3（chr21）**独立复现——**0 人工介入、2 h 34 min**、7 工件 97 文件 SHA-256 全部校验通过。GPT-5.6-sol **双独立样本**评审：**72.20 / 72.80（方差 0.6）→ 官方采用 72.5**（Major Revision，证据等级 E2；本次为全代码口径，D3 回升至 7.6，证实 R04「D3 受截断影响」判断）。
>
> **judge 严格口径 vs 答卷自评**：答卷自评 9 claims = 8 PASS + 1 PARTIAL；judge 判 C01 reproduced / C03 partially_reproduced / **C02、C05 unverifiable**（答卷发现的「论文逐染色体计数表从未发布」勘误成立，但替代判据不等价于原 ±1 与 tolerance-band 对照）/ **C04 not_reproduced**（PCA ARI 0.8742 < 0.9；排除混合人群 AMR 后 4 群 ARI 0.9898 属诊断性证据）。无伪造迹象；主要问题是判据替换后过度报 PASS。
>
> **综合总分 =（01 Tyson 43.25 + 02 Auton 72.5）/ 2 = 57.9**，正式并入综合榜第 7 位（⚠️ 其两项目分均出自 GPT-5.6-sol，与 R03 六组合的评审口径不可直接互比，详见 [docs/leaderboard.md](docs/leaderboard.md) R05 节）。评测记录见 [evaluations/round-05-glm-5.3-flash-case02.md](evaluations/round-05-glm-5.3-flash-case02.md)，评审全文见 [evaluations/gpt5.6-review-glm5.3flash-case02.md](evaluations/gpt5.6-review-glm5.3flash-case02.md)。

### Round 04 — GLM-5.3-Flash × 3 篇复现（01 Tyson 部分；case 02 已于 R05 补测）

> 当时因缺 case 02 未入综合排名（**已于 R05 补测并入**）。GPT-5.6-sol 审稿式评分：**Tyson 2004 = 43.25⚠️ / Love 2014 (DESeq2) = 52.0⚠️ / Zeisel 2015 = 51.5⚠️**，均 Major Revision。关键发现：judge 将 Tyson「用 NCBI 参照 bins 支撑结论」判为输入违规，与 R03 的 dsh-science×GLM-5.3（Tyson 93，同样引用参照 bins）不一致，需人工复核；Love 两次采样 55.8/52.0 显示评审方差。评测记录见 [evaluations/round-04-glm-5.3-flash.md](evaluations/round-04-glm-5.3-flash.md)。

### Round 02 — 双项目综合评测（历史）

> 历史轮次，最新结果以上方 Round 03 为准。D 的 02 已在 R03 首次实测（92 → 综合 92.5），本节的 93.3† 暂定值与"暂列第一"状态已被 R03 结果取代。

> **评分口径（已固定）**：五维加权分 `总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`（0–100 制）。
> **综合总分 = 已完成 01、02 两项目的项目分平均值**；未完成项目暂按已完成项目分数占位计入（见 D 的 02），待实测后更新，排名为暂定。
>
> **Harness 说明**：榜单中的 **dsh-science**（早期记录写作 DSH / dsh）是运行于 DeepSeek Harness 之上的科研场景插件，负责执行本仓库的评测任务；源码与文档见 <https://github.com/biociao/dsh-science>。R02 起统一使用 dsh-science 表述，历史轮次（R01）保留原始记录。

本轮包含两个经典论文复现项目：

| 项目 | 论文 | 科研任务核心 |
|---|---|---|
| **01** | [Tyson et al. 2004, *Nature*](benchmarks/tyson2004/) | AMD 环境宏基因组：微生物基因组重构、分箱、代谢与群体变异 |
| **02** | [Auton et al. 2015, *Nature*](benchmarks/humangenomics/) | 1000 Genomes Phase 3 人群遗传学核心论断独立复现（VCF 计算 / PCA / Fst） |

#### 正式综合排行榜（R02）

| Rank | Harness | LLM | 总分 /100 | 项目分 | 综合评价 |
|---|---|---:|---|---|---|
| 🥇 **1** | **dsh-science** | **GLM-5.3** | **93.3†** | 01 **93.3** /02 **93.3†** | **暂列第一**；01 表现突出，02 结果未出、暂按 01 分数计入 |
| 🥈 **2** | **dsh-science** | **GLM-5.2** | **91.8** | 01 **91.0** / 02 **92.5** | 科研复现工程最完整；claim-level 验证、交叉工具、环境锁定、artifact/provenance 最成熟 |
| 🥉 **3** | **dsh-science** | **DeepSeek-V1-Flash** | **90.8** | 01 **90.6** / 02 **91.0** | 综合科研能力很强；两个领域任务都稳定，方法学差异披露尤其好 |
| 4 | **Claude Science** | **DeepSeek-V1-Flash** | **85.8** | 01 **84.4** / 02 **87.1** | 科研分析不错，但 Harness 工程化弱一档 |
| 5 | **workbuddy（auto 模式）** | **GLM-5.2** | **53.0‡** | 01 **53.0** / 02 未测 | ⚠️ **复现未成立（Major Revision）**：核心 binning 直接采用 NCBI 既有 assignment，复现 claim 不成立 |

**†** D 的 02（Auton 2015）结果尚未产出，暂按 01 分数（93.3）计入；综合总分 93.3 为**暂定值**，待 02 实测后更新，届时排名可能变动。

**‡** E（workbuddy auto × GLM-5.2）仅完成 01（Tyson 2004），GPT-5.6 审稿结论为 **Major Revision / 复现未成立**（53.0/100；标题曾写 56，按评审自身 rubric 复算为 53.0）。评审认为关键问题修复前不应进入正式排名，此处收录并明确标注状态。评审全文见 [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md)。

#### 总分天梯图

```text
科研 Harness Leaderboard（R02 · 综合总分 /100）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

D  dsh-science × GLM-5.3
█████████████████████████████████████████████  93.3†
        ↑ 暂列综合 Rank #1（02 未出，暂按 01 计）

C  dsh-science × GLM-5.2
████████████████████████████████████████████  91.8
        ↑ 综合 Rank #2

A  dsh-science × DeepSeek-V1-Flash
███████████████████████████████████████████  90.8
        ↑ 综合 Rank #3

B  Claude Science × DeepSeek-V1-Flash
█████████████████████████████████████████  85.8
        ↑ 综合 Rank #4

E  workbuddy（auto）× GLM-5.2
█████  53.0‡
        ↑ ⚠️ 复现未成立（Major Revision），暂列榜末

  50        60        70        80        90        100
```

#### 分项目成绩

**01｜Tyson 2004**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| **C · dsh-science** | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| **A · dsh-science** | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| **B · Claude Science** | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| **D · dsh-science** | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |
| **E · workbuddy（auto）** | GLM-5.2 | 70 | 55 | 40 | 55 | 50 | **53.0‡** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| **C · dsh-science** | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| **A · dsh-science** | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| **B · Claude Science** | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| **D · dsh-science** | GLM-5.3 | — | — | — | — | — | **93.3†** |
| **E · workbuddy（auto）** | GLM-5.2 | — | — | — | — | — | **53.0‡** |

**†** D 的 02 结果尚未产出，暂按 01 分数（93.3）计入，待实测后更新。

#### 本轮关键结论

- **Harness Effect ≈ +5 分**：A 与 B 使用同一 LLM（DeepSeek-V1-Flash），dsh-science（90.8）比 Claude Science（85.8）高 **5.0 分**——当前 benchmark 测到的是 Harness 结构差异，而非单纯 LLM 差异。
- **同一 Harness 换更强模型只提升 1.0 分**：A → C（dsh-science 上 DeepSeek-V1-Flash → GLM-5.2），90.8 → 91.8。提示在科研长任务中，Harness 的作用可能比单纯换模型更显著。
- **GLM-5.3 暂列综合第一（待 02 确认）**：D01 = 93.3 表现突出；02（Auton 2015）结果未出，暂按 01 分数计入，综合总分暂定 **93.3**。此为暂定排名——在 02 实测前，尚不能把「GLM-5.3 一定综合第一」当作定论。
- **同模型不同 Harness 可差 38 分（反面证据）**：E（workbuddy auto × GLM-5.2）与 C 同用 GLM-5.2，01 项目却仅 **53.0**（vs C 的 91.0）——其核心 binning 直接取自 NCBI 既有 organism assignment 而非按论文方法独立复现，且 gene prediction 与代谢重建之间存在数据来源链断裂。同一模型在不同 Harness/运行模式下，科研可信度可出现断崖式差距。

#### 细节报告入口

| 内容 | 入口 |
|---|---|
| 完整审稿式评测（评分依据、claim 级证据、方法学披露、排行榜） | [benchmarks/Review/260816 bench.txt](benchmarks/Review/260816%20bench.txt) |
| Round 02 评测记录（结构化） | [evaluations/round-02-two-project-combined.md](evaluations/round-02-two-project-combined.md) |
| Round 02 增补：workbuddy auto × GLM-5.2 评测记录（01） | [evaluations/round-02-workbuddy-auto-glm5.2.md](evaluations/round-02-workbuddy-auto-glm5.2.md) |
| workbuddy auto × GLM-5.2 的 01 评审全文（GPT-5.6 审稿，53.0/100，Major Revision） | [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md) |
| 完整榜单与更新记录 | [docs/leaderboard.md](docs/leaderboard.md) |
| Case 详情：Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case 详情：1000 Genomes Phase 3（Auton 2015） | [benchmarks/humangenomics/](benchmarks/humangenomics/) |
| dsh-science 插件（执行评测的 Harness 插件） | <https://github.com/biociao/dsh-science> |

> **欢迎参与评测**：欢迎用你的 LLM（Claude、GPT 等）× Harness 工具复现上述题目，将报告提交到本仓库，一起参与评测比较，提供更全面的参考。

### Round 01（初始基准）— Tyson2004-v1

> 历史轮次，最新结果请以上方 Round 03 为准。

任务：对 Tyson et al. 2004 的环境微生物组/基因组重建工作进行独立计算复现。

| Rank | System | Harness | LLM | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | 复现报告 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 🥇 1 | DSH 科研代理 | DSH (DeepSeek Harness) | 待补录 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | [报告](benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | 待补录 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | [报告](benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

> 加权分公式：`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`（`scripts/score.py` 计算；Claude Science 精确值为 7.99，按 8.00 展示；R01 为 0–10 制）。
>
> 这是本仓库初始化时的案例基准，不代表永久排名。后续所有新系统应使用同一 case、同一 rubric、同一证据要求重新评测，并将复现报告提交至 `benchmarks/<case>/reports/`。
>
> 完整榜单（含更新记录）见 [docs/leaderboard.md](docs/leaderboard.md)；每期评测评价见 [evaluations/](evaluations/)。

## 贡献测评结果（Contributing）

欢迎用你的 LLM（Claude、GPT 等）× Harness 工具复现上述题目（或 [benchmarks/](benchmarks/) 下任一 case），把测评结果提交到本仓库，一起参与横向比较。**只有遵循同一评分口径、同一 benchmark version 的结果才能进入排行榜。**

**提交内容**（详见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [docs/benchmark-protocol.md](docs/benchmark-protocol.md)）：

| 项 | 要求 |
|---|---|
| 系统信息 | system 名称 / 版本 / 类型（Harness / LLM / Skill） |
| 基准版本 | 使用的 benchmark version（如 Tyson2004-v1、Auton2015-v1）；**不同版本不可直接比较** |
| 五维原始分数 | D1–D5 原始分（R02 起 0–100 制，按上方加权公式计算） |
| Claim 级证据 | 每个 claim 的状态（`reproduced / partially / not_reproduced / contradicted`）与证据路径 |
| 可复现交付 | 代码 / 环境锁定 / 执行日志 / 结果 artifact / provenance（复现等级 R0–R4） |
| 评审信息 | reviewer 身份与日期；9 分以上建议第二位 reviewer 或 clean-room verification |

**提交流程**：

1. 复现报告与证据放入 `benchmarks/<case>/reports/`；
2. 在 [evaluations/](evaluations/) 新建一轮评测记录（Round 编号递增）；
3. 将成绩追加到 [docs/leaderboard.md](docs/leaderboard.md)（附 reviewer scorecard 以便回溯）。

**禁止**：
- 用不同 benchmark version 直接比较；
- 没有执行证据却宣称复现；
- 删除失败实验记录（failure is evidence）；
- 用宣传材料代替可核查证据。

评分标准见 [docs/rubric.md](docs/rubric.md)；提交协议见 [docs/benchmark-protocol.md](docs/benchmark-protocol.md)；完整贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 核心原则

1. **Claim-first**：先定义要验证的科学论断，再评价 Agent。
2. **Evidence-first**：评分必须绑定证据，而不是只看最终报告。
3. **Execution matters**：代码是否真正执行、结果是否来自执行，是核心指标。
4. **Reproducibility is graded**：复现不是二元变量，而是连续等级。
5. **Failure is evidence**：明确识别不可复现部分不会扣“科学诚信分”，隐瞒失败反而应扣分。
6. **Independent verification**：高分结果应支持第三方 clean-environment rerun。
7. **Versioned benchmark**：Benchmark、数据、评分规则和排行榜均版本化。

## 推荐评级

| 分数 | 等级 | 含义 |
|---:|---|---|
| 9.0–10.0 | Excellent | 接近独立科研执行/审计级 |
| 8.0–8.9 | Strong | 高质量科研助手/Agent |
| 7.0–7.9 | Good | 可完成多数科研分析，但闭环存在缺口 |
| 6.0–6.9 | Developing | 有明显科研执行短板 |
| <6.0 | Weak | 不适合作为可靠科研执行系统 |

## 为什么强调可复现

计算科研的可信度不能只靠“报告写得好”。Nature Methods 对计算可复现性提出从 Bronze/Silver/Gold 的渐进标准；Gold 标准要求整个分析能够自动化执行。citeturn0search0

本项目因此把代码、依赖、环境、数据 provenance、执行日志、结果工件和第三方验证纳入评价。

## Roadmap

- [x] 五维评分体系
- [x] Tyson 2004 初始 benchmark
- [x] 科研可信度加权排行榜
- [x] 第二个生命科学 benchmark（多组学：人基因组学 [humangenomics](benchmarks/humangenomics/) + 转录组学 [love2014](benchmarks/love2014/) + 单细胞 [zeisel2015](benchmarks/zeisel2015/)）
- [x] 第二轮双项目综合评测（R02：Tyson2004 + 1000 Genomes Phase 3，A/B/C/D 四系统横向对比，0–100 制评分口径固定）
- [x] 第三轮六系统双项目复评（R03：A–F × 2 论文共 12 份报告；D/E 的 02 首次实测，新增组合 F；关闭 R02 暂定排名并标记 E01 评审冲突；入库时勘误 D02/E02 标注互换）
- [ ] 化学/材料 benchmark
- [ ] 临床文献与数据分析 benchmark
- [ ] Agent / LLM / Skill 三类统一提交格式
- [ ] 自动 artifact validator
- [ ] clean-room reproduction
- [ ] GitHub Pages 排行榜
- [ ] benchmark versioning + leaderboard history

## License

建议 MIT；具体 benchmark 数据和论文衍生材料应分别遵守其原始许可证与版权要求。
