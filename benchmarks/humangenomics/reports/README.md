# 答卷（模型复现报告）目录

本目录存放各系统对本 case 的答卷（复现报告 md），命名约定：`<system>-reproduction-report.md`。

## 提交要求

1. 按 [benchmarks/templates/submission.yaml](../../templates/submission.yaml) 填写系统信息（name / type / version / harness / LLM）。
2. 答卷须包含：执行摘要、claim 级结果表（对应 claims.yaml 的 C01–C05，状态取 reproduced / partially_reproduced / not_reproduced / contradicted）、证据路径、与论文差异、评分明细。
3. 证据等级 E0–E4 与复现等级 R0–R4 见 [docs/rubric.md](../../../docs/rubric.md)。

## 当前答卷

| System | 答卷 | 状态 |
|---|---|---|
| dsh-science × GLM-5.3-Flash | [dsh-glm-5.3-flash-reproduction-report.md](dsh-glm-5.3-flash-reproduction-report.md)（渲染版 [html](dsh-glm-5.3-flash-reproduction-report.html)；原始工程 `/Volumes/repo/ciao/Harness-bench/dsh-glm-5.3-flash/kgp-phase3-repro/`） | ✅ 已归档（2026-09-02）；答卷自评 9 claims：8 PASS + 1 PARTIAL + 0 FAIL；GPT-5.6-sol 双样本评审 **72.5/100**（Major Revision，E2，judge 口径 C01 reproduced / C03 partial / C02、C05 unverifiable / C04 not_reproduced）；综合 57.9 已入 [leaderboard R05 节](../../../docs/leaderboard.md) |

> 注：R02/R03 各组合（A–F）的 1000G 答卷保留在各自工作区（`/Volumes/repo/ciao/Harness-bench/dsh-*`），未逐一复制到本目录；评审记录见 `evaluations/`。
>
> ⚠️ 答卷重要发现：论文 Supp Table 1 实为人群样本量表，**逐染色体变异计数表论文从未发布**（最细粒度为 Supp Table 3）——benchmarks/humangenomics/README.md 中「逐染色体计数与 Supp Table 1 比对」的锚点描述需在下一版 benchmark 修订时核实更正。
