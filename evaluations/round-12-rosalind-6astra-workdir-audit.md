# Round 12 — Rosalind × GPT-6 Astra 双项目工作目录五维评估

## 基本信息

| 项 | 值 |
|---|---|
| Round | R12 |
| Benchmark | Tyson 2004 + Auton 2015 / 1000 Genomes Phase 3 chr21 |
| 日期 | 2026-09-07 |
| 被评对象 | `Answers/Rosalind-6Astra/` |
| 评审方式 | 完整工作目录审计：报告、脚本、原始/派生数据、环境锁、日志、测试、图形与 provenance；按 `docs/rubric.md` 五维评分 |
| 权重 | D1 15% / D2 30% / D3 25% / D4 20% / D5 10% |
| 独立核查 | Tyson 静态重跑检查；Auton 四项输入 SHA-256；关键结果表、JSON、日志及图形交叉核对 |
| 证据等级 | Tyson：E3-ready（本轮核实到 E2，未全量重跑）；Auton：E3（交付中有重复运行逐位一致证据）；均非 E4 |

本轮评估的是当前完整工作目录，不沿用 R09 对早期“最终 HTML 成品”的 67.5/68.5 分。当前目录已经补齐原始数据、可执行代码、环境锁、日志、测试、中间结果与版本一致性证据，因此作为不同模型版本 `Rosalind × GPT-6 Astra` 单独入榜；`ChatGPT-Rosalind × GPT-5.6 Sol` 的 R09 历史行继续保留。

## 综合成绩

| 报告 | D1 文献 | D2 理解 | D3 代码 | D4 实验/可视化 | D5 过程/效率 | 加权总分 | 科学判定 |
|---|---:|---:|---:|---:|---:|---:|---|
| Tyson 2004 | 9.5 | 9.5 | 9.0 | 8.5 | 7.0 | **89.25** | 高质量部分复现；不能称整篇论文完全复现 |
| Auton 2015 chr21 | 9.5 | 9.5 | 9.5 | 9.0 | 8.0 | **92.50** | 高质量 chr21 子集复现；不构成全基因组论文复现 |
| 双项目平均 | — | — | — | — | — | **90.88** | 完成双项目评估，纳入总榜 |

计算式：`项目分 = 0.15×D1 + 0.30×D2 + 0.25×D3 + 0.20×D4 + 0.10×D5`，再乘 10 转为百分制；综合分为两项目分的算术平均，精确值 90.875，显示为 90.88。

## 1. Tyson 2004

### D1 文献检索与获取：9.5/10

- 取得主文、Supplementary Methods、两份原始自动注释附件、TraceDB FASTA/QUAL/XML/ancillary 文件，并恢复 AADL/CH 历史版本。
- paper→accession→XYG raw reads→历史参考→分析结果的来源链完整；输入、文献及功能参考均有哈希或来源清单。
- 主动保留采样日期、GC、scaffold 末端和注释集合之间的历史冲突，并引入 2009 后续研究审查原 CBB/RuBisCO 解释。
- 未取得原 JAZZ/MALIGN/CrossMatch/Fgenesb 二进制、完整人工组装判断、FISH 原始计数和实验图像；报告已明确披露，属于资料可得性上限。

### D2 内容理解与逻辑推理：9.5/10

- 严格区分独立重算、历史输出审计、后续文献修订与未验证主张。
- 没有把 GC/depth 当细胞丰度、four-gamete 信号当重组事件数、同源基因当酶活或把历史参考标签当完全无监督分箱。
- 逐结论矩阵正确把“三祖先菌株”、FISH、完整代谢网络及现场活性保留为未验证或部分证据。
- 主要未完成项来自原始证据缺失，而不是逻辑逃避；但祖先数量模型和全部代谢通路仍未形成可检验的定量替代方案。

### D3 代码生成与复现规范：9.0/10

- 从 124,805 条真实 XYG Sanger reads 开始，实际完成质量剪切、SPAdes de novo 组装、回贴、分箱、变异、four-gamete、ORF、蛋白恢复和功能竞争分析。
- 有精确环境锁、输入/代码哈希、中间表、BAM/FASTA、合成边界测试、失败即停的阶段入口及隔离 `--fresh` 模式。
- 本轮执行 `bash scripts/tyson_reproduce.sh --check`，41 个代码文件、8 个必需程序、manifest 和 Rmd 均通过静态检查。
- 扣分：原生锁仅覆盖 macOS arm64；现代替代算法不等价于历史管线；默认入口复用已有 assembly；本轮未看到统一入口 `--fresh` 的完整成功重放，因此不标 E4。

### D4 实验设计与可视化：8.5/10

- 7 张图均可正常查看，覆盖 read QC、GC/depth、scaffold bins、多态性、nif 邻域、蛋白恢复和碳固定审计。
- 采用 read/clone 双口径、深度敏感性、历史/新组装对照、竞争同源家族和严格/宽松阈值，能够限制假阳性解释。
- 扣分：未做 MAG completeness/contamination 的独立验证；four-gamete 位点对不独立；缺祖先数模型比较和湿实验层面的功能验证。

### D5 研究过程与效率：7.0/10（evidence-limited）

- 有分阶段日志、缓存复用、失败保护、新运行目录和明确的一键入口，任务覆盖率高。
- 缺少统一全流程 wall time、峰值内存、计算成本、token 消耗和人工介入次数。按 rubric 不能凭成熟的报告形式推断更高效率。

### Tyson 结论

可信复现集中于原始文库、组装结构、LII/FII 多态方向、历史参考恢复和 Leptospirillum III 的 nifHDK 基因潜能。LII 历史参考 ACGT 覆盖约 96.9%，FII 约 85.3%；FII 多态率方向与原文一致。原文“三祖先菌株”、完整代谢网络、FISH 与现场功能没有被独立验证，CBB/type-II RuBisCO 的历史解释不能原样保留。

## 2. Auton 2015 chr21

### D1 文献检索与获取：9.5/10

- 取得 Nature 正式正文、124 页补充资料、PubMed XML、PMC 标识映射、Europe PMC 全文 XML和官方 Phase 3 chr21 VCF/panel。
- 精确纠正任务中的表号错误：Supplementary Table 1 是人口表，Table 3 才是 callset 汇总，且均无 chr21 singleton 论文基准。
- 输入版本、GRCh37坐标、下载端点、文件大小和 SHA-256 完整记录；本轮四项输入哈希全部通过。
- 插件后端当时无适配工作流或可调用文献 API，报告如实记录官方接口回退，没有伪称插件执行成功。

### D2 内容理解与逻辑推理：9.5/10

- 正确区分 record、ALT allele、carrier site、AC=1、MAC=1、均值/中位数以及 chr21/全常染色体范围。
- 11 项 claim 表分别使用 PASS、COMPUTED、PARTIAL、NOT_TESTABLE 和 FAIL_THRESHOLD，避免把计算完成等同于论文数值复现。
- PCA 主分析 ARI=0.872252 未达到预设 0.9 时如实判失败；未选择最有利参数或删除 AMR 后改写结论。
- Fst 明确是新增的 chr21 五超级人群估计，不能冒充论文已发布的同口径十组结果。

### D3 代码生成与复现规范：9.5/10

- 全量扫描 1,105,538 条记录和 2,768,267,152 个样本—位点基因型，从 GT 重算 AC/AN，结果为 0 mismatch。
- 自写 Weir–Cockerham 分量与 scikit-allel 在缺失及不等样本数场景逐位对照；测试覆盖多等位 singleton、稀有参考、FILTER、LD、ARI 置换不变性和 jackknife。
- 统一入口重复执行后，四个核心结果文件 SHA-256、ARI、保留 SNP 数及十组 Fst 完全一致；报告、图、Rmd 和机器可读结果同版。
- 扣分：环境锁仅原生覆盖 macOS arm64；本轮没有在新的 clean-room 环境再次执行完整流程，因此不标 E4。

### D4 实验设计与可视化：9.0/10

- 主 PCA 配方事先固定，附 2/5/10/20 PC 敏感性、ARI/NMI/Hungarian accuracy和混淆矩阵。
- Fst 使用 ratio-of-component-sums，保留负分量，并给出 1 Mb delete-block jackknife 区间；负担图报告中位数与 IQR。
- 图形完整、标签清楚，负结果和 AMR 混合来源直接可见。
- 扣分：研究范围只有 chr21；Fst 没有同口径论文数值基线；jackknife 只有单染色体物理区块，不能表示全基因组不确定性。

### D5 研究过程与效率：8.0/10（evidence-limited）

- 统一入口把测试、GT扫描、独立位点审计、PCA/Fst、汇总及Rmd渲染串成闭环；重复运行约6分钟，失败修复轨迹有记录。
- 仍缺 token/compute cost、峰值内存和完整人工介入统计；压缩包为节省空间不包含完整 VCF 和运行环境，但提供下载与校验脚本。

### Auton 结论

样本结构、AC/AN、chr21 变异计数、singleton 恒等式、个体负担和十组 WC-Fst 均有可核查结果。PCA 未通过 ARI≥0.9；其余染色体和 Table 1 全常染色体绝对值因输入范围未被直接复现；Fst 是有效的新计算而不是与论文数值的一致性复现。

## 3. 本轮核查与限制

本轮独立执行了：

1. Tyson 静态入口检查：41 个代码文件、8 个执行程序及关键清单全部通过。
2. Auton 四项输入的 SHA-256 校验：VCF、panel及两个官方 README 全部匹配。
3. 报告、claim 表、JSON 汇总、日志和图形之间的关键数值交叉核对。

本轮没有重新运行 Tyson 的完整组装/变异/功能流程，也没有在全新环境重建 Auton 软件栈并全量运行，所以不能声称 clean-room verified。R12 的高分来自当前交付已经具备 E3 级复现条件和强一致性记录，不代表所有原论文结论均被复现成功。

## 4. 入榜决定

- 作为 `Rosalind × GPT-6 Astra` 新方案进入双项目总榜。
- Tyson 89.25、Auton 92.50、综合 90.88。
- R09 的 `ChatGPT-Rosalind × GPT-5.6 Sol` 作为不同模型版本继续保留，避免覆盖历史。
- 后续如完成第三方 clean-room 全量重算，应新开评测轮次更新证据等级和分值，不直接改写 R12。
