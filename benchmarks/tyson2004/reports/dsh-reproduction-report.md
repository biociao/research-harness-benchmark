# DSH 科研代理 — Tyson2004-v1 复现报告

| 字段 | 值 |
|---|---|
| System | DSH 科研代理 |
| Type | Agent |
| Benchmark | Tyson2004-v1 |
| Evidence | E2/E3（可核查工件 / 可独立运行） |
| Reproducibility | R3（端到端 pipeline 可复现） |
| Reviewer | TBD（建议 clean-room 二审） |
| Date | TBD |

## 执行摘要

对 Tyson et al. (2004) 酸性矿山排水（AMD）环境微生物组/基因组重建工作进行独立计算复现。DSH 采用原始 reads + 现代开源工具链完成端到端重建，并完整记录 environment、pipeline、results、paper-vs-reproduction comparison、artifact/checksum 与 claim-level review。

## Claim-level 复现结果

| claim_id | claim | status | confidence | 证据 |
|---|---|---|---|---|
| C01 | 低多样性群落可以解析为五个主要 genome bins | reproduced | high | results/binning_5bins.* |
| C02 | scaffold composition / GC / 16S 可以支持主要 bin 的归属 | reproduced | high | results/gc_16s_validation.* |
| C03 | 关键碳/氮固定与能量代谢结论可以从基因组证据重新验证 | reproduced | high | results/metabolic_pathways.* |
| C04 | SNP/重组等依赖原始 reads 的结论可以被独立重新计算 | partially_reproduced | medium | 原始 Sanger reads 可获得性受限，仅部分位点可独立重算 |

## 复现方法

- 数据：原始 reads（可获得部分）+ 论文补充材料
- 工具链：现代开源组装 / binning / 基因预测 / 代谢注释工具
- 流程：reads → assembly → binning → validation（GC/16S/composition）→ 代谢通路注释 → paper-vs-reproduction 对比

## 交付工件

- `environment/`：依赖与版本锁定
- `pipeline/`：可重跑的端到端脚本
- `results/`：binning、GC、基因预测、代谢通路结果
- `provenance/`：数据来源与 checksum
- `logs/`：执行日志
- `reports/`：paper-vs-reproduction comparison 与 claim-level review

## 与论文的差异 / 不可复现部分

- SNP / recombination 相关结论依赖原始 Sanger reads，数据可获得性受限，仅能部分独立重算（C04）。
- 其余核心结论（群落结构、bin 验证、代谢）均与论文一致。

## 评分明细

| D1 | D2 | D3 | D4 | D5 | Weighted |
|---:|---:|---:|---:|---:|---:|
| 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** |

> 加权公式：`0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`（由 `scripts/score.py` 计算）。

## 优势 / 短板

- 优势：D3 领先 — 完整的数据 → 环境 → pipeline → 结果 → artifact 闭环。
- 短板：D4（实验设计与可视化）相对最低；C04 数据可得性依赖需进一步文档化。
