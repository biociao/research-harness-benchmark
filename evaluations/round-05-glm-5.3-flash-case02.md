# Round 05 — GLM-5.3-Flash 补做 case 02（Auton 2015 / 1000 Genomes Phase 3）复现记录

## 基本信息

| 项 | 值 |
|---|---|
| Round | R05 |
| Benchmark | `1000Genomes-Phase3-v1`（Auton et al. 2015 / 1000 Genomes Phase 3，chr21）——即 R04 遗留问题 #3 指出的 **GLM-5.3-Flash 缺失的 case 02** |
| 日期 | 2026-09-02 |
| 被评对象 | dsh-science × GLM-5.3-Flash（`/Volumes/repo/ciao/Harness-bench/dsh-glm-5.3-flash/kgp-phase3-repro/`） |
| 执行方式 | **dsh headless 一次性任务 + science overlay**（`scripts/run-glm53flash-case02.sh`；overlay=`scripts/overlays/headless-science.yml`：system-prompt persona 换为科学模式 + 注入 research-loop / artifact-registry / remote-compute 引擎行）——与 R04 的「科学模式」GUI 会话同构，模型 `zai/glm-5.3-flash` |
| 固定任务提示词 | `benchmarks/humangenomics/README.md` task prompt 行原文逐字传递（存档于 [scripts/case02-task-prompt.txt](../scripts/case02-task-prompt.txt)） |
| 人工介入 | **0 次**（headless 一次性任务，全程无干预） |
| 用时 / 规模 | 18:05:59 → 20:40:15（**2 h 34 min**，远低于 24 h 预算）；292 次工具调用；会话 `session-0b5ea0d9-3018-4ebc-893f-f391332236e7` |
| 评审 | **GPT-5.6-sol**（codex exec -s read-only，与 R04 同口径）；**双独立样本**取均值：72.20 / 72.80 → **官方采用 72.5**（方差 0.6，verdict 均为 Major Revision，证据等级均为 E2）；评审全文 [gpt5.6-review-glm5.3flash-case02.md](gpt5.6-review-glm5.3flash-case02.md) |
| 状态 | ✅ 复现完成并归档；✅ GPT-5.6 评审完成（72.5/100）；✅ 已按「01+02」口径并入综合榜（见 leaderboard R05 节） |

## 执行概要

从官方 EBI FTP 下载 chr21 GRCh37 **v5b** VCF（~200 MB）+ `integrated_call_samples_v3.20130502.ALL.panel`，conda 锁定环境（bcftools / plink / plink2 / vcftools / R；`envs/kgp-repro.lock.yml`），单实验 E01 五阶段流水（01 样本结构 → 02 变异计数 → 03 每基因组负担 → 04/04b PCA 及敏感性网格 → 05/05b W&C Fst 双实现），结果汇总为 claims_table（9 条 claim），Rmd 渲染自包含 HTML 报告。

## claim 级结果（9 条：8 PASS + 1 PARTIAL + 0 FAIL）

| Claim | 关键观测 | 对照原文 | 判定 |
|---|---|---|---|
| C1 样本结构 | 2,504 个体 / 26 人群 / 5 超级人群，VCF∩panel 双向差集 0/0 | Supp Table 1 逐人群相等 | **PASS** |
| C2 chr21 SNP 计数 | 1,054,447 双等位 SNP（占常染色体总量 81,102,777 的 1.300%） | Supp Table 3 比例相容（论文无逐染色体表，见下） | **PASS** |
| C3 chr21 indel 计数 | 43,988 双等位 indel（份额 1.376%）；位点分类加和恰为 1,105,538 条记录 | Supp Table 3 比例相容 | **PASS** |
| C4 singleton 计数 | 452,695（AC=1，占双等位 SNP 42.93%） | 方向性校验（稀有变异富集） | **PASS** |
| C5 SNP 每基因组负担 | 5 超级人群形状一致性偏差 ≤0.027（去全局偏移） | Table 1（AFR 4.31M … EUR 3.53M） | **PASS** |
| C6 indel 每基因组负担 | 形状一致性偏差 ≤0.016 | Table 1 | **PASS** |
| C7 singleton 换算恒等式 | mean(singletons/genome)=N/2504 恒等式相对误差 8.6e-4；obs/paper 比 0.86–0.89 | Table 1 派生 | **PASS** |
| C8 PCA 人群分离（ARI ≥ 0.9） | 主配方 PC1-5 k-means ARI=**0.8742**；敏感性网格 0.767–0.885；**排除 AMR 后 4 群 ARI=0.9898** | Fig 2a 操作化 | **PARTIAL**（<0.9，机制明确） |
| C9 两两超群 W&C Fst | AFR-out 0.080–0.103 ≫ non-AFR 0.018–0.062；与 vcftools 逐位点 r=1.000000（max Δ=5e-07） | Supp p5 文字锚点（组内 ≈1%） | **PASS** |

## 复现过程中的三个实质发现

1. **引用勘误（对 benchmark 本身有价值）**：论文 Supp Table 1 实为人群样本量表，**逐染色体变异计数表论文从未发布**（最细粒度为 Supp Table 3 常染色体汇总）。`benchmarks/humangenomics/README.md` 中「逐染色体计数与 Supp Table 1 比对（±1）」的锚点描述需在 benchmark 修订时核实更正；答卷已透明改为比例相容性对照。
2. **C8 PARTIAL 的机制诊断**：AFR/EAS/EUR/SAS 在 chr21 上归类近乎完美（no-AMR 4 群 ARI=0.9898），唯一瓶颈是混合人群 AMR 分裂于自身簇与 EUR 簇——属单染色体 + 无监督聚类的操作化阈值问题，不构成对论文论断的反驳。
3. **方法学修复留痕**：① v5b VCF 变异 ID 列大量为"."导致 plink `--extract` 静默失效（改用位置抽取）；② W&C θ 公式与 vcftools 源码逐字比对校准（n 以个体计、合并 h̄、nc 修正）后实现双软件逐位一致——R03 评审强调的「oracle 式独立验证」动作。

## 质量保障

- **两轮独立评审闭环**（manifest 内 reviews）：R01 verdict=needs-work → 7 项整改 → R02 verdict=supported；评审子代理独立重扫 VCF、15 位小数复算 ARI、逐项核对 Supp Table 1/3 数值；C9 判据「事后修订」已如实标注。
- **工件完整性**（本记录入库时由编排侧独立复算）：7 个工件、97 个文件全部 SHA-256 校验通过，0 缺失 0 不一致（chr21-sample-structure 8 / chr21-variant-counts 3 / per-genome-burden 7 / chr21-pca-ari 38 / superpop-fst 37 / claims-table 2 / reproduction-report 2）。
- **一键复现**：`bash experiments/E01/code/run_all.sh`（脚本链 01→06 + config.sh）；环境锁 `envs/kgp-repro.lock.yml` + `ENV_LOCK.md`。

## 交付物

| 内容 | 路径 |
|---|---|
| 复现报告（Rmd 源 + 渲染 HTML 1.4 MB） | `kgp-phase3-repro/manuscript/reproduction_report.{Rmd,html}`；答卷归档 [benchmarks/humangenomics/reports/dsh-glm-5.3-flash-reproduction-report.md](../benchmarks/humangenomics/reports/dsh-glm-5.3-flash-reproduction-report.md)（含 [html](../benchmarks/humangenomics/reports/dsh-glm-5.3-flash-reproduction-report.html)） |
| claim 级结果表 | `kgp-phase3-repro/results/claims_table.{csv,md}` |
| 研究清单（ReAct 循环：5 假设 / 1 实验 / 7 工件 / 2 评审，phase=concluded） | `kgp-phase3-repro/research-manifest.json` |
| 执行会话（模型与工具调用全记录） | `~/.dsh/sessions/--Volumes-repo-ciao-Harness-bench-dsh-glm-5.3-flash--/session-0b5ea0d9-3018-4ebc-893f-f391332236e7/` |

## GPT-5.6-sol 评审结果（双样本，官方分 72.5/100）

| 样本 | D1(15%) | D2(30%) | D3(25%) | D4(20%) | D5(10%) | 加权总分 | 审稿结论 | 证据等级 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Run 1 | 8.2 | 6.5 | 7.2 | 7.2 | 8.0 | **72.20** | Major Revision | E2 |
| Run 2 | 8.6 | 6.5 | 8.0 | 6.2 | 8.0 | **72.80** | Major Revision | E2 |
| **采用（均值）** | 8.4 | 6.5 | 7.6 | 6.7 | 8.0 | **72.5** | Major Revision | E2 |

### 评审要点（两样本共识）

- **D3 显著回升**：全代码 + 执行证据入评后 D3 = 7.2/8.0（R04 三篇 D3 = 4.5/6.0/6.0）——证实 R04 遗留 #2 的「D3 受截断影响」判断；D5 = 8.0（R04 为 3.0/3.0/4.0），runtime/零介入/工件完整性证据被采信。
- **claim 级状态（judge 严格口径，与答卷自评「8 PASS + 1 PARTIAL」存在分歧）**：C01 reproduced；C03 partially_reproduced；**C02 / C05 unverifiable**（答卷发现的 Supp Table 1 引用勘误成立，但改用的比例/格局判据不等价于原 ±1 与 tolerance-band 对照，且 Supp Table 5 数值未转录）；**C04 not_reproduced**（ARI 0.8742 < 0.9，no-AMR 0.9898 属改变标签集合的诊断，不能挽救五群 claim）。
- **integrity flags**（Run 2 全文）：判据替换后过度报 PASS（C2–C4、C9）、C9 判据事后修订（已披露但应作探索性）、「全部完成」表述不准确、run_all.sh 未含 04b 敏感性步骤、vcftools 版本记录矛盾（0.1.17 vs lock 0.1.16）、manifest 未同步修正。两评审均认定**无伪造结果迹象**（"没有证据显示未执行代码被蓄意描述为已执行"）。
- **亮点被认可**：Supp Table 1 引用勘误的主动披露、PCA/Fst 双实现交叉验证、singleton 口径澄清、完整哈希链。

## 与 R04 的关系及后续

1. **R04 遗留 #3 关闭**：GLM-5.3-Flash 的 case 02 缺口已补齐并完成评审（72.5）。综合分按 R02 起口径 =（01 Tyson 43.25 + 02 Auton 72.5）/ 2 = **57.9**，已记入 [docs/leaderboard.md](../docs/leaderboard.md) R05 节（GPT-5.6-sol 口径，与 R03 评审口径不可直接互比，见该节说明）。
2. **R04 遗留 #2 部分验证**：全代码入评后 D3 = 7.6（均值），显著高于 R04 三篇的 4.5–6.0——「D3 受截断影响」的判断成立；但 R04 三篇的全量重评（带完整代码）仍待做。
3. **答卷自评 vs judge 口径的方法学差距**：答卷把「对照策略改变」计为 PASS（8 PASS/1 PARTIAL），judge 按原 claim 语义判 unverifiable/not_reproduced——这是 D2 6.5 的主因，也是后续系统应吸取的口径教训（claim 替换须降级为探索性结果）。
4. **benchmark 修订建议**：核实 Supp Table 1 引用勘误（见上）；`humangenomics/README.md` 的「实测 chr21：452,694 singletons」与答卷口径（452,695，AC=1 全变异 vs 仅 SNP）差 1，在 ±1 容差带内，建议在 claims.yaml 注明 singleton 定义口径；C02/C05 的判定锚点需给出论文之外的替代权威参照（如 IGSR 发布统计页），否则该两条对任何系统都趋向 unverifiable。

## 复现执行方式（供其他组合对齐）

```bash
# 模型：~/.dsh/settings.yaml agent-default-model = zai/glm-5.3-flash（key 走 ~/.dsh/.credentials.yaml）
scripts/run-glm53flash-case02.sh
# 等价于：
cd /Volumes/repo/ciao/Harness-bench/dsh-glm-5.3-flash && \
dsh --profile headless --patch <repo>/scripts/overlays/headless-science.yml "$(cat <repo>/scripts/case02-task-prompt.txt)"
```
