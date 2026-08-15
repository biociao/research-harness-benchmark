# Love et al. 2014 (DESeq2) Reproduction Benchmark

## Scientific task

对 Love, Huber & Anders (2014) *Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2* (Genome Biology 15:550, DOI 10.1186/s13059-014-0550-8) 的核心论断进行独立计算复现：地塞米松（Dex）处理人气道平滑肌细胞（ASM）的差异表达分析（airway 数据集，Himes et al. 2014 PLoS One）与 DESeq2 统计方法基准。

## 固定输入（Fixed Inputs）

| 项 | 定义 |
|---|---|
| task prompt | 复现 Love et al. (2014) 的两类核心论断：① **统计 claim**：按论文完全指定的模拟方案（10,000 基因、负二项计数、均值/离散度取自 Pickrell 数据、80% null / 20% DE、FC∈{2,3,4}、m∈{6,8,10,20}）实现 DESeq2 并评估其灵敏度与 FDR 控制（可与 DESeq1/edgeR 对照）；② **生物学 claim**：对 airway 数据（4 Dex vs 4 未处理）做 DESeq2 差异表达，验证 CRISPLD2 显著上调（qPCR/WB 验证锚点）、DUSP1/KLF15/PER1/TSC22D3 检出、DE 基因数 ≈1,069（FDR 0.1）。输出与评分锚点一致的 claim 结果表、可重跑代码、环境锁定、日志。 |
| source paper | Love, Huber & Anders. *Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2*. Genome Biology 15:550 (2014)；配套数据论文 Himes et al. *RNA-Seq transcriptome profiling identifies CRISPLD2 as a glucocorticoid responsive gene*. PLoS One 9:e103874 (2014) |
| permitted data sources | 计数路径：Bioconductor `airway` 包或 GEO GSE52778；原始 reads 路径（进阶）：NCBI SRA SRP033351（8 样本，~15.5 GB SRA）；**禁止**使用他人已算好的 DE 结果列表 |
| permitted software | R + Bioconductor（DESeq2 等）；原始 reads 路径另允许 STAR/hisat2 + featureCounts/subread；版本锁定并记录 |
| time budget | 12 小时（计数路径预期 1 小时内完成） |
| compute budget | 单机：4 核 CPU / 8 GB 内存（原始 reads 路径建议 16 GB）；无需 GPU |
| internet policy | 允许联网（Bioconductor 安装、文档、数据下载）；检索不计分但计入 time budget |
| human intervention policy | ≤1 次人工介入（须记录理由）；核心分析禁止人工代跑 |

## 数据路径（两档可选）

| 路径 | 数据源 | 大小 | 运行时长 |
|---|---|---|---|
| A. 计数矩阵（推荐入门） | Bioconductor `airway` 包 / GEO GSE52778 | 几 MB | 分钟级 |
| B. 原始 reads 全流程 | NCBI SRA SRP033351（8 样本 Dex/未处理） | ~15.5 GB（SRA）；4 样本子集 ~7.5 GB | 数小时（比对+定量+DE） |

- 许可：NCBI/GEO 公开无限制，无需授权。
- 注意：airway 原始流程基于 GRCh37 + Ensembl release 75 归档注释；用新版注释时结果会有偏差，评分按 overlap/rank 容忍。

## Core claims

1. **统计 claim（纯代码复现）**：DESeq2 在论文完全指定的模拟方案下（10,000 基因、负二项、80% null / 20% DE、FC∈{2,3,4}、m∈{6,8,10,20}）比 DESeq1/edgeR 灵敏度更高且 FDR 受控。
2. **生物学 claim**：Dex 处理导致显著差异表达基因集，其中 **CRISPLD2 显著上调**（Himes 2014 以 qRT-PCR + Western blot 实验验证）。
3. **已知靶基因检出**：糖皮质激素响应基因 **DUSP1、KLF15、PER1、TSC22D3** 出现在显著 DE 列表中（Himes 2014 报告 BH p<0.05 共 316 个 DE 基因）。
4. **规范复现基准**：标准 airway 8 样本分析（FDR<0.1）预期得到 **~1,069 个 DE 基因**（官方 DESeq2 vignette 输出）。

## 自动评分锚点

| 锚点 | 指标 |
|---|---|
| CRISPLD2 | 上调且显著（方向 + padj） |
| DUSP1 / KLF15 / PER1 / TSC22D3 | 是否在 top DE 列表 |
| DE 基因数 | ~1,069 @ FDR 0.1（容差带宽评分） |
| 模拟基准 | precision / recall / FDR 控制（与已知 truth 比对） |
| Himes 2014 列表 | 316 个 DE 基因 overlap |

## Benchmark status

`v0.1 — draft case`

> 待完成：固定输入表（task prompt / 软件白名单 / time & compute budget / internet & intervention policy）、参考容器环境（R/Bioconductor）。
