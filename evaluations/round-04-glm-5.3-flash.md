# Round 04 — GLM-5.3-Flash 三篇复现报告 GPT-5.6 评测记录

## 基本信息

| 项 | 值 |
|---|---|
| Round | R04 |
| Benchmark | GT-5.6 单系统评测：GLM-5.3-Flash（dsh-science 插件 × GLM-5.3-Flash）× 3 篇复现报告 |
| 日期 | 2026-09-02 |
| 被评对象 | **Tyson et al. 2004**（宏基因组）、**Love et al. 2014 / DESeq2**（转录组统计+生物学）、**Zeisel et al. 2015**（单细胞图谱）三篇独立复现报告 |
| 评审 | **GPT-5.6-sol**（通过 codex CLI，`codex exec -s read-only`） |
| 评测方式 | 审稿式逐份评分：五维 0–10 制 Rubric（15/30/25/20/10 权重），加权折算 0–100 制；逐维理由 + claim 级状态 + 证据等级 + integrity_flags |
| 状态 | ✅ 完成（**缓存为单样本评审**；首轮 Love = 55.8，复跑 = 52.0，故 Love 取 52.0，分录见下） |

## 重要说明（必读，影响分数解读）

1. **评测范围与榜单口径不匹配**：GLM-5.3-Flash 实际复现的是 **Tyson（=R03 的 case 01）+ Love2014 + Zeisel2015**，**没有**新榜单「02」所追踪的 **Auton 2015 / 1000 Genomes Phase 3** 报告。因此它**无法按「01 Tyson + 02 Auton」的 0–100 综合口径并入 R03 排行榜**；本轮按它实际产出的三类 case **单独记录**，不入综合排名。
2. **给 judge 的输入为「报告叙述 + 交付物清单」**（为控制 token，代码/日志内联在评审中被省略/概括），judge 据此明确压低了 D3（Tyson 4.5 / Love 6.0 / Zeisel 6.0）。若提供全代码，D3 可能上浮；但下面三条 integrity flags 属内容层面，不随代码可见性而消失。
3. **与 R03 同侪的一致性问题**：R03 中 dsh-science×GLM-5.3 的 Tyson 得 **93**，而那份报告同样大量引用 NCBI 参照 bins（`dsh-glm-5.3/manuscript/reproduction_report*` 亦为"NCBI 标签"）。GPT-5.6-sol 把"参照 bins 支撑结论"判为**输入违规**并把总分压到 43——**可能是 judge 判定更严，也可能 GLM-5.3-Flash 确实比同侪更依赖参照**，需人工复核裁决。
4. **评审方差**：本仓库惯例评审间方差 ±3 分；Love 两次采样 55.8 / 52.0，单次结果不宜下强结论，建议第二评审。

## 综合得分（GPT-5.6-sol，五维 0–100 制）

| 报告 | 加权总分 | 审稿结论 | 推荐评级 | D1 | D2 | D3 | D4 | D5 |
|---|---:|---|---|---:|---:|---:|---:|---:|
| **Tyson 2004** | **43.25** | Major Revision | Weak | 6.0 | 4.0 | 4.5 | 4.0 | 3.0 |
| **Love 2014 (DESeq2)** | **52.0** | Major Revision | Developing | 6.0 | 5.0 | 6.0 | 5.0 | 3.0 |
| **Zeisel 2015** | **51.5** | Major Revision | Developing | 6.0 | 4.5 | 6.0 | 5.0 | 4.0 |

> 加权公式：`0.15·D1 + 0.30·D2 + 0.25·D3 + 0.20·D4 + 0.10·D5`。
> Love 首轮 55.8 的取值：D1 6.0/D2 5.0/D3 6.5/D4 5.5/D5 4.5（55.75≈55.8）；复跑 52.0 的取值：D1 6.0/D2 5.0/D3 6.0/D4 5.0/D5 3.0。两次均为 Major Revision，本记录以复跑（持久化）为准，并保留首轮记录于评审存档页眉。

## 各篇核心结论

### 01｜Tyson 2004 — 43.25 / 100（Weak / Major Revision）
- 判 `partially`（群落结构、L2 重建、nif 定位、菌株异质性），`not_reproduced`（固碳/生物膜/金属抗性的自建验证、F2 三菌株重组机制）。
- **关键 flags**：`prohibited_reference_use`（用 NCBI 现成参照 bins 支撑核心结论，违反"禁止使用现成 binning/组装结果"）、`reference_substitution`（用参照注释补自建 bins 缺失）、`claim_overstatement`（L2 仅 69.5% 参照覆盖却称"近完整"）、`artifact_visibility_gap`。
- 证据等级：E1（报告证据）。

### 02｜Love 2014 / DESeq2 — 52.0 / 100（Developing / Major Revision）
- 判 `reproduced`（CRISPLD2 上调、DUSP1/KLF15/PER1/TSC22D3 检出），`not_reproduced`（统计核心 claim，即"DESeq2 ≥ DESeq1/edgeR 灵敏度更高且 FDR 受控"；DE≈1,069）。
- **关键 flags**：`claim_substitution`（把统计核心命题替换为"灵敏度单调、FDR 相对现代 DESeq2 改善"的较弱命题）、`baseline_exclusion`（失败的 DESeq1 近似基线未进主结果）、`numeric_inconsistency`（DE 计数范围 3,384–4,834 vs 4,905）、`unsupported_causal_attribution`。
- 证据等级：E1（报告证据）；存在 E2 工件线索但未核查内容。

### 03｜Zeisel 2015 — 51.5 / 100（Developing / Major Revision）
- 判 `partially`（9 大类恢复、47 亚类、Pax6、CA1/S1 分层），`reproduced`（Slc17a7、Gad1），`not_reproduced`（Itpr2 少突胶质亚类）。
- **关键 flags**：`evaluation_label_leakage`（用评分标签选聚类分辨率，违反"标签仅用于评分比对"）、`claim_substitution`（Itpr2 应为少突胶质亚类，却被验证成 CA1 特异性）、`invalid_metric_comparison`（NMI 0.546 与 ARI 0.465 跨指标比较）、`reference_mapping_uncertainty`。
- 证据等级：E1（报告证据）。

## 横向发现

- 三篇均有**工程交付意识**（脚本/环境/工件/日志清单完整），这是 R03 高分组合强调的"证据闭环"根基；但 judge 认为**缺少可核查的执行内容**（D3 均 ≤6.0），且**关键 claim 存在替换或独立性问题**（D2 均 ≤5.0）。
- 三篇均**未把任何核心 claim 判为 `contradicted`**；`not_reproduced` 多指"目标 claim 未被本复现建立/验证"，不代表原结论为假。
- 与 R03 同侪（A–F，82–97）差距主要来自两块：① **methodology 独立性**（参照 bins、评分标签参与模型选择、统计命题替换）；② **可核查证据/代码可见性**。若补齐代码与独立验证，D3/D5 有望上浮，但 D2 方法学问题需实质修订。

## 遗留问题与建议（R05）

1. 对 **Tyson「参照 bins 支撑结论」** 与 R03 同侪（D=93）的判定不一致——建议人工/第二评审核实；必要时在 rubric 中明确"参照 bins 用作阳性对照 vs 作为结论来源"的边界。
2. **补全代码/日志**后再对三篇做一次全量重评，以确认 D3/D5 的真实水平（本轮 D3 受截断影响）。
3. GLM-5.3-Flash 未完成 Auton/1000G（case 02），如需并入综合榜需补评。
4. 评审为单次 GPT-5.6-sol 采样，建议第二评审；分差 >3 的维度人工复核。

## 细节报告入口

| 内容 | 入口 |
|---|---|
| Tyson 2004 GPT-5.6 评审全文 | [gpt5.6-review-glm5.3flash-tyson2004.md](gpt5.6-review-glm5.3flash-tyson2004.md) |
| Love 2014 GPT-5.6 评审全文 | [gpt5.6-review-glm5.3flash-love2014.md](gpt5.6-review-glm5.3flash-love2014.md) |
| Zeisel 2015 GPT-5.6 评审全文 | [gpt5.6-review-glm5.3flash-zeisel2015.md](gpt5.6-review-glm5.3flash-zeisel2015.md) |
| 原始被评报告（GLM-5.3-Flash 工作区） | `/Volumes/repo/ciao/Harness-bench/dsh-glm-5.3-flash/` |
| 完整榜单与更新记录 | [docs/leaderboard.md](../docs/leaderboard.md) |
