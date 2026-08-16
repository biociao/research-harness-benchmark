# Research Harness Benchmark

> 🌐 Language / 语言：English ｜ [**中文**](README.md)

An open evaluation framework for the research capabilities of **Agent / LLM / Skill / Harness** systems.

The goal is not to judge "who chats smarter", but to evaluate whether a system can complete real research tasks:

> Literature understanding → Data acquisition → Experiment design → Code execution → Result verification → Scientific argumentation → Reproducible delivery

This repository provides:
- Five-dimension research capability evaluation framework
- Research credibility-weighted scoring
- Standard benchmark case template
- Tyson et al. (2004) reproduction case
- Leaderboard data format for Agent / LLM / Skill
- Peer-review-style scoring template
- Extensible automated scoring scripts

## Five-Dimension Evaluation Framework

| Dimension | Meaning | Research credibility weight |
|---|---:|---:|
| D1 | Literature search & acquisition | 15% |
| D2 | Content understanding & logical reasoning | 30% |
| D3 | Code generation & reproduction standards | 25% |
| D4 | Experiment design & result visualization | 20% |
| D5 | Research process & efficiency | 10% |

### Weighted Research Score

`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`

Scoring scale: Round 01 (initial) used 0–10; from Round 02 onward the scale is unified to 0–100 (weights unchanged, convention fixed; R03 reviews in the 0–10 scale were converted ×10 when recorded).

## Evaluation Rounds

### Round 03 (Latest) — Six-System Two-Project Re-evaluation (A–F × 2 papers)

> **Scoring convention**: same five-dimension weighted formula as R02 (0–100 scale). This round is an external peer-review-style re-evaluation of **12 reproduction reports** (6 combos × 2 papers); the reviewer scored on a 0–10 scale, converted ×10 into this leaderboard, with the combined total taken from the reviewer's overall score (D/E recomputed as the two-project average after the D02/E02 erratum; formula-recomputed values are in the round record).
> **Combo letters carry over from R02** (A–E identities verified against report contents); **F is a new combo (dsh-science × kimi k3, identity now recorded)**. **D's 02 (Auton 2015) was measured for the first time this round**, closing R02's 93.3† provisional value.
> **Erratum (2026-08-17)**: the original review swapped the D02 and E02 labels (the ARI 0.9106 / vcftools bit-identical report is actually D02; the ARI 0.872 report is actually E02). Corrected on ingestion: D02=92 / E02=86, with D/E combined totals recomputed (92.5 / 81.5).

#### Official Combined Leaderboard (R03)

| Rank | Combo | Harness | LLM | Total /100 | Project scores | Highlights |
|---|---|---|---|---:|---|---|
| 🥇 **1** | **C** | dsh-science | GLM-5.2 | **93** | 01 **94** / 02 **92** | **Most balanced, highest engineering maturity**: provenance chain, oracle-style cross-validation (Fst bit-identical with vcftools, 0.02388 / n=7,335), pinned environment & single-machine rerun guide |
| 🥈 **2** | **D** | dsh-science | GLM-5.3 | **92.5** | 01 **93** / 02 **92** | **Strong on both projects**: Tyson (H1–H4→E01–E04 structure, nif reassignment correction) + 1000G claim-level all-PASS (ARI 0.9106, WC84 Fst bit-identical with vcftools), with bug-fix provenance; 02 measured for the first time |
| 🥉 **3** | **A** | dsh-science | DeepSeek-V1-Flash | **91** | 01 **91** / 02 **91** | **Strongest scientific reasoning**: found the GenBank deposit inconsistent with the paper's assembly and independently re-assembled; thorough disclosure of methodological differences |
| 4 | **F** | dsh-science | kimi k3 | **87** | 01 **83** / 02 **90** | **Rigorous, strong reproduction discipline**: honest boundary disclosure (full text not obtained; canu→miniasm switch); explicit lock files, own WC84 Fst implementation, download-truncation retry with Content-Length check; 4/5 claims supported |
| 5 | **B** | Claude Science | DeepSeek-V1-Flash | **84** | 01 **82** / 02 **86** | Good scientific judgment, but engineering clearly lags behind |
| 6 | **E** | workbuddy (auto) | GLM-5.2 | **81.5**⚠️ | 01 **77** / 02 **86** | Tyson report too "dashboard-like", lacking depth; 02 better than 01 (C4 ARI 0.872 below the 0.9 threshold but honestly reported); ⚠️ conflicts with the R02 review verdict — rank provisional (see below) |

**⚠️ E01 review conflict**: the R03 reviewer gave E01 = 77, and its key numbers (2,731 scaffolds / 16.5 Mb / 5 bins / 18,214 genes) exactly match the workbuddy submission already reviewed in R02, where GPT-5.6 concluded **53.0 / Major Revision (reproduction not established)** (binning taken directly from existing NCBI assignments; broken data provenance). The R03 review did not address those issues, so the two verdicts on the same submission conflict (a 24-point gap); E's score and rank await third-party review / clean-room verification. This leaderboard provisionally adopts the R03 review while keeping the R02 verdict on record.

#### Total Score Ladder Chart

```text
Research Harness Leaderboard (R03 · Combined Total /100)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C  dsh-science × GLM-5.2
██████████████████████████████████████  93
        ↑ Combined Rank #1 (engineering champion: provenance + cross-validation)

D  dsh-science × GLM-5.3
██████████████████████████████████████  92.5
        ↑ Combined Rank #2 (02 first measured 92; 0.5 behind C, within reviewer variance)

A  dsh-science × DeepSeek-V1-Flash
█████████████████████████████████████  91
        ↑ Combined Rank #3 (reasoning champion: data-deposit anomaly finding)

F  dsh-science × kimi k3
██████████████████████████████████  87
        ↑ Combined Rank #4 (rigorous: boundary disclosure + engineering standards)

B  Claude Science × DeepSeek-V1-Flash
████████████████████████████████  84
        ↑ Combined Rank #5 (good science, one-tier-weaker engineering)

E  workbuddy (auto) × GLM-5.2
██████████████████████████████  81.5⚠️
        ↑ ⚠️ Conflicts with R02 Major Revision verdict — rank provisional

  50        60        70        80        90        100
```

#### Per-Project Scores

**01｜Tyson 2004**

| Combo | Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **C** | dsh-science | GLM-5.2 | **95** | **96** | **97** | 93 | **88** | **94** |
| **D** | dsh-science | GLM-5.3 | 94 | **96** | 95 | **94** | **88** | **93** |
| **A** | dsh-science | DeepSeek-V1-Flash | 90 | 94 | 92 | 90 | 87 | **91** |
| **F** | dsh-science | kimi k3 | 80 | 87 | 84 | 82 | 80 | **83** |
| **B** | Claude Science | DeepSeek-V1-Flash | 80 | 87 | 81 | 82 | 80 | **82** |
| **E** | workbuddy (auto) | GLM-5.2 | 75 | 82 | 75 | 78 | 76 | **77⚠️** |

**02｜Auton 2015 (1000 Genomes Phase 3)**

| Combo | Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **C** | dsh-science | GLM-5.2 | 90 | **94** | **96** | **92** | **88** | **92** |
| **D** | dsh-science | GLM-5.3 | **91** | **94** | **96** | **92** | 87 | **92** |
| **A** | dsh-science | DeepSeek-V1-Flash | 90 | **94** | 94 | 90 | 87 | **91** |
| **F** | dsh-science | kimi k3 | 90 | 93 | 92 | 91 | 85 | **90** |
| **B** | Claude Science | DeepSeek-V1-Flash | 87 | 89 | 88 | 86 | 80 | **86** |
| **E** | workbuddy (auto) | GLM-5.2 | 82 | 90 | 89 | 88 | 80 | **86** |

#### Key Conclusions of This Round

- **R02's 93.3† placeholder closed; C confirmed at the top**: D's 02 was measured for the first time (92) → combined **92.5 (Rank 2)**, only 0.5 behind C (93) — the C/D ordering is within inter-reviewer variance (±3 points) and should not be over-interpreted. R02's "update after actual measurement" handling proved necessary.
- **Evidence loops separate the field**: top combos share the closed loop `paper claim → raw data → code → independent verification → conclusion → limitations` (C02's bit-level vcftools cross-validation; D02's post-bugfix rerun log) — "writing a pretty report" is not the dividing line; building an evidence loop is.
- **Finding reproduction failures is high-score behavior**: B02's ARI 0.87 not forced to PASS; E02's ARI 0.872 honestly reported with an AMR explanation; F02's 4/5 claims supported; F01's un-obtained full text / unfinished parts honestly marked; A01's ~2× methodological difference disclosed; D01's nif reassignment correction — consistent with this project's "Failure is evidence" principle.
- **Biggest common problem — chr21 approximations presented as whole-genome reproduction**: most 1000G reports support C4 PCA / burden / Fst / some variant counts with chr21, while the paper is genome-wide / 26×26; the reviewer recommends strictly distinguishing **"claim supported"** from **"paper-level exact reproduction"** (also why no 1000G single score reached full marks this round). R04 plans to encode this in the rubric.
- **Recommended tiers (reviewer): tier 1 C ≈ A ≈ D** (C engineering champion / A reasoning champion / D deep-research champion), tier 2 F, tier 3 B, tier 4 E; after the erratum swap the score order is **C 93 > D 92.5 > A 91** (top-three gaps within reviewer variance) **> F 87 > B 84 > E 81.5**.
- **Inter-reviewer variance ±3 points**: the same submissions scored within ±3 across R02/R03 (C01 91.0→94, D01 93.3→93, A01 90.6→91, B01 84.4→82), with E01 the sole exception (53.0→77) — under single-reviewer scoring, rank gaps of 1–2 points are not conclusive; high scores need a second reviewer.

#### Detail Report Entry Points

| Content | Link |
|---|---|
| R03 full review (per-report scoring of 12 reports, cross-cutting findings, tier recommendation) | [evaluations/round-03-A-F.md](evaluations/round-03-A-F.md) |
| Round 03 evaluation record (structured, with combo-identity verification and cross-round checks) | [evaluations/round-03-six-system-combined.md](evaluations/round-03-six-system-combined.md) |
| Full leaderboard & changelog | [docs/leaderboard.md](docs/leaderboard.md) |
| Case details: Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case details: 1000 Genomes Phase 3 (Auton 2015) | [benchmarks/humangenomics/](benchmarks/humangenomics/) |
| dsh-science plugin (the harness plugin running the evaluations) | <https://github.com/biociao/dsh-science> |

> **Join the evaluation**: You are welcome to reproduce the tasks above with your own LLM (Claude, GPT, etc.) × Harness tool and submit your report to this repository, so we can benchmark it together for a more comprehensive reference.

### Round 02 — Two-Project Combined Evaluation (Historical)

> Historical round; for the latest results see Round 03 above. D's 02 was first measured in R03 (92 → combined 92.5), so this section's provisional 93.3† value and "provisionally #1" status have been superseded by R03 results.

> **Scoring convention (fixed)**: five-dimension weighted score `Total = Literature×15% + Understanding×30% + Reproduction×25% + Experiments/Visualization×20% + Process×10%` (0–100 scale).
> **Combined total = average of the project scores across completed projects 01 and 02**; an unfinished project is provisionally counted at the completed project's score (see D's 02) and updated after actual measurement — the ranking is provisional.
>
> **About the harness name**: **dsh-science** (earlier records write DSH / dsh) in this leaderboard is a research-scenario plugin running on top of DeepSeek Harness that executes this repository's evaluation tasks; source & docs at <https://github.com/biociao/dsh-science>. From R02 onward we consistently use dsh-science; historical rounds (R01) keep their original records.

This round covers two classic paper reproduction projects:

| Project | Paper | Core research task |
|---|---|---|
| **01** | [Tyson et al. 2004, *Nature*](benchmarks/tyson2004/) | AMD environmental metagenomics: microbial genome reconstruction, binning, metabolism & population variation |
| **02** | [Auton et al. 2015, *Nature*](benchmarks/humangenomics/) | Independent reproduction of 1000 Genomes Phase 3 population genetics claims (VCF computation / PCA / Fst) |

#### Official Combined Leaderboard (R02)

| Rank | Harness | LLM | Total /100 | Project scores | Highlights |
|---|---:|---|---|---|---|
| 🥇 **1** | **dsh-science** | **GLM-5.3** | **93.3†** | 01 **93.3** / 02 **93.3†** | **Provisionally #1**; outstanding 01, 02 not yet available — counted at 01's score |
| 🥈 **2** | **dsh-science** | **GLM-5.2** | **91.8** | 01 **91.0** / 02 **92.5** | Most complete research reproduction engineering; claim-level verification, cross-tooling, environment pinning, mature artifact/provenance |
| 🥉 **3** | **dsh-science** | **DeepSeek-V1-Flash** | **90.8** | 01 **90.6** / 02 **91.0** | Strong overall research capability; stable across both domains, especially good disclosure of methodological differences |
| 4 | **Claude Science** | **DeepSeek-V1-Flash** | **85.8** | 01 **84.4** / 02 **87.1** | Decent research analysis, but harness engineering one tier weaker |

**†** D's 02 (Auton 2015) result is not yet available; it is provisionally counted at the 01 score (93.3). The combined total of 93.3 is a **provisional value** and will be updated once 02 is actually measured — the ranking may change.

#### Total Score Ladder Chart

```text
Research Harness Leaderboard (R02 · Combined Total /100)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

D  dsh-science × GLM-5.3
█████████████████████████████████████████████  93.3†
        ↑ Provisional combined Rank #1 (02 pending, counted at 01)

C  dsh-science × GLM-5.2
████████████████████████████████████████████  91.8
        ↑ Combined Rank #2

A  dsh-science × DeepSeek-V1-Flash
███████████████████████████████████████████  90.8
        ↑ Combined Rank #3

B  Claude Science × DeepSeek-V1-Flash
█████████████████████████████████████████  85.8
        ↑ Combined Rank #4

       80      85      90      95      100
```

#### Per-Project Scores

**01｜Tyson 2004**

| Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 89 | 92 | **94** | 92 | 84 | **91.0** |
| A · dsh-science | DeepSeek-V1-Flash | 90 | 92 | 93 | 90 | 82 | **90.6** |
| B · Claude Science | DeepSeek-V1-Flash | 84 | 86 | 85 | 84 | 80 | **84.4** |
| D · dsh-science | GLM-5.3 | 91 | **95** | **95** | **93** | 85 | **93.3** |

**02｜Auton 2015 (1000 Genomes Phase 3)**

| Harness | LLM | Literature | Understanding | Reproduction | Experiments | Process | Project score |
|---|---|---:|---:|---:|---:|---:|---:|
| C · dsh-science | GLM-5.2 | 90 | **94** | **95** | **94** | 86 | **92.5** |
| A · dsh-science | DeepSeek-V1-Flash | 88 | 92 | 94 | 91 | 84 | **91.0** |
| B · Claude Science | DeepSeek-V1-Flash | 85 | 88 | 88 | 87 | 82 | **87.1** |
| D · dsh-science | GLM-5.3 | — | — | — | — | — | **93.3†** |

**†** D's 02 result is not yet available; provisionally counted at the 01 score (93.3), to be updated after actual measurement.

#### Key Conclusions of This Round

- **Harness Effect ≈ +5 points**: A and B use the same LLM (DeepSeek-V1-Flash); dsh-science (90.8) beats Claude Science (85.8) by **5.0 points** — this benchmark measures harness structure differences, not just LLM differences.
- **Swapping to a stronger model on the same harness gains only 1.0 point**: A → C (DeepSeek-V1-Flash → GLM-5.2 on dsh-science), 90.8 → 91.8. In long research tasks, the harness may matter more than simply switching models.
- **GLM-5.3 provisionally #1 (pending 02)**: D01 = 93.3 is outstanding; 02 (Auton 2015) is not yet available and is counted at the 01 score, giving a provisional combined total of **93.3**. This is a provisional ranking — until 02 is actually measured, "GLM-5.3 is definitely #1" cannot be treated as settled.

#### Detail Report Entry Points

| Content | Link |
|---|---|
| Full peer-review evaluation (scoring rationale, claim-level evidence, methodological disclosures, leaderboard) | [benchmarks/Review/260816 bench.txt](benchmarks/Review/260816%20bench.txt) |
| Round 02 evaluation record (structured) | [evaluations/round-02-two-project-combined.md](evaluations/round-02-two-project-combined.md) |
| Full leaderboard & changelog | [docs/leaderboard.md](docs/leaderboard.md) |
| Case details: Tyson 2004 | [benchmarks/tyson2004/](benchmarks/tyson2004/) |
| Case details: 1000 Genomes Phase 3 (Auton 2015) | [benchmarks/humangenomics/](benchmarks/humangenomics/) |
| dsh-science plugin (the harness plugin running the evaluations) | <https://github.com/biociao/dsh-science> |

> **Join the evaluation**: You are welcome to reproduce the tasks above with your own LLM (Claude, GPT, etc.) × Harness tool and submit your report to this repository, so we can benchmark it together for a more comprehensive reference.

### Round 01 (Initial Baseline) — Tyson2004-v1

> Historical round; for the latest results see Round 03 above.

Task: independently reproduce the computational reconstruction of the environmental microbiome/genome work in Tyson et al. 2004.

| Rank | System | Harness | LLM | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | Report |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 🥇 1 | DSH Research Agent | DSH (DeepSeek Harness) | TBD | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | [Report](benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | TBD | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | [Report](benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

> Weighted formula: `Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5` (computed by `scripts/score.py`; Claude Science exact value 7.99, shown as 8.00; R01 used the 0–10 scale).
>
> This is the case baseline from repository initialization and does not represent a permanent ranking. All new systems should be re-evaluated on the same case, the same rubric, and the same evidence requirements, with reproduction reports submitted to `benchmarks/<case>/reports/`.
>
> Full leaderboard (with changelog) at [docs/leaderboard.md](docs/leaderboard.md); per-round evaluation notes at [evaluations/](evaluations/).

## Contributing Benchmark Results

You are welcome to reproduce the tasks above (or any case under [benchmarks/](benchmarks/)) with your own LLM (Claude, GPT, etc.) × Harness tool and submit your evaluation results to this repository for head-to-head comparison. **Only results following the same scoring convention and the same benchmark version can enter the leaderboard.**

**What to submit** (see [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/benchmark-protocol.md](docs/benchmark-protocol.md)):

| Item | Requirement |
|---|---|
| System info | system name / version / type (Harness / LLM / Skill) |
| Benchmark version | which benchmark version was used (e.g., Tyson2004-v1, Auton2015-v1); **different versions are not directly comparable** |
| Raw five-dimension scores | D1–D5 raw scores (0–100 scale from R02 onward, computed with the weighted formula above) |
| Claim-level evidence | status per claim (`reproduced / partially / not_reproduced / contradicted`) with evidence paths |
| Reproducible deliverables | code / pinned environment / execution logs / result artifacts / provenance (reproducibility levels R0–R4) |
| Review info | reviewer identity & date; scores ≥ 9.0 should have a second reviewer or clean-room verification |

**How to submit**:

1. Put your reproduction report and evidence in `benchmarks/<case>/reports/`;
2. Open a new round record in [evaluations/](evaluations/) (incrementing round number);
3. Append your scores to [docs/leaderboard.md](docs/leaderboard.md) (with a reviewer scorecard for traceability).

**Not allowed**:
- Comparing directly across different benchmark versions;
- Claiming reproduction without execution evidence;
- Deleting failed experiment records (failure is evidence);
- Substituting promotional material for verifiable evidence.

Scoring rubric: [docs/rubric.md](docs/rubric.md); submission protocol: [docs/benchmark-protocol.md](docs/benchmark-protocol.md); full contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md).

## Core Principles

1. **Claim-first**: define the scientific claims to verify before evaluating the agent.
2. **Evidence-first**: scores must be tied to evidence, not just the final report.
3. **Execution matters**: whether the code actually ran and whether results come from execution are core metrics.
4. **Reproducibility is graded**: reproduction is not binary but a continuous grade.
5. **Failure is evidence**: clearly identifying non-reproducible parts does not cost "scientific integrity" points; concealing failure should.
6. **Independent verification**: high scores should support third-party clean-environment reruns.
7. **Versioned benchmark**: benchmarks, data, scoring rules, and leaderboards are versioned.

## Recommended Ratings

| Score | Grade | Meaning |
|---:|---|---|
| 9.0–10.0 | Excellent | Near independent research execution / audit-grade |
| 8.0–8.9 | Strong | High-quality research assistant / agent |
| 7.0–7.9 | Good | Completes most research analyses, but gaps in the closed loop |
| 6.0–6.9 | Developing | Notable research execution weaknesses |
| <6.0 | Weak | Not suitable as a reliable research execution system |

## Why Reproducibility Matters

The credibility of computational research cannot rest on "well-written reports" alone. Nature Methods has proposed a progressive Bronze/Silver/Gold standard for computational reproducibility; the Gold standard requires the entire analysis to run automatically.

This project therefore incorporates code, dependencies, environment, data provenance, execution logs, result artifacts, and third-party verification into the evaluation.

## Roadmap

- [x] Five-dimension scoring framework
- [x] Tyson 2004 initial benchmark
- [x] Research credibility-weighted leaderboard
- [x] Second life-science benchmark (multi-omics: human genomics [humangenomics](benchmarks/humangenomics/) + transcriptomics [love2014](benchmarks/love2014/) + single-cell [zeisel2015](benchmarks/zeisel2015/))
- [x] Round 02 two-project combined evaluation (R02: Tyson2004 + 1000 Genomes Phase 3, four-system A/B/C/D comparison, 0–100 scoring convention fixed)
- [x] Round 03 six-system two-project re-evaluation (R03: A–F × 2 papers, 12 reports; D/E's 02 first measured, new combo F added; R02 provisional ranking closed, E01 review conflict flagged, D02/E02 label swap corrected on ingestion)
- [ ] Chemistry / materials benchmark
- [ ] Clinical literature & data analysis benchmark
- [ ] Unified submission format for Agent / LLM / Skill
- [ ] Automated artifact validator
- [ ] Clean-room reproduction
- [ ] GitHub Pages leaderboard
- [ ] Benchmark versioning + leaderboard history

## License

Suggested MIT; specific benchmark data and paper-derived materials should follow their original licenses and copyright requirements.
