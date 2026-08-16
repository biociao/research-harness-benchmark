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

评分制：初始轮（R01）采用 0–10 分；最新轮（R02）起统一为 0–100 分（五维权重不变，评分口径已固定）。

## 评测轮次

### Round 02（最新）— 双项目综合评测

> **评分口径（已固定）**：五维加权分 `总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`（0–100 制）。
> **综合总分 = 已完成 01、02 两项目的项目分平均值**；未完成项目暂按已完成项目分数占位计入（见 D 的 02），待实测后更新，排名为暂定。

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

**†** D 的 02（Auton 2015）结果尚未产出，暂按 01 分数（93.3）计入；综合总分 93.3 为**暂定值**，待 02 实测后更新，届时排名可能变动。

#### 总分天梯图

```text
科研 Harness Leaderboard（R02 · 综合总分 /100）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

D  DSH × GLM-5.3
█████████████████████████████████████████████  93.3†
        ↑ 暂列综合 Rank #1（02 未出，暂按 01 计）

C  DSH × GLM-5.2
████████████████████████████████████████████  91.8
        ↑ 综合 Rank #2

A  DSH × DeepSeek-V1-Flash
███████████████████████████████████████████  90.8
        ↑ 综合 Rank #3

B  Claude Science × DeepSeek-V1-Flash
█████████████████████████████████████████  85.8
        ↑ 综合 Rank #4

       80      85      90      95      100
```

#### 分项目成绩

**01｜Tyson 2004**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| **C · DSH** | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| **A · DSH** | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| **B · Claude Science** | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| **D · DSH** | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| **C · DSH** | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| **A · DSH** | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| **B · Claude Science** | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| **D · DSH** | GLM-5.3 | — | — | — | — | — | **93.3†** |

**†** D 的 02 结果尚未产出，暂按 01 分数（93.3）计入，待实测后更新。

#### 本轮关键结论

- **Harness Effect ≈ +5 分**：A 与 B 使用同一 LLM（DeepSeek-V1-Flash），DSH（90.8）比 Claude Science（85.8）高 **5.0 分**——当前 benchmark 测到的是 Harness 结构差异，而非单纯 LLM 差异。
- **同一 Harness 换更强模型只提升 1.0 分**：A → C（DSH 上 DeepSeek-V1-Flash → GLM-5.2），90.8 → 91.8。提示在科研长任务中，Harness 的作用可能比单纯换模型更显著。
- **GLM-5.3 暂列综合第一（待 02 确认）**：D01 = 93.3 表现突出；02（Auton 2015）结果未出，暂按 01 分数计入，综合总分暂定 **93.3**。此为暂定排名——在 02 实测前，尚不能把「GLM-5.3 一定综合第一」当作定论。

#### 细节报告入口

| 内容 | 入口 |
|---|---|
| 完整审稿式评测（评分依据、claim 级证据、方法学披露、排行榜） | [benchmarks/Review/260816 bench.txt](benchmarks/Review/260816%20bench.txt) |
| Round 02 评测记录（结构化） | [evaluations/round-02-two-project-combined.md](evaluations/round-02-two-project-combined.md) |
| 完整榜单与更新记录 | [docs/leaderboard.md](docs/leaderboard.md) |
| Case 详情：Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case 详情：1000 Genomes Phase 3（Auton 2015） | [benchmarks/humangenomics/](benchmarks/humangenomics/) |

> **欢迎参与评测**：欢迎用你的 LLM（Claude、GPT 等）× Harness 工具复现上述题目，将报告提交到本仓库，一起参与评测比较，提供更全面的参考。

### Round 01（初始基准）— Tyson2004-v1

> 历史轮次，最新结果请以上方 Round 02 为准。

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
- [ ] 化学/材料 benchmark
- [ ] 临床文献与数据分析 benchmark
- [ ] Agent / LLM / Skill 三类统一提交格式
- [ ] 自动 artifact validator
- [ ] clean-room reproduction
- [ ] GitHub Pages 排行榜
- [ ] benchmark versioning + leaderboard history

## License

建议 MIT；具体 benchmark 数据和论文衍生材料应分别遵守其原始许可证与版权要求。
