# 总榜补充说明

[返回总榜](leaderboard.md) · [各 Round 原始评测](../evaluations/README.md)

本页承载评分来源、争议和未完成双项目的单项成绩；当前总排名只在总榜维护。

## 评分来源与舍入

| 来源 | 收录方式 | 需要说明的边界 |
|---|---|---|
| [R03](../evaluations/round-03-six-system-combined.md) | 六组合外部评审原项目分 | 评审未署名；原评总分与五维公式复算有差异，总榜保留收录分，不在文档整理时重新评分 |
| [R04 / R05](../evaluations/round-05-glm-5.3-flash-case02.md) | GPT-5.6-sol；Auton 为全代码双样本评审 | 综合精确均值 57.875，沿用原收录的一位小数 57.9；总榜显示 57.90 |
| [R09](../evaluations/round-09-chatgpt-rosalind-5.6sol-two-reports.md) | GPT-5.6-sol 最终 HTML 成品评估 | 两项 67.5/68.5，均值 68.0；未等同于完整代码重跑评估 |
| [R10](../evaluations/round-10-genpilot-ds-v4-flash.md) | 已有评估归档与算术复核 | 评审者未署名，未本地重跑；Tyson 原评 79.0、固定权重复算 78.75，Auton 78.00；综合精确值 78.375，显示 78.38 |
| [R11](../evaluations/round-11-dsh-science-workdir-audit.md) | **工作目录代码级审计**（GLM-5.3-Flash 署名）；Tyson 2004 + Auton 2015 双项目重评 dsh-science；**为四家 dsh-science 的最新分（已并入总榜）** | 证据=脚本/日志/中间件/环境而非 HTML 报告；deepseek 的 Tyson 工作目录未随库存档、无法重评，其 Auton 由 R11 更新（75）、Tyson 保留 R03（91）。含评审者 clean-room 重算（Auton：panel、VCF 单例四口径；Tyson：7 项载荷结论抽查全证实）。已产出 4 条 humangenomics 锚点修订（v0.1.1）+ 3 条 tyson2004 修订 |
| [R12](../evaluations/round-12-rosalind-6astra-workdir-audit.md) | Rosalind × GPT-6 Astra 双项目完整工作目录评估；**已并入总榜** | 证据覆盖报告、原始/派生数据、脚本、日志、测试、环境锁和 provenance；Tyson 入口静态检查与 Auton 输入哈希经本轮独立核查，但未全量 clean-room 重算。D5 因缺 token/cost/完整交互数据按 evidence-limited 评分；与 R09 的 GPT-5.6 Sol 视为不同模型版本，不覆盖旧行 |

同一权重公式不代表同一证据输入或评审尺度。总榜统一收录并按成绩排序，具体能力判断需结合各轮次证据。

## 待核验与历史勘误

- **workbuddy E01 评审冲突**：R02 为 53.0，R03 为 77.0。总榜暂沿用 R03 项目分；争议详见 [R02 评审记录](../evaluations/round-02-workbuddy-auto-glm5.2.md) 与 [R03 记录](../evaluations/round-03-six-system-combined.md)。
- **R03 D02/E02 标签互换**：已按报告归属勘误为 D02=92、E02=86；保留原评与勘误记录，见 [R03 原评](../evaluations/round-03-A-F.md)。
- **R04 参照 bins 判定及评审方差**：与早期外部评审存在口径差异；Love 项有 55.8/52.0 两次分值，见 [R04](../evaluations/round-04-glm-5.3-flash.md)。
- **Rosalind 成品与执行工作区版本**：Auton HTML 与现存工作区 ARI 不一致；详细扣分依据见 [R09](../evaluations/round-09-chatgpt-rosalind-5.6sol-two-reports.md)。
- **Rosalind R09 与 R12 不同版本**：R09 评的是 GPT-5.6 Sol 的早期 HTML 成品，R12 评的是 GPT-6 Astra 的完整工作目录；二者证据范围和模型版本均不同。R12 不反向改写或消除 R09 当时存在的 HTML/工作区不一致问题。
- **Genpilot 原评证据**：远程核验主张、PCA 参数选择及覆盖率分母等需进一步独立核验；不影响当前已有评分入榜，见 [R10](../evaluations/round-10-genpilot-ds-v4-flash.md)。
- **R03 报告口径对 dsh-science 的系统性高估（R11 校准，2026-09-04）**：工作目录代码审计后，R03 的 Auton 02 项目分 90–92 下修为 72–79（−13～−18），**Tyson 01 项目分同样下修**（glm-5.2 9.4→73、glm-5.3 9.3→58，−21/−35）。Tyson 侧主因：glm-5.3 循环论证坐实（nif 归属与 per-bin SNP 的 bin 全部来自 NCBI 2014 组装 defline 自带 MAG 标签，GMM 算了但下游从未使用，报告却称"先无监督分箱再对照"）+ 提交脚本（bwa aln，实测 0.20% 比对率）与报告宣称（bwa mem，80.3%，来自未落盘运行）脱节、provenance 与代码矛盾；glm-5.2 存在"每 bin 恰 1 条 16S"夸大（LpIII/Gplasma 16S 文件 0 字节）、SS_OVERRIDE 硬编码、五项子分析无脚本存档。报告审稿无法暴露此类问题；**报告口径下 <2 分的名次差异（如 C 93 vs D 92.5）不应作为能力结论引用**；后续轮次建议两段式评审（报告筛查+工作目录审计）。见 [R11 §9.3](../evaluations/round-11-dsh-science-workdir-audit.md)。
- **R05 对 GLM-5.3-Flash C02/C05 "unverifiable" 的推翻（R11 校准，2026-09-04）**：工作目录证据（`site_classification.csv` 全套计数产物、Fst 十对全口径 + vcftools 逐位点对账 r=1.000000）证实两项均可验证——旧判根因是"HTML 副本无证据"而非"工作区无证据"。C04 "not_reproduced" 仅在"结果未达 ARI≥0.9 阈值"意义下成立（ARI=0.8742，PCA 产物链完整）；"未执行/无产物"含义不成立。代码审计口径下 Auton 从 72.5 上修至 **81**。
- **R04 对 GLM-5.3-Flash Tyson 43.25 的低估（R11 校准，2026-09-04）**：全代码审计支撑 ≈**69**（+25.75）。R04 标注的"D3 受截断影响"被证实（独立分箱、正向对照设计、SNP 重算、工件 SHA-256 全部在目录中可验）；但 D3 并非回到 8.0——新发现独立扣分项：自建 bin 的"nifH 2 hits"实为 P-II/GlnB 调控蛋白正则误中（`nifH` 匹配 "nifHD region" 描述文本，抽查证实）、全部脚本硬编码死路径、"98.8%" 为跨计数上界。
- **"Sanger reads 不可获得"旧假设被推翻（R11，2026-09-04）**：benchmark 及 R01 时代认定 Tyson 原始 reads 不可获得——四个被审 Tyson 项目**全部实测取得 180,713 条 reads**（SRR9434122–25；glm-5.3 与 flash 逐字节核验）。C04 的 data_availability 应改判"可获得"。见 [R11 §9.5](../evaluations/round-11-dsh-science-workdir-audit.md) 与 [tyson2004 README 修订记录](../benchmarks/tyson2004/README.md)。
- **环境可复现全线问题（R11，2026-09-04）**：四个 Tyson 项目无一可在交付位置重跑（chdir/ROOT/WS 硬编码死路径、conda RPATH 烘焙失效致 samtools 崩溃、env yaml 与实际工具不符或无 pin）——评审此类缺陷必须下到代码与环境层，报告审稿完全不可见。
- **benchmark 锚点修正（R11 证实，已落实 v0.1.1）**：C02 "51,091 indels" 实为非双等位-SNP 残差、"452,694 singletons" 为双等位记录 AC=1 口径、"与 Supp Table 1 逐染色体比对"系引用错误（论文未发布逐染色体计数表，五家复现一致发现）；C05 无数值容差带可对照（26×26 表为图像，W&C 聚合口径差 3–10 倍）；C04 ARI≥0.9 对估计量敏感。修订详见 [humangenomics README 修订记录](../benchmarks/humangenomics/README.md)。

## 单项及非双项目成绩

此处只列总榜不能完整表达的单项记录，不另建重复综合榜。

| 对象 | 任务 / 文档类型 | 分数 /100 | 依据 |
|---|---|---:|---|
| phylo-biomni-standard | Tyson 2004 | 52.5 | [R08](../evaluations/round-08-biomni-dcscloud.md) |
| dcsCloud / Genpilot 旧版提交 | Tyson 2004 | 41.5 | [R08](../evaluations/round-08-biomni-dcscloud.md) |
| dsh-science × GLM-5.3-Flash | Love 2014 | 52.0 | [R04](../evaluations/round-04-glm-5.3-flash.md) |
| dsh-science × GLM-5.3-Flash | Zeisel 2015 | 51.5 | [R04](../evaluations/round-04-glm-5.3-flash.md) |
| 两份科研 Harness 培训课件 | 课件评估 | 55.8 / 47.8 | [R06](../evaluations/round-06-codedecks-gpt5.6-sol.md) |
| GPT-5.6 对 workbuddy E01 的评审稿 | 评审文档评估 | 53.5 | [R07](../evaluations/round-07-gpt5.6-sol-rosalind-e01review.md) |

R08 的 dcsCloud 旧版单篇报告不被 R10 新双项目记录覆盖；二者不是同一提交，不能仅据分差推断提升。

## 历史记录与维护

每轮的详细评价、分维度表格和执行证据在 [评测轮次索引](../evaluations/README.md) 对应的子文档中维护。R01/R02 的初始分数、缺测占位和历史名次不重复计入当前总榜。

整理前的完整榜单（含历史表格、轮次解读与更新记录）保留在 [历史快照](leaderboard-history.md)，仅供追溯，不再作为当前成绩入口。新增评测时只更新总榜对应行、轮次子文档及轮次索引，不向总榜追加 Round 专节。
