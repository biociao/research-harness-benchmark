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

## 统一排行榜

> 榜单口径：**五维加权** `总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`（R02 起 0–100 制；R01 为 0–10 制，已折算展示）。**综合总分** = 已成「01 Tyson + 02 Auton」双项目的项目分平均值；**单论文分** 为仅评 01 Tyson 的独立复现报告。各主体分数同列于一张榜，**用「评审口径」列区分**不同评审/轮次（R03 外部评审 / GPT-5.6-sol），附注注明口径差异、冲突与勘误。
>
> **⚠️ 口径须知**：同一主体在不同评审/轮次下的分数**不可直接互比**（R03 外部评审明显更宽松：同家族 dsh-science×GLM-5.3 的 Tyson 得 93，而 GPT-5.6-sol 对方法类似的 GLM-5.3-Flash 判 43.25，分差 ~50）。本榜按分值排序仅供排名展示，名次解读须结合「评审口径」列。**严格同台需以 GPT-5.6-sol 全代码口径复评 R03 六组合**（后续工作）。

### 总榜（全主体，按分值降序）

| Rank | 主体 | Harness / 实现 | LLM | 总分 /100 | 01 分 | 02 分 | 评审口径 | 综合评价 |
|:--:|---|---|---|:--:|:--:|:--:|---|---|
| 🥇 1 | **C** · dsh-science | dsh-science | GLM-5.2 | **93** | 94 | 92 | R03 外部评审 | 最均衡，科研复现工程化程度最高：provenance 链、oracle 式交叉验证（Fst 与 vcftools 逐位一致 0.02388 / n=7,335）、环境锁定与单机重跑说明 |
| 🥈 2 | **D** · dsh-science | dsh-science | GLM-5.3 | **92.5** | 93 | 92 | R03 外部评审 | 两个项目都强：Tyson（H1–H4→E01–E04 结构、nif 归属科学修正）+ 1000G claim-level 全 PASS（ARI 0.9106、WC84 Fst 与 vcftools 逐位一致）；02 为首次实测 |
| 🥉 3 | **A** · dsh-science | dsh-science | DeepSeek-V1-Flash | **91** | 91 | 91 | R03 外部评审 | 科学推理强：发现 GenBank 沉积组装与论文不一致并独立重组装；方法学差异披露与结果验证充分 |
| 4 | **F** · dsh-science | dsh-science | kimi k3 | **87** | 83 | 90 | R03 外部评审 | 逻辑严谨、复现意识强：未获全文 / canu→miniasm 等边界如实披露；显式环境锁定、自实现 WC84 Fst、下载截断校验重试；4/5 claim 支持 |
| 5 | **B** · Claude Science | Claude Science | DeepSeek-V1-Flash | **84** | 82 | 86 | R03 外部评审 | 研究判断不错，但工程化明显落后 |
| 6 | **E** · workbuddy（auto） | workbuddy（auto 模式） | GLM-5.2 | **81.5**⚠️ | 77 | 86 | R03 外部评审 | 01 报告"仪表盘化"、深度不足；02 好于 01（C4 ARI 0.872 未达 0.9 阈值但如实报告）；⚠️ 与 R02 评审结论冲突，名次待第三方核验（见下） |
| — | **ChatGPT-Rosalind-5.6Sol** | ChatGPT-Rosalind-5.6Sol | — | **67.5** | **67.5** | — | GPT-5.6-sol（01 单论文） | 01 单论文复现报告：部分复现成功；D2=8 把握证据边界、深至 2004 contig 批次，但 SNP/重组/FISH/ORF/代谢仅原文复核 |
| 7⚠️ | **GLM-5.3-Flash** · dsh-science | dsh-science | GLM-5.3-Flash | **57.9**⚠️ | 43.25 | 72.5 | GPT-5.6-sol（R04/R05） | 唯一被 GPT-5.6-sol 完整评审双项目的系统；Supp Table 1 勘误发现 + Fst 双实现逐位一致 + 全代码 D3 7.6 为真亮点；01 参照 bins 违规与 claim 判据替换为主要失分 |
| — | **phylo-biomni-standard** | Biomni 标准 | — | **52.5** | **52.5** | — | GPT-5.6-sol（01 单论文） | 01 单论文复现报告：真实端到端复现尝试（原始 Sanger reads 起算，D1/D5 最高），但 7 图全 broken 致 D4=3，单一 nifH 命中过度升为机制结论 |
| — | **dcsCloud** | DCS Cloud / Genpilot | — | **41.5** | **41.5** | — | GPT-5.6-sol（01 单论文） | 01 单论文复现报告：非端到端（成品基因组再分析）；碳固定未检出与论文不符、nif 归因偷换、e-value 误当复现显著 |

> 📌 **榜单说明**：① 综合总分（含 01+02）与 01 单论文分（仅 Tyson）**不是同一种量纲**——综合分高的主体完成双项目、单论文分主体只评了 Tyson，故后四行仅作 01 维度的补充参考，不计入「综合排名」；但**全部列出**便于横向对照。② **E（workbuddy）评审冲突**：R03 评审给出 E01=77，其关键数值与 R02 收录的 workbuddy 同一提交一致，而 R02 的 GPT-5.6 审稿判该提交 **53.0 / Major Revision（复现未成立）**（binning 直接采用 NCBI 既有 assignment、来源链断裂），同一提交两轮分差 24 分，名次待第三方/clean-room 核验裁决。③ **GLM-5.3-Flash 口径警告**：其两项目分出自 GPT-5.6-sol，与 R03 六组合的评审口径不可直接互比（见上方口径须知）。

### 分项目

**01｜Tyson 2004（统一，含 R03 六组合 + GPT-5.6-sol 单论文，按 01 分降序）**

| 主体 | Harness / 实现 | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 01 分 | 评审口径 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| **C** · dsh-science | dsh-science | GLM-5.2 | **95** | **96** | **97** | 93 | **88** | **94** | R03 外部评审 |
| **D** · dsh-science | dsh-science | GLM-5.3 | 94 | **96** | 95 | **94** | **88** | **93** | R03 外部评审 |
| **A** · dsh-science | dsh-science | DeepSeek-V1-Flash | 90 | 94 | 92 | 90 | 87 | **91** | R03 外部评审 |
| **F** · dsh-science | dsh-science | kimi k3 | 80 | 87 | 84 | 82 | 80 | **83** | R03 外部评审 |
| **B** · Claude Science | Claude Science | DeepSeek-V1-Flash | 80 | 87 | 81 | 82 | 80 | **82** | R03 外部评审 |
| **ChatGPT-Rosalind-5.6Sol** | ChatGPT-Rosalind-5.6Sol | — | 7 | 8 | 6 | 6 | 6 | **67.5** | GPT-5.6-sol（单论文） |
| **phylo-biomni-standard** | Biomni 标准 | — | 8 | 5 | 5 | 3 | 7 | **52.5** | GPT-5.6-sol（单论文） |
| **GLM-5.3-Flash** · dsh-science | dsh-science | GLM-5.3-Flash | — | — | — | — | — | **43.25** | GPT-5.6-sol（R04） |
| **dcsCloud** | DCS Cloud / Genpilot | — | 5 | 3 | 4 | 5 | 5 | **41.5** | GPT-5.6-sol（单论文） |
| **E** · workbuddy（auto） | workbuddy（auto 模式） | GLM-5.2 | 75 | 82 | 75 | 78 | 76 | **77**⚠️ | R03 外部评审 |

> ⚠️ **口径分离**：R03 六组合出自外部评审、为双项目答卷；GPT-5.6-sol 三份（Rosalind/Biomni/dcsCloud）为单论文独立复现报告，两者**非同口径**，只并列不混排为一个名次表。若需统一口径排名，应以 GPT-5.6-sol 全代码口径复评 R03 六组合。

**02｜Auton 2015（1000 Genomes Phase 3，统一）**

| 主体 | Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 02 分 | 评审口径 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| **C** · dsh-science | dsh-science | GLM-5.2 | 90 | **94** | **96** | **92** | **88** | **92** | R03 外部评审 |
| **D** · dsh-science | dsh-science | GLM-5.3 | **91** | **94** | **96** | **92** | 87 | **92** | R03 外部评审 |
| **A** · dsh-science | dsh-science | DeepSeek-V1-Flash | 90 | **94** | 94 | 90 | 87 | **91** | R03 外部评审 |
| **F** · dsh-science | dsh-science | kimi k3 | 90 | 93 | 92 | 91 | 85 | **90** | R03 外部评审 |
| **B** · Claude Science | Claude Science | DeepSeek-V1-Flash | 87 | 89 | 88 | 86 | 80 | **86** | R03 外部评审 |
| **E** · workbuddy（auto） | workbuddy（auto 模式） | GLM-5.2 | 82 | 90 | 89 | 88 | 80 | **86** | R03 外部评审 |
| **GLM-5.3-Flash** · dsh-science | dsh-science | GLM-5.3-Flash | — | — | — | — | — | **72.5** | GPT-5.6-sol（R05 双样本均值） |

### 关键结论与横向解读

- **证据闭环拉开差距**：高分组合的共同点是 `论文 claim → 原始数据 → 代码 → 独立验证 → 结论 → 局限` 的闭环（C02 以 vcftools 做逐位交叉验证；D02 记录 bug 修复后重跑）——"会不会写报告"不是分水岭，能否建立证据闭环才是。
- **发现复现失败是高分行为**：B02 ARI 0.87 未强行标 PASS、E02 ARI 0.872 如实报告并解释 AMR 原因、F02 4/5 claim 支持、A01 披露 ~2 倍方法学差异、D01 指出 nif 归属后续被修正——与本项目 "Failure is evidence" 原则一致。
- **最大共同问题——chr21 近似被表述为全基因组复现**：多数 1000G 报告以 chr21 支撑 claim，对应论文是全基因组分析；评审建议严格区分 **"claim supported"** 与 **"paper-level exact reproduction"**（这也是 1000G 单项无人满分的原因）。
- **Harness Effect ≈ +5 分**（R02）：A 与 B 同用 DeepSeek-V1-Flash，dsh-science（90.8）比 Claude Science（85.8）高 5.0 分——benchmark 测到的主要是 Harness 结构差异；同一 Harness 换更强模型仅 +1.0 分（A→C），提示 Harness 作用可能大于单纯换模型。
- **同模型不同 Harness 可差 38 分（反面证据）**：E（workbuddy auto × GLM-5.2）与 C 同用 GLM-5.2，01 项目却仅 53.0（vs C 的 94）——核心 binning 直接取自 NCBI 既有 assignment 而非独立复现，且 gene prediction 与代谢重建存在来源链断裂。同一模型在不同 Harness/运行模式下，科研可信度可断崖式差距。
- **评审间方差 ±3 分**：同一提交两轮评审项目分差 ±3 以内（C01 91.0→94、D01 93.3→93、A01 90.6→91、B01 84.4→82），唯 E01 例外（53.0→77）——单人评审下 1–2 分名次差异不足以定性，高分段需第二评审。

### 历史轮次与初始基准

- **Round 01（初始基准，0–10 制，已折算）**：DSH 科研代理 **9.10** vs Claude Science **8.00**（Tyson2004-v1；0–10 制 ×10 折算为 91.0/80.0）。为初始化案例基准，不代表永久排名；后续新系统须用同一 case、同一 rubric、同一证据要求重评。报告见 [benchmarks/tyson2004/reports/](benchmarks/tyson2004/reports/)。
- **Round 02（双项目首评，历史）**：D·GLM-5.3 **93.3†**（02 未出暂按 01 计）、C·GLM-5.2 **91.8**、A·DeepSeek-V1-Flash **90.8**、B·Claude Science **85.8**、E·workbuddy **53.0‡**（复现未成立）。† 暂定值已被 R03 实测取代；‡ E01 结论与 R03 冲突，已在总榜标注。

### 细节报告入口

| 内容 | 入口 |
|---|---|
| R08 评测记录（Biomni 52.5 / dcsCloud 41.5，GPT-5.6-sol） | [evaluations/round-08-biomni-dcscloud.md](evaluations/round-08-biomni-dcscloud.md) |
| R07 评测记录（Rosalind 67.5 单论文 / E01 评审稿 53.5，GPT-5.6-sol） | [evaluations/round-07-gpt5.6-sol-rosalind-e01review.md](evaluations/round-07-gpt5.6-sol-rosalind-e01review.md) |
| R03 评审全文（12 份报告逐一评分、横向发现与推荐梯队） | [evaluations/round-03-A-F.md](evaluations/round-03-A-F.md) |
| Round 03 评测记录（结构化、含组合身份核对与跨轮次核对） | [evaluations/round-03-six-system-combined.md](evaluations/round-03-six-system-combined.md) |
| Round 05 评测记录（GLM-5.3-Flash case 02 补测 + 评审 + 并入综合榜） | [evaluations/round-05-glm-5.3-flash-case02.md](evaluations/round-05-glm-5.3-flash-case02.md) |
| Round 05 评审全文（GPT-5.6-sol 双样本） | [evaluations/gpt5.6-review-glm5.3flash-case02.md](evaluations/gpt5.6-review-glm5.3flash-case02.md) |
| Round 02 评测记录（结构化） | [evaluations/round-02-two-project-combined.md](evaluations/round-02-two-project-combined.md) |
| Round 02 增补：workbuddy auto × GLM-5.2 评测记录（01） | [evaluations/round-02-workbuddy-auto-glm5.2.md](evaluations/round-02-workbuddy-auto-glm5.2.md) |
| workbuddy auto × GLM-5.2 的 01 评审全文（GPT-5.6 审稿，53.0/100，Major Revision） | [benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md](benchmarks/Review/260816-review-workbuddy-auto-glm5.2-E01.md) |
| 完整榜单与更新记录 | [docs/leaderboard.md](docs/leaderboard.md) |
| Case 详情：Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case 详情：1000 Genomes Phase 3（Auton 2015） | [benchmarks/humangenomics/](benchmarks/humangenomics/) |
| dsh-science 插件（执行评测的 Harness 插件） | <https://github.com/biociao/dsh-science> |

> **欢迎参与评测**：欢迎用你的 LLM（Claude、GPT 等）× Harness 工具复现上述题目，将报告提交到本仓库，一起参与评测比较，提供更全面的参考。

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
