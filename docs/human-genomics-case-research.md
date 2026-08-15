# 人基因组学 Benchmark Case 候选论文调研报告

> 目的：为「AI 科研 Agent 能力评测框架」设计第二个 case（人类基因组学，含变异检测 / 人群遗传学 / 外显子组与全基因组分析）。
> 复现范式：选一篇经典论文，让 Agent **独立计算复现其核心科学论断**；要求证据可核查、代码真执行。
> 硬约束：数据总量 **≤30 GB（理想 ≤10 GB）**；计算可在单机数小时至 1–2 天完成；数据 **公开无限制下载**（dbGaP 授权数据一律排除）。
>
> 调研日期：2026-08；所有文件大小均通过 EBI FTP 目录、AWS S3 列表或 HTTP HEAD 实测（标注「实测」），无法实测的明确标注「需进一步核实」。

---

## 0. 结论速览

| 候选 | 判定 | 一句话理由 |
|---|---|---|
| **1000 Genomes Phase 3 (2015)** | ✅ **推荐（主 case）** | 数据实测仅 ~400 MB（chr21+chr22），claims 全部可定量计算，官方发布值即金标准，自动评分最容易 |
| **gnomAD (2020)** | ⚠️ 备选（chr21 子集可行） | chr21 外显子 sites VCF 实测 684 MB，但 sites VCF 无基因型、核心 LOEUF 模型不可独立重算，复现深度较浅 |
| **GIAB Zook et al. (2014)** | ⚠️ 不推荐作主 case | 金标准自动评分最严格，但原始 reads 实测 158 GB（30x BAM），远超预算；仅适合「pipeline 评测」型 case |
| **Ng et al. (2010, Miller 综合征)** | ❌ **排除** | 原始外显子数据在 dbGaP 受控访问（phs000204），违反「公开无限制下载」硬约束 |

---

## 1. 候选对比表

### 1.1 1000 Genomes Project Phase 3 —— **推荐**

**论文**：*A global reference for human genetic variation*, 1000 Genomes Project Consortium, **Nature 526:68–74 (2015)**, DOI [10.1038/nature15393](https://www.nature.com/articles/nature15393), PMID 26432245

**核心 claims（可计算验证，已对照论文全文 PMC4750478 核实措辞）**：

| ID | Claim（论文原文/数值） | chr21 子集上如何验证 |
|---|---|---|
| C1 | 2,504 个体、26 个人群、5 个超级人群（AFR/AMR/EAS/EUR/SAS） | panel 文件直接数（**实测**：2504 样本；AFR 661 / AMR 347 / EAS 504 / EUR 503 / SAS 489）；VCF 头部样本数（**实测**：2504） |
| C2 | 全数据集 >88M variants：84.7M SNPs、3.6M indels、60k SVs；包含 >99% 频率>1% 的 SNP | chr21 逐条计数并与官方发布值比对（**实测** chr21：1,105,538 条记录、1,054,447 SNPs、51,091 indels、452,694 个 singleton(AC=1)）；与论文 Supplementary Table 1 的逐染色体计数比对 |
| C3 | 典型基因组与参考差异 4.1–5.0M 位点；中位 autosomal 变异位点/基因组：SNP 3.53–4.31M、singleton 11.4k–14.8k（Table 1） | 按样本统计非参考基因型位点数与 singleton 数，换算到 chr21 尺度（chr21 ≈ 基因组 1.5%）后与 Table 1 比例一致 |
| C4 | PCA 将 26 个人群分离为 5 个超级人群聚类（论文 Fig 2） | 对 2504 样本 × chr21 位点跑 PCA（plink2 / scikit-allel / EIGENSOFT），用超级人群标签评估聚类一致度（如 adjusted Rand index ≥0.9） |
| C5 | 人群间分化（Fst；论文 Fig 3 / 补充材料给出超级人群两两 Fst） | chr21 上计算两两超级人群 Fst（Weir & Cockerham），与发布值容差比对 |

**数据位置与许可**：
- GRCh37（论文使用版本）：EBI FTP `https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/`（200 MB/chr21）＋ 镜像 AWS `s3://1000genomes/release/20130502/`、Azure Open Datasets。**开放访问、无登录、无 dbGaP 授权**。
- GRCh38 lifted 版本：同一 AWS bucket（`ALL.chr21...v5a...vcf.gz`，**实测 218,612,970 B ≈ 219 MB**）。
- 样本-人群映射：`integrated_call_samples_v3.20130502.ALL.panel`（**实测 55 KB**）。
- 全 26 条染色体 VCF 全集太大（合计数百 GB，**需进一步核实**精确值）→ **只下载 chr21（可加 chr22）即可复现全部核心结论**。

**数据大小评估（实测）**：chr21 GRCh37 v5b = **209,774,472 B ≈ 200 MB**；chr22 v5b = **≈196 MB**；panel = 55 KB。合计 **≈ 400 MB**，远低于 10 GB 理想线。✅

**复现难点**：
1. 参考基因组版本选择必须与 VCF 一致（GRCh37 论文版本 vs GRCh38 lifted 版本）——真实、可评分的复现陷阱；
2. 需要真实跑通 plink2 / scikit-allel / EIGENSOFT（smartpca）等群体遗传学工具链；
3. 单条染色体的数值与论文全基因组 headline（84.7M SNPs）之间的缩放/口径说明；
4. 计数口径（biallelic vs multiallelic、AC=1 singleton 定义）需与发布统计一致。

**Gold standard / 自动评分**：✅ 极强。官方发布 VCF 与 panel 本身即 ground truth（自洽）；论文 Table 1/Fig 2 提供数值与结构先验。评分 = 容差比对（计数类：精确/±1；PCA 结构：ARI/聚类纯度；Fst：容差带）。无人工主观判断。

**计算评估**：单机即可。chr21 全染色体 VCF 解析与统计 ~10–30 min；PCA（2504 × ~1.05M 位点）~10–30 min（randomized SVD / fastPCA）；Fst 分钟级。总计 **2–6 小时**。✅

---

### 1.2 gnomAD (2020) —— 备选

**论文**：*The mutational constraint spectrum quantified from variation in 141,456 humans*, Karczewski et al., **Nature 581:434–443 (2020)**, DOI [10.1038/s41586-020-2308-7](https://www.nature.com/articles/s41586-020-2308-7), PMID 32461654（全文 PMC7334197）

**核心 claims（已对照全文核实）**：

| ID | Claim | chr21 子集上如何验证 |
|---|---|---|
| G1 | 聚合 125,748 exomes + 15,708 genomes | ⚠️ sites VCF **无基因型列**（**实测**其 `#CHROM` 头部仅 8 列），样本数无法从 VCF 头部直接数；可间接验证（VCF 中 AN 最大值 ≈ 2×125,748；或对照论文/官网数字） |
| G2 | 443,769 个高置信 pLoF 变异（其中 413,097 落在 16,694 基因的 canonical transcript） | 解析 chr21 sites VCF 的 CSQ/LOFTEE 注释，统计 HC pLoF 数，与全基因组数字的比例关系/官方表比对 |
| G3 | 基因约束度量：obs_lof / exp_lof / LOEUF（90% 置信上限）/ pLI；19,197 基因按 LOEUF 十分位分层 | 从 chr21 VCF 用 CSQ(LOFTEE=HC)+AC 重算各基因 obs_lof，与官方 by_gene 表逐基因比对（**实测**表值：DYRK1A obs_lof=3、LOEUF=0.083、pLI=1.0；DSCAM obs_lof=11、LOEUF=0.114、pLI=1.0；APP obs_lof=12、LOEUF=0.259；KCNE1 obs_lof=3、LOEUF=1.48） |

**数据位置与许可**：AWS `s3://gnomad-public-us-east-1`（同 GCS `gnomad-public` 镜像），公开下载，terms of use 宽松（研究使用无限制）。
- chr21 外显子 sites VCF：`release/2.1.1/vcf/exomes/gnomad.exomes.r2.1.1.sites.21.vcf.bgz`，**实测 684,431,973 B ≈ 684 MB**；
- 基因级约束表：`release/2.1.1/constraint/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz`，**实测 4,609,488 B ≈ 4.6 MB**；
- ⚠️ 全外显子 sites VCF 全集 **实测 63.2 GB**（24 个 per-chromosome 文件合计；另有合并单文件 63.15 GB）→ **必须按染色体子集**；genomes chr21 单文件 **实测 6.57 GB**（偏大，不推荐）。

**数据大小评估（实测）**：chr21 sites VCF 684 MB + 约束表 4.6 MB ≈ **0.7 GB** ✅（理想线内）。

**复现难点**：
1. v2.1.1 公开发布的是 **site-only VCF**（无 per-sample 基因型）→ 无法从原始 reads 或基因型层面独立重算，只能做「位点层面 + AC/AN」验证；
2. obs_lof 的精确计数协议（LOFTEE HC + 过滤规则）需对齐 gnomAD 方法学，建议容差评分；
3. 核心创新「期望突变率模型（mutability）」与 LOEUF 本身**不可独立重算**——复现边界是「重算表的一部分并与官方表比对」，计算深度低于 1000G 的 PCA/Fst；
4. 需要 VEP/LOFTEE 注释理解（VCF 内嵌 CSQ 字段）。

**Gold standard / 自动评分**：✅ 官方 by_gene 表即精确金标准（实测 4.6 MB，含 obs_lof/exp_lof/LOEUF/pLI 全列），逐基因数值比对，评分直接。但「独立计算含量」较低。

**计算评估**：VCF 解析（bcftools/pysam）+ CSQ 解析，单机 1–3 小时。✅

---

### 1.3 GIAB Zook et al. (2014) —— 金标准最佳但数据超限

**论文**：*Integrating human sequence data sets provides a resource of benchmark SNP and indel genotype calls*, Zook et al., **Nat Biotechnol 32:246–251 (2014)**, DOI [10.1038/nbt.2835](https://pubmed.ncbi.nlm.nih.gov/24531798/), PMID 24531798

**核心 claims**：
- Z1：整合 **14 个数据集、5 种测序技术、7 个 read mapper、3 个 variant caller**，仲裁生成 NA12878 的高置信 SNP/indel/纯合参考基因型调用（摘要；v2.19 README 可查证数据集清单）；
- Z2：高置信区间覆盖范围（v2.19 README 声明排除 GRCh37 约 23% 的非 N 碱基 → 覆盖 **~77% 非 N 碱基**；**实测** v2.19 BED = 2,215,826,661 bp，即全基因组 3.09 Gb 的 **71.7%**，与「排除 ~23% 非 N 碱基」口径一致）；
- Z3：该基准可用于 pipeline 的 precision/recall 实时评测（方法论 claim，可用 hap.py/RTG vcfeval 复算）。

**数据位置与许可**：
- 基准调用文件（金标准）：NCBI `ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/NA12878_HG001/`，公开无限制。**实测**：v3.3.2 高置信 VCF = 134 MB、BED = 12.5 MB；v2.19 BED = 14.8 MB（v2.19 VCF 全量大小**需进一步核实**，本次下载中断于 33 MB）。
- 原始 reads：同 FTP `data/NA12878/NIST_NA12878_HG001_HiSeq_300x/`。**实测** `RMNISTHS_30xdownsample.bam` = **158,166,081,112 B ≈ 158 GB**；HiSeq300x fastq 为 14 个 flowcell 目录（每目录 ~20–30x，README 原文），per-lane fastq 单文件大小**需进一步核实**（估算每 flowcell ~100 GB+）。另有外显子数据集（Garvan/Nebraska exome，较小，未实测）。

**数据大小评估**：金标准文件本身很小（~150 MB）✅，但**「从原始 reads 独立重调用」所需数据 ≈ 158 GB+，远超 30 GB 上限** ❌。chr21-only 不可行（reads 无法按染色体预下载，必须先下全基因组 BAM/fastq）。外显子子集可行但偏离论文核心（WGS 整合）。

**复现难点**：原始数据过大；若要跑 pipeline 需外显子子集或单 lane（~10x，recall 受限）；GRCh37 参考；复杂变异的表示差异（vcfallelicprimitives/vcfeval）会显著影响 P/R 数值。

**Gold standard / 自动评分**：✅✅ 最强。高置信 VCF+BED 即金标准，hap.py 输出 precision/recall/F1，全自动、无主观项。**这是所有候选中唯一「金标准即论文产物」的 case**——但代价是数据超限。

**计算评估**：若接受外显子/子集方案：BWA-MEM + GATK HaplotypeCaller + hap.py，单机数小时–1 天。

---

### 1.4 Ng et al. (2010) —— ❌ 排除

**论文**：*Exome sequencing identifies the cause of a mendelian disorder*, Ng SB et al., **Nat Genet 42:30–35 (2010)**（注：用户题述「NEJM」——Miller 综合征/DHODH 外显子诊断论文实际发表于 **Nature Genetics**；NEJM 2010;363:918–929 为同一团队的后续工作），DOI [10.1038/ng.499](https://pubmed.ncbi.nlm.nih.gov/19915526/), PMID 19915526。

**核心 claims**：4 例无关 Miller 综合征个体外显子测序（平均 40x，~97% 靶区可调用），过滤公共 SNP 库与 HapMap 后锁定唯一候选基因 **DHODH**（嘧啶从头合成关键酶），Sanger 验证另 3 个家系。

**排除理由**：
1. **数据不可公开获取**：原始外显子数据存放于 dbGaP **受控访问**（如 phs000204 Exome_FreemanSheldon，需机构申请与授权），违反本 benchmark「公开无限制下载」硬约束；
2. 队列仅 4 例，无公开 gold standard 可自动评分；
3. 无原始 reads 时复现退化为「读论文抄结论」，无法满足「代码真执行、证据可核查」。

---

## 2. 推荐结论

### 🏆 推荐主 case：1000 Genomes Project Phase 3（Auton et al., Nature 2015）

| 维度 | 评价 |
|---|---|
| **经典性** | 人类群体遗传学奠基性参考（被引 7,000+），论文 Fig 2（PCA 人群结构）为教科书级结果；论文发表于 2015 年，符合「2010 年以后经典工作优先」 |
| **数据可控性** | **实测 chr21+chr22 ≈ 400 MB**（预算 30 GB 的 1.3%，理想 10 GB 的 4%）；EBI FTP / AWS / Azure 三处开放镜像，无登录、无 dbGaP |
| **Claims 可验证性** | 5 类 claims（样本结构 / 变异计数 / 每基因组变异负担与 singleton / PCA 人群结构 / Fst）全部可从 chr21 VCF + panel 独立计算；单条染色体即可复现论文最重要的**定性结论（人群结构）**与**逐染色体定量结论** |
| **自动评分可行性** | 官方发布 VCF/panel 即 ground truth，论文 Table 1 提供对照数值；计数类容差评分、PCA 结构用 ARI/聚类纯度评分、Fst 用容差带评分——全自动、无主观项 |
| **代码真执行** | 必须真实跑通 plink2 / scikit-allel / EIGENSOFT 等工具链（对齐→LD 剪枝→PCA/Fst），单机 2–6 小时完成 |
| **复现陷阱（评分点）** | 参考基因组版本（GRCh37 vs GRCh38）、计数口径、染色体-全基因组缩放说明、pipeline 版本锁定 |

### 备选 / 排除总结

- **备选 2（gnomAD 2020）**：chr21 子集实测 0.7 GB，官方约束表是精确金标准；但 v2.1.1 公开 VCF 为 site-only（无基因型）、核心 LOEUF 模型不可独立重算，复现深度明显浅于 1000G。适合作为后续第三个 case 或 1000G 的补充题。
- **不推荐作主 case（GIAB 2014）**：金标准自动评分最严格，但「从原始 reads 独立复现」需 **158 GB（实测）** 起步，违反数据约束；建议仅在数据预算放宽（或接受外显子子集）时作为「变异检测 pipeline 评测」型 case。
- **排除（Ng 2010）**：dbGaP 受控数据（phs000204），无公开 gold standard，样本量过小。

### 给 case 落地时的建议（下一步）

1. case 固定输入：chr21 GRCh37 v5b VCF（200 MB）+ panel（55 KB）+ 论文全文；禁止使用第三方预处理/汇总数据；
2. claims.yaml 建议（对齐仓库模板）：
   - C01 样本结构：2,504 样本 / 26 人群 / 5 超级人群（panel + VCF 头部）；
   - C02 变异计数：chr21 记录数 / SNP / indel / singleton 与官方发布一致（实测基线 1,105,538 / 1,054,447 / 51,091 / 452,694）；
   - C03 每基因组变异负担：chr21 上按个体统计非参考位点数与 singleton 数，与 Table 1 缩放一致；
   - C04 人群结构：chr21 PCA 将 5 个超级人群分离（ARI ≥ 0.9）；
   - C05 人群分化：超级人群两两 Fst 与发布值容差一致；
3. 工具白名单：bcftools/plink2/scikit-allel/EIGENSOFT，锁定版本；参考 GRCh37（hs37d5）与 GRCh38 双版本可选（作评分陷阱）；
4. 本次调研已下载并保留的参考文件：`benchmarks/humangenomics/data/`（panel.txt、gnomad 约束表、GIAB v2.19 BED；1000G chr21 VCF 已实测统计后清理，Agent 复现时按上述 URL 重新下载并做 checksum 校验）。

---

## 附录：实测数据清单（本次调研期间）

| 文件 | 来源 | 实测大小 | 备注 |
|---|---|---|---|
| 1000G chr21 GRCh37 v5b VCF | EBI FTP release/20130502 | 209,774,472 B (200 MB) | 头部 2,504 样本；1,105,538 条记录 / 1,054,447 SNPs / 51,091 indels / 452,694 singleton(AC=1)（zcat 统计） |
| 1000G chr22 GRCh37 v5b VCF | EBI FTP release/20130502 | ~196 MB（FTP 列表） | 未逐条统计 |
| 1000G chr21 GRCh38 v5a VCF | AWS s3://1000genomes | 218,612,970 B (219 MB) | lifted 版本 |
| 1000G sample panel | AWS s3://1000genomes | 55,156 B | 2504 样本；AFR 661/AMR 347/EAS 504/EUR 503/SAS 489 |
| gnomAD chr21 exome sites VCF | AWS gnomad-public-us-east-1 | 684,431,973 B (684 MB) | site-only（#CHROM 仅 8 列，无基因型） |
| gnomAD 全外显子 sites VCF 全集 | 同上 | 63.2 GB（24 个 per-chr 文件）+ 合并文件 63.15 GB | 需按染色体子集 |
| gnomAD genomes chr21 sites VCF | 同上 | 6,572,449,452 B (6.57 GB) | 偏大 |
| gnomAD 基因约束表 by_gene | 同上 | 4,609,488 B (4.6 MB) | DYRK1A LOEUF=0.083/pLI=1.0 等可查 |
| GIAB v3.3.2 高置信 VCF / BED | NCBI giab FTP | 134,602,007 B / 12,496,110 B | HEAD 实测 |
| GIAB v2.19 高置信 BED | NCBI giab FTP | 14,776,060 B (14.8 MB) | 覆盖 2,215,826,661 bp = 71.7% 全长 / ~77% 非 N |
| GIAB NA12878 30x BAM | NCBI giab FTP | 158,166,081,112 B (158 GB) | 超预算 ❌ |
| 1000G/gnomAD/GIAB 论文数值 | PMC 全文（PMC4750478 / PMC7334197） | — | 84.7M SNPs、443,769 HC pLoF 等均已核实原文措辞 |
