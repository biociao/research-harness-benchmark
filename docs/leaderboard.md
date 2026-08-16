# 科研场景 Harness 能力排行榜

> 榜单规则：同版 benchmark 才能横向比较；评分必须绑定证据（E0–E4），见 [benchmark-protocol.md](benchmark-protocol.md) 与 [rubric.md](rubric.md)。
> 评分口径（R02 起）：五维加权 0–100 制，`总分 = 文献检索×15% + 内容理解×30% + 代码复现×25% + 实验/可视化×20% + 研究过程×10%`；综合总分 = 已完成 01、02 两项目的项目分平均值；未完成项目暂按已完成项目分数占位计入（待实测后更新，排名为暂定）。
>
> **Harness 说明**：榜单中的 **dsh-science**（早期记录写作 DSH / dsh）是运行于 DeepSeek Harness 之上的科研场景插件，负责执行本仓库的评测任务；源码与文档见 <https://github.com/biociao/dsh-science>。R02 起统一使用 dsh-science 表述，历史轮次（R01）保留原始记录。

## Round 02（最新）— 双项目综合榜（Tyson2004-v1 + Auton2015 / 1000 Genomes Phase 3）

| Rank | System | Harness | LLM | 01 项目分 | 02 项目分 | **综合总分 /100** | Status | 显著特点 |
|---:|---|---|---|---:|---:|---:|---|---|
| 🥇 1 | D · dsh-science | dsh-science | GLM-5.3 | 93.3 | 93.3† | **93.3†** | 暂列综合 Rank #1（02 未出，暂按 01 计） | 01 表现突出；科学判断、结果复现、研究状态管理最强 |
| 🥈 2 | C · dsh-science | dsh-science | GLM-5.2 | 91.0 | 92.5 | **91.8** | 综合 Rank #2 | 科研复现工程最完整；claim-level 验证、交叉工具、环境锁定、artifact/provenance 最成熟 |
| 🥉 3 | A · dsh-science | dsh-science | DeepSeek-V1-Flash | 90.6 | 91.0 | **90.8** | 综合 Rank #3 | 综合科研能力很强；两个领域任务都稳定，方法学差异披露尤其好 |
| 4 | B · Claude Science | Claude Science | DeepSeek-V1-Flash | 84.4 | 87.1 | **85.8** | 综合 Rank #4 | 科研分析不错，但 Harness 工程化弱一档 |

**†** D 的 02（Auton 2015）结果尚未产出，暂按 01 分数（93.3）计入；综合总分 93.3 为**暂定值**，待 02 实测后更新，届时排名可能变动。

### 分项目评分

**01｜Tyson 2004**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| A · dsh-science | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| B · Claude Science | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| D · dsh-science | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |

**02｜Auton 2015（1000 Genomes Phase 3）**

| Harness | LLM | 文献 | 理解 | 复现 | 实验 | 效率 | 项目分 |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| A · dsh-science | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| B · Claude Science | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| D · dsh-science | GLM-5.3 | — | — | — | — | — | **93.3†** |

**†** D 的 02 结果尚未产出，暂按 01 分数（93.3）计入，待实测后更新。

## Round 01（初始）— Tyson2004-v1

> 历史轮次（0–10 制），Harness / LLM 列为评测时未记录字段，以"待补录"标注。

| Rank | System | Harness | LLM | Type | Benchmark | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | Status | 复现报告 |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 🥇 1 | DSH 科研代理 | DSH (DeepSeek Harness) | 待补录 | Agent | Tyson2004-v1 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | baseline | [报告](../benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | 待补录 | Agent | Tyson2004-v1 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | baseline | [报告](../benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

## 解读

**Round 02**

- **Harness Effect ≈ +5 分**：A 与 B 同为 DeepSeek-V1-Flash，dsh-science（90.8）比 Claude Science（85.8）高 5.0 分，说明 benchmark 测到的主要是 Harness 结构差异。
- **同一 Harness 换模型仅 +1.0 分**：A → C（DeepSeek-V1-Flash → GLM-5.2），90.8 → 91.8；科研长任务中 Harness 的作用可能比模型本身更显著。
- **D（GLM-5.3）暂列综合第一（待 02 确认）**：在 Tyson 2004 单项目取得当前最高分 93.3；02（Auton 2015）结果未出，暂按 01 分数计入，综合总分暂定 93.3，待实测后更新。

**Round 01**

- DSH 的主要优势来自 D3：完整的数据→环境→pipeline→结果→artifact 闭环。
- Claude Science 的主要优势在 D2：科学内容理解、证据辨析和对不可复现结论的边界识别。

## 注意

本榜单不是模型能力总榜，也不是通用 intelligence 排名。

它评价的是：

> 在指定科研任务、指定规则和指定证据要求下，一个 Harness/Agent/LLM/Skill 完成可靠科研工作的能力。

## 更新记录

- **R02（最新）**：双项目综合评测（Tyson2004-v1 + Auton2015），评分口径固定为 0–100 制五维加权；D·dsh-science×GLM-5.3 **93.3†** 暂列综合第一（02 未出、暂按 01 计入，待实测更新），C·dsh-science×GLM-5.2 **91.8** 第二，A·dsh-science×DeepSeek-V1-Flash **90.8** 第三，B·Claude Science **85.8** 第四。完整审稿记录见 [benchmarks/Review/260816 bench.txt](../benchmarks/Review/260816%20bench.txt)，评测记录见 [evaluations/round-02-two-project-combined.md](../evaluations/round-02-two-project-combined.md)。
- **v0.1（初始）**：Tyson2004-v1，DSH 科研代理 9.10 vs Claude Science 8.00；新增 Harness/LLM 版本列（待补录）。
- 多组学 case（humangenomics / love2014 / zeisel2015）已发布为考题，评测完成后按同一 rubric 追加。
