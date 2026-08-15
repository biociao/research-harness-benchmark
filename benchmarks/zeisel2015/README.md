# Zeisel et al. 2015 (Single-Cell) Reproduction Benchmark

## Scientific task

对 Zeisel et al. (2015) *Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq* (Science 347:1138–42, DOI 10.1126/science.aaa1934) 的核心论断进行独立计算复现：3005 个小鼠皮层/海马单细胞（SMART-seq/C1）的细胞类型图谱与 marker 基因验证。

## 固定输入（Fixed Inputs）

| 项 | 定义 |
|---|---|
| task prompt | 复现 Zeisel et al. (2015) 细胞类型图谱：对 GSE60361 的 3005 细胞 UMI 计数矩阵独立执行 QC → 标准化 → 降维 → 聚类 → marker 发现，将聚类结果与论文 level-1（9 大类）/ level-2（47 亚类）逐细胞标签对齐，并验证指定 marker（Pax6 / Itpr2 / Slc17a7 / Gad1 等）与 CA1-vs-S1 分层。输出聚类与对齐结果（ARI/NMI）、marker 分析、可重跑代码、环境锁定、日志。 |
| source paper | Zeisel et al. *Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq*. Science 347:1138–42 (2015). DOI 10.1126/science.aaa1934 |
| permitted data sources | GEO GSE60361 `GSE60361_C1-3005-Expression.txt.gz`（11 MB）与论文补充表；Bioconductor `scRNAseq` 包 zeisel 标签**仅用于评分比对，不得作为聚类输入提示** |
| permitted software | scanpy 或 Seurat（任选其一）；Python/R 通用科学计算库；版本锁定并记录 |
| time budget | 12 小时（预期 <1 小时完成） |
| compute budget | 单机：4 核 CPU / 8 GB 内存（16 GB 舒适）；无需 GPU |
| internet policy | 允许联网（文档、数据下载）；检索不计分但计入 time budget |
| human intervention policy | ≤1 次人工介入（须记录理由）；聚类与评分步骤禁止人工代跑 |

## 数据输入（官方处理矩阵）

| 项 | 值 |
|---|---|
| 数据源 | GEO GSE60361 `GSE60361_C1-3005-Expression.txt.gz` |
| 大小 | **11 MB**（19,973 基因 × 3005 细胞，UMI 计数） |
| 许可 | GEO 公开无限制，无需授权 |
| 运行时长 | QC→标准化→PCA→UMAP→聚类→marker：16GB 单机 <30 分钟 |

> 注意：原始 fastq 约 317 GB（SRA），**超限**。本 case 采用官方处理表达矩阵作为输入——这与论文自身分析所用输入一致，不影响核心论断验证。原始 reads 全流程复现列为进阶（bonus）任务。

## Core claims

1. 3005 个细胞可聚类为 **~9 个 level-1 大类 / 47 个 level-2 分子亚类**（论文摘要："47 molecularly distinct subclasses"；官方门户 level-1 BackSPIN 热图为 nine clusters）。
2. 特定 marker 可识别特定类型：如 **Pax6⁺ layer I 中间神经元、Itpr2⁺ 少突胶质亚类**（Slc17a7 兴奋性锥体、Gad1 抑制性等通用 marker 亦应可验证）。
3. **CA1 与 S1 锥体神经元可分层**（海马 CA1 与体感皮层 S1 的区域性差异）。

## 自动评分锚点

| 锚点 | 指标 |
|---|---|
| level-1 大类（9 类） | 聚类结果 vs 论文逐细胞标签的 **ARI / NMI**（主评分） |
| level-2 亚类（47 类） | 簇数匹配 + level-2 ARI（设容差，bonus 分） |
| marker 基因 | Pax6 / Itpr2 / Slc17a7 / Gad1 等的 **AUROC** 或差异表达方向 |
| CA1 vs S1 | 聚类分离度 / 差异表达方向 |

> 逐细胞标签来源：Bioconductor `scRNAseq` 包 `zeisel` 数据集（level1class / level2class 列）或论文补充表。
> 注意："47 亚类"依赖聚类分辨率，主评分建议以 level-1 为准，level-2 与 marker 作 bonus。

## Benchmark status

`v0.1 — draft case`

> 待完成：固定输入表（task prompt / 软件白名单 / time & compute budget / internet & intervention policy）、参考环境（scanpy/Seurat）、level-1 标签集版本固定（不同 scRNAseq 包版本间为 8–10 类）。
