# 1000 Genomes Phase 3 (Auton et al. 2015) Reproduction Benchmark

## Scientific task

对 1000 Genomes Project Consortium (2015) *A global reference for human genetic variation* (Nature 526:68–74, DOI 10.1038/nature15393) 的核心人群遗传学论断进行独立计算复现，输入为官方发布的 chr21（可选 chr22）VCF 与样本 panel。

> 完整候选调研（含 gnomAD / GIAB / Ng 2010 的评估与排除理由）见 [docs/human-genomics-case-research.md](../../docs/human-genomics-case-research.md)。

## 固定输入（Fixed Inputs）

| 项 | 定义 |
|---|---|
| task prompt | 对 Auton et al. (2015) 1000 Genomes Phase 3 的人群遗传学核心论断做**独立计算复现**。输入：chr21 GRCh37 v5b VCF + 样本 panel。必须完成：① 验证样本结构（2,504 个体 / 26 人群 / 5 超级人群）；② 逐染色体变异计数（SNP / indel / singleton AC=1）并与论文 Supplementary Table 1 比对；③ 每基因组变异负担与 singleton 换算验证（Table 1）；④ chr21 PCA 并评估 5 超级人群聚类（ARI ≥ 0.9）；⑤ 两两超级人群 Fst（Weir & Cockerham）。输出 claim 级结果表、可重跑代码、环境锁定、执行日志。 |
| source paper | 1000 Genomes Project Consortium. *A global reference for human genetic variation*. Nature 526:68–74 (2015). DOI 10.1038/nature15393 |
| permitted data sources | EBI FTP `release/20130502/` 或 AWS `s3://1000genomes` 的 chr21（可选 chr22）VCF 与 `integrated_call_samples_v3.20130502.ALL.panel`；**禁止**使用第三方汇总统计或现成 PCA/Fst 结果 |
| permitted software | bcftools、plink2、scikit-allel、EIGENSOFT(smartpca)；Python/R 通用科学计算库；须锁定版本并记录 |
| time budget | 24 小时（含数据下载与运行） |
| compute budget | 单机：8 核 CPU / 16 GB 内存 / 100 GB 磁盘；无需 GPU |
| internet policy | 允许联网（文献、工具文档、数据下载）；检索不计分但计入 time budget |
| human intervention policy | ≤2 次人工介入（须逐次记录理由）；核心分析步骤禁止人工代跑 |

## 数据输入（官方发布，实测大小）

| 项 | 值 |
|---|---|
| chr21 VCF | GRCh37 v5b，**~200 MB**（EBI FTP / AWS `s3://1000genomes` / Azure 开放镜像） |
| chr22 VCF（可选） | GRCh37 v5b，**~196 MB** |
| 样本 panel | `integrated_call_samples_v3.20130502.ALL.panel`，**55 KB** |
| 合计 | **~400 MB**（远低于预算上限） |
| 许可 | 开放访问、无登录、无 dbGaP 授权 |

- 参考基因组版本：论文使用 **GRCh37**；GRCh38 lifted 版本存在（v5a，~219 MB）。版本选择是**真实复现陷阱评分点**。
- 注意：全 26 条染色体 VCF 全集数百 GB，**只下载 chr21（+chr22）即可复现全部核心结论**。
- 运行时长：单机 2–6 小时（VCF 统计 10–30 min + PCA 10–30 min + Fst 分钟级）。

## Core claims（可计算验证）

1. **样本结构**：2,504 个体、26 个人群、5 个超级人群（AFR/AMR/EAS/EUR/SAS）——panel 与 VCF 头部直接验证。
2. **变异计数**：chr21 逐条计数（SNP / indel / singleton AC=1）并与论文 Supplementary Table 1 的逐染色体发布值比对（实测 chr21：1,105,538 条记录、1,054,447 SNPs、51,091 indels、452,694 singletons）。
3. **每基因组变异负担**：按样本统计非参考位点数与 singleton 数，换算 chr21 尺度后与论文 Table 1（SNP 3.53–4.31M/基因组、singleton 11.4k–14.8k）比例一致。
4. **PCA 人群结构**：2504 样本 × chr21 位点 PCA，超级人群标签聚类一致度（ARI ≥ 0.9）对应论文 Fig 2。
5. **人群分化 Fst**：chr21 上两两超级人群 Fst（Weir & Cockerham），与论文 Fig 3 / 补充材料容差比对。

## 自动评分锚点（全自动、无主观项）

| 锚点 | 指标 |
|---|---|
| 样本/人群结构 | panel 计数精确比对（2,504 / 26 / 5） |
| 变异计数 | 与 Supplementary Table 1 容差比对（±1） |
| 变异负担 | 与 Table 1 比例一致性 |
| PCA | 超级人群 ARI ≥ 0.9 |
| Fst | 两两超级人群容差带 |

## 工具与复现陷阱

- 工具白名单：bcftools / plink2 / scikit-allel / EIGENSOFT(smartpca)
- 陷阱：① 参考基因组版本（GRCh37 vs GRCh38）必须与 VCF 一致；② 计数口径（biallelic vs multiallelic、singleton 定义）需与发布统计一致；③ 单染色体数值与全基因组 headline（84.7M SNPs）的缩放/口径说明。

## Benchmark status

`v0.1 — draft case`

> 待完成：固定输入表（task prompt / time & compute budget / internet & intervention policy）、参考环境（plink2/scikit-allel conda env）。
