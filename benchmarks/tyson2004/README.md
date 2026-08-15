# Tyson 2004 Reproduction Benchmark

## Scientific task

对 Tyson et al. (2004) 的环境微生物组/基因组重建研究进行计算复现。

## 固定输入（Fixed Inputs）

| 项 | 定义 |
|---|---|
| task prompt | 对 Tyson et al. (2004) 酸性矿山排水（AMD）微生物组/基因组重建进行独立计算复现：群落结构（主要 genome bins）、bin 验证（GC / composition / 16S）、核心代谢通路；SNP / recombination 等依赖原始 reads 的结论须单独评估数据可获得性。 |
| source paper | Tyson et al. *Community structure and metabolism through reconstruction of microbial genomes from the environment*. Nature 428:37–43 (2004) |
| permitted data sources | 原始 reads（SRA，若可获得）与论文补充材料；**禁止**使用现成 binning/组装结果 |
| permitted software | 现代开源工具链（组装 / binning / 注释 / 比对）；版本锁定并记录 |
| time budget | 48 小时 |
| compute budget | 单机：16 GB 内存（建议 8 核 CPU） |
| internet policy | 允许联网（文献、数据下载） |
| human intervention policy | ≤2 次人工介入（须逐次记录理由） |

## Core claims

1. 低多样性酸性矿山排水群落可解析为少数主要 genome bins。
2. Leptospirillum / Ferroplasma 等群体可通过 scaffold composition、GC、16S 等证据进行验证。
3. 核心代谢功能可通过基因组证据重新验证。
4. SNP / recombination 等依赖原始 reads 的结论必须单独判断数据可获得性。

## Initial benchmark findings

### Claude Science

- 5 genome bins / community structure：可复现
- GC / gene prediction / key metabolic pathways：可复现
- unsupervised binning：部分复现
- SNP / recombination：由于原始 Sanger reads 不可获得而不可复现

### DSH

进一步采用原始 reads + 现代开源工具链完成端到端重建，并记录：
- environment
- pipeline
- results
- paper-vs-reproduction comparison
- artifact / checksum
- claim-level review

## Benchmark status

`v0.1 — reference case`

正式公开榜单前建议完成一次独立 clean-room verification。
