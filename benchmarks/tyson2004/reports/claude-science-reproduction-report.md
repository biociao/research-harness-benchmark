# Claude Science — Tyson2004-v1 复现报告

| 字段 | 值 |
|---|---|
| System | Claude Science |
| Type | Agent |
| Benchmark | Tyson2004-v1 |
| Evidence | E2（可核查工件） |
| Reproducibility | R2（关键结果复现） |
| Reviewer | TBD |
| Date | TBD |

## 执行摘要

对 Tyson et al. (2004) 酸性矿山排水（AMD）环境微生物组/基因组重建工作进行独立计算复现。Claude Science 复现了群落结构与关键代谢结论，并对不可复现部分（依赖原始 reads 的 SNP/重组分析）作出了明确的边界识别。

## Claim-level 复现结果

| claim_id | claim | status | confidence | 证据 |
|---|---|---|---|---|
| C01 | 低多样性群落可以解析为五个主要 genome bins | reproduced | high | results/binning_5bins.* |
| C02 | scaffold composition / GC / 16S 可以支持主要 bin 的归属 | reproduced | high | results/gc_16s_validation.* |
| C03 | 关键碳/氮固定与能量代谢结论可以从基因组证据重新验证 | reproduced | high | results/metabolic_pathways.* |
| C04 | SNP/重组等依赖原始 reads 的结论可以被独立重新计算 | not_reproduced | high（结论明确） | 原始 Sanger reads 不可获得 |

> 注：unsupervised binning 环节仅部分复现（bin 数量与主要组成一致，但聚类细节存在偏差）。

## 复现方法

- 数据：论文补充材料与公开数据
- 流程：genome binning → GC / 基因预测 → 关键代谢通路验证 → 与论文结果对比
- 未执行端到端 reads → assembly → binning 全流程

## 与论文的差异 / 不可复现部分

- SNP / recombination 结论：原始 Sanger reads 不可获得，标记为 **不可复现**（如实报告，未隐瞒）。
- unsupervised binning：部分复现，与论文在细节上存在偏差。
- 其余核心结论（5 bins、GC/16S 验证、关键代谢通路）与论文一致。

## 评分明细

| D1 | D2 | D3 | D4 | D5 | Weighted |
|---:|---:|---:|---:|---:|---:|
| 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** |

> 加权公式：`0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`（由 `scripts/score.py` 计算；精确值为 7.99，榜单按 8.00 展示）。

## 优势 / 短板

- 优势：D2 领先 — 科学内容理解、证据辨析、对不可复现结论的边界识别。
- 短板：D3（代码生成与复现规范）明显偏低 — 缺少端到端 pipeline 与完整 artifact 闭环。
