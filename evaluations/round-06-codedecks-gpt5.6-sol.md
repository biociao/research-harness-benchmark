<!-- 评审存档：两份科研 Harness 培训课件 × GPT-5.6-sol（codex CLI）
     评审模型：GPT-5.6-sol（codex exec -s read-only，与 R04/R05 同口径）
     评审输入：两份 PPT 课件逐页文本 + 演讲者备注（纯文本抽取）
     被评对象：
       ①  Research-Harness-Training-90min.pptx（从论文到证据 · 90 MIN · BIOCIAO LAB Training）
       ②  AI-BI-SCI-Claude-Science-Aesthetics-Harness.pptx（Claude Science 美学 × Harness 解构）
     scripts/score.py 复算：Deck1 5.58 / Deck2 4.78（×10 = 55.8 / 47.8）✓
-->

# Round 06 — 两份科研 Harness 培训课件 GPT-5.6-sol 评测记录

## 基本信息

| 项 | 值 |
|---|---|
| Round | R06 |
| 被评对象 | 两份培训课件（PPT）：① Research-Harness-Training-90min（从论文到证据 · 90 MIN）② AI-BI-SCI-Claude-Science-Aesthetics-Harness（Claude Science 美学 × Harness 解构） |
| 评审 | **GPT-5.6-sol**（通过 codex CLI，`codex exec -s read-only`，与 R04/R05 同口径） |
| 评测方式 | 五维 0–10 制 Rubric（15/30/25/20/10 权重），加权折算 0–100 制；逐维理由 + 证据等级 + integrity_flags |
| 状态 | ✅ 完成 |

> **口径说明**：这两份被评对象是**教学/课程交付物**（培训课件），不是论文复现报告。按五维 Rubric 评估其在「教会/体现科研 Harness 能力」上的质量与严谨度。因为是纯课件、无真实执行工件，D3/D5 按 rubric 标记 evidence-limited，评审已相应压低。

## 综合得分（GPT-5.6-sol，五维 0–100 制）

| 课件 | 加权总分 | D1 | D2 | D3 | D4 | D5 | 证据等级 |
|---|---:|---:|---:|---:|---:|---:|---|
| ① Research-Harness-Training-90min | **55.8** | 5.0 | 7.4 | 4.2 | 5.8 | 4.0 | E1 / R1 |
| ② AI-BI-SCI-Claude-Science-Aesthetics | **47.8** | 5.8 | 7.1 | 3.0 | 3.8 | 2.7 | E1 / R1 |

> 加权公式：`0.15·D1 + 0.30·D2 + 0.25·D3 + 0.20·D4 + 0.10·D5`。Deck1 = 5.58、Deck2 = 4.78（0–10），×10 折算。

---

## ① Research-Harness-Training-90min（从论文到证据 · 90 MIN）

### 一句话结论

**55.8/100 — 概念框架扎实、教学立场严谨（D2 亮点），但作为课程交付物缺少可核查的论文/数据实证与执行工件，D1/D3/D5 被压。**

### 五维评分表

| 维度 | 得分/10 | 权重 | 一句话理由 |
|---|---:|---:|---|
| D1 文献检索与获取 | 5.0 | 15% | 引用 BioMni/Anthropic/OpenAI 官方页面并给出 accession「GSE60361」，但 Zeisel 2015 原始论文、矩阵下载地址、版本与校验信息均缺失，paper→dataset→accession→evidence 链未形成 |
| D2 内容理解与逻辑推理 | 7.4 | 30% | 较好落实 claim-first，拆分 C01–C03，强调「UMAP 像不像不是 C01 充分验收标准」「不能声称 FASTQ 端到端复现」，但各 claim 与论文原文位置、定量阈值及冲突证据未给出 |
| D3 代码生成与复现规范 | 4.2 | 25% | 给出「校验→QC→标准化→PCA+聚类→载入标签→ARI/NMI、Marker→写回 Claim」框架、恢复点与 artifact 思路，但无代码、参数、依赖锁、输入校验与真实运行日志；`agent_result: ARI=…; NMI=…` 仍为占位 |
| D4 实验设计与结果可视化 | 5.8 | 20% | 设计了标签后载入防泄漏 control，提出 ARI/NMI/AUROC/方向/分离度/DE 定量指标及故障注入，但缺预注册阈值、baseline、统计检验、误差/不确定性与实际图表 |
| D5 研究过程与效率 | 4.0 | 10% | 规定了「4 核 CPU｜8–16 GB」「人工介入≤1 次必须记录」「课堂运行 16 分钟」及 R0–R2 恢复点，体现过程治理意识，但无实际 runtime、完成率、迭代、cost、介入或失败恢复日志 → evidence-limited |

### integrity_flags

- 第 13 页称「最小 Pipeline：真实运行」，但全文未提供执行代码、日志、完成时间或非占位结果，不能据此认定已经真实执行。
- 第 15 页的「ARI=…; NMI=…」是占位符，不能作为复现结果或 claim 状态证据。
- Zeisel 2015 实操部分主要标注「Internal course design and local project materials」，未直接引用原始论文及数据文件来源，削弱来源可追溯性。

### review

- strengths：课程结构围绕 claim、指标、输入、环境、artifact 与独立核验建立清晰证据闭环；明确区分处理矩阵复现与 FASTQ 端到端复现，抑制 scope overclaim；以标签泄漏/视觉≠指标/静默漂移等故障注入训练科研诚信审查；强调「可信的未复现＞无证据的成功复现」，教学立场严谨。
- weaknesses：实操案例缺少原始论文定位、数据 URL、版本、checksum、许可信息；没有交付可运行脚本、环境文件、参数表、自动检查或真实结果包；claim 验收阈值、baseline、统计不确定性与异常判定规则不完整；过程效率指标只有计划值无实测。
- confidence：high
- evidence_gaps：Zeisel 2015 原始论文 DOI/权威版本/支持 C01–C03 的原文位置；GSE60361 具体文件、版本、大小、checksum、样本与标签 provenance；完整代码、参数、随机种子、Scanpy/Seurat 版本及依赖锁；实际执行/错误日志、恢复点、第三方重跑记录；ARI/NMI/AUROC/DE 真实结果与预注册阈值；baseline/control、重复、误差条与统计不确定性；实际 runtime/iteration/cost/完成率/介入次数；是否有独立评测者完成 E3/E4 验证。

---

## ② AI-BI-SCI-Claude-Science-Aesthetics-Harness（Claude Science 美学 × Harness 解构）

### 一句话结论

**47.8/100 — 批判意识与架构解构是亮点（D2 良好），但这是最「概念化」的一份：几乎无真实执行证据、无教学案例，D3/D4/D5 被显著压低（为两份中最低）。**

### 五维评分表

| 维度 | 得分/10 | 权重 | 一句话理由 |
|---|---:|---:|---|
| D1 文献检索与获取 | 5.8 | 15% | 引用 Claude Science 官方发布、BioMni 原始论文与 GPT-Rosalind 官方材料，并提醒「避免把产品发布材料当作独立验证」，但未展示检索策略、版本核验、开放性判断或 paper→dataset→accession→evidence 链 |
| D2 内容理解与逻辑推理 | 7.1 | 30% | 区分能力主张与独立证据，指出「自检≠独立验证」「界面完整≠Claim 成立」「持续上下文可能隐藏方法漂移」等边界，但未把具体 claims 逐条拆成假设/结果/解释/冲突证据/可证伪条件 |
| D3 代码生成与复现规范 | 3.0 | 25% | 教导「FIGURE / CODE / ENV / HISTORY」绑定并强调代码应是可检查 artifact，但仅给出示意 `plot_xscale('log')`，无真实执行代码、参数、依赖锁、运行日志、自动检查、恢复点或第三方重跑说明 |
| D4 实验设计与结果可视化 | 3.8 | 20% | 提出分叉比较、结果检查与「图表服务证据」的正确原则，Workshop 要求区分事实与推断，但无明确科研问题对应的实验方案、baseline/control、验证集、定量指标、误差分析或不确定性可视化实例 |
| D5 研究过程与效率 | 2.7 | 10% | 给出「PLAN→EXECUTE→INSPECT→REVIEW→REFINE→PACKAGE」端到端概念循环，但无任务完成率、agent iteration、runtime、token/compute cost、人工介入、失败恢复记录或执行日志 → evidence-limited |

### integrity_flags

- 无（评审未发现内容层面的诚信可疑项；但整份为概念课件，见 evidence_gaps）。

### review

- strengths：把科研工作台的视觉设计与 provenance、审计、可复现性联系起来，教学主线清晰；明确区分官方产品主张、自检机制与独立验证，批判意识好；强调研究对象优先、图代码环境历史绑定以及结果循环与证据循环同步。
- weaknesses：主要停留在架构与设计原则层面，缺少从真实论文、数据集、accession 到结论的完整教学案例；没有真实代码、环境清单、日志、中间结果、自动检查或可下载提交包，无法证明关键步骤实际执行；产品对比缺少逐项引用与可核查证据矩阵；未教授 baseline/control/统计验证/误差与异常处理核心方法；无效率与失败恢复硬数据。
- confidence：high
- evidence_gaps：各网页/论文的访问日期、版本、页码或段落级引用；三个产品对比表每项能力的逐项证据映射；原始论文→数据集/accession→输入文件→claim 的 provenance 链；可执行代码、参数、随机种子、依赖锁、容器/环境导出；真实运行日志、中间结果、自动化测试、失败案例与恢复点；第三方重跑或 clean-room verification；完成率/iteration/runtime/cost/介入时长；含 baseline/control、定量指标、误差条与不确定性报告的完整实验示例。

---

## 横向结论

- **共性**：两课件的**共同亮点在 D2**（概念逻辑、边界意识与批判思维），都把「证据闭环 / 可信未复现 > 无证据成功 / 自检 ≠ 独立验证」作为教学主张——这与本榜单 R03 高分组合强调的「证据闭环」价值取向完全一致。
- **共同失分点**：作为课程交付物，**两者都拿不出真实执行工件**（代码/日志/参数/结果/接入 accession），D3 与 D5 因此被按 evidence-limited 压低；D1 都缺「原文→数据→accession→evidence」的完整可追溯链；D4 都缺预注册阈值、baseline/control、统计不确定性与真实图表。
- **两者的差别**：① 90min 课件更「实操导向」，有 Zeisel 2015 最小复现案例、R0–R2 恢复点与故障注入练习，故 D3/D4 高于 ②；② 美学解构课件更「概念/架构导向」，D2 批判性强但几乎无真实案例与执行证据，故 D3/D4/D5 为最低。
- **口径提醒**：这两份是**培训课件**，与榜单上的论文复现报告（R03/R05）**不是同类型对象**，分值**不可直接与综合榜互比**。本记录仅作为「课件类交付物」的五维定性+定量评测，用于师资/材料质量评估，不入正式综合排行榜。
