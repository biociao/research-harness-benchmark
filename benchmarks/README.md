# Benchmarks 总览

| Case | 领域 | 论文 | 数据规模 | 状态 |
|---|---|---|---|---|
| [tyson2004](tyson2004/) | 宏基因组学 | Tyson et al. 2004 | 原始 reads（小） | ✅ v0.1 reference |
| [humangenomics](humangenomics/) | 人基因组学（人群遗传学） | Auton et al. 2015 (1000 Genomes Phase 3) | ~400 MB | 🚧 draft |
| [love2014](love2014/) | 转录组学（bulk RNA-seq / DE） | Love et al. 2014 (DESeq2, airway) | 几 MB ~ 15.5 GB | 🚧 draft |
| [zeisel2015](zeisel2015/) | 单细胞组学（scRNA-seq） | Zeisel et al. 2015 | 11 MB | 🚧 draft |

## 固定输入概览（详细见各 case README「固定输入」节）

| Case | 数据量 | 时间预算 | 算力预算 | 人工介入上限 | 主要工具 |
|---|---|---|---|---|---|
| tyson2004 | 原始 reads（小） | 48 h | 单机 16 GB | ≤2 次 | 现代组装/binning/注释工具链 |
| humangenomics | ~400 MB | 24 h | 8 核 / 16 GB / 100 GB 磁盘 | ≤2 次 | bcftools, plink2, scikit-allel, EIGENSOFT |
| love2014 | 几 MB ~ 15.5 GB | 12 h | 4 核 / 8–16 GB | ≤1 次 | R/Bioconductor (DESeq2), STAR/hisat2+featureCounts |
| zeisel2015 | 11 MB | 12 h | 4 核 / 8–16 GB | ≤1 次 | scanpy 或 Seurat |

## Case 结构约定

每个 case 目录包含：
- `README.md`：Scientific task、数据路径（含大小与许可）、Core claims、自动评分锚点、状态
- `claims.yaml`：claim-first 定义（`benchmark` / `title` / `claims[]`）

通用模板见 [templates/case-template/](templates/case-template/)，协议见 [docs/benchmark-protocol.md](../docs/benchmark-protocol.md)。
