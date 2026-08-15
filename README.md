# 科研场景 Harness 能力评价（Research Harness Benchmark）

一个面向 **Agent / LLM / Skill / Harness** 的科研能力公开评价框架。

目标不是评“谁聊天更聪明”，而是评价一个系统能否在真实科研任务中完成：

> 文献理解 → 数据获取 → 实验设计 → 代码执行 → 结果验证 → 科学论证 → 可复现交付

本仓库提供：
- 五维科研能力评价体系
- 科研可信度加权评分
- Benchmark case 标准模板
- Tyson et al. (2004) 复现案例
- Agent / LLM / Skill 的排行榜数据格式
- 审稿式评分模板
- 可扩展的自动评分脚本

## 五维评价体系

| 维度 | 含义 | 科研可信度权重 |
|---|---|---:|
| D1 | 文献检索与获取 | 15% |
| D2 | 内容理解与逻辑推理 | 30% |
| D3 | 代码生成与复现规范 | 25% |
| D4 | 实验设计与结果可视化 | 20% |
| D5 | 研究过程与效率 | 10% |

### 科研加权分

`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`

评分采用 0–10 分。

## 第一轮 Benchmark

### Tyson et al. (2004)

任务：对 Tyson et al. 2004 的环境微生物组/基因组重建工作进行独立计算复现。

### 排行榜（Tyson2004-v1）

| Rank | System | Harness | LLM | D1 | D2 | D3 | D4 | D5 | Weighted | Evidence | 复现报告 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 🥇 1 | DSH 科研代理 | DSH (DeepSeek Harness) | 待补录 | 9.0 | 9.2 | 9.3 | 8.8 | 9.0 | **9.10** | E2/E3 | [报告](benchmarks/tyson2004/reports/dsh-reproduction-report.md) |
| 🥈 2 | Claude Science | Claude Science | 待补录 | 8.0 | 8.8 | 7.0 | 8.0 | 8.0 | **8.00** | E2 | [报告](benchmarks/tyson2004/reports/claude-science-reproduction-report.md) |

> 加权分公式：`Score = 0.15*D1 + 0.30*D2 + 0.25*D3 + 0.20*D4 + 0.10*D5`（`scripts/score.py` 计算；Claude Science 精确值为 7.99，按 8.00 展示）。
>
> 这是本仓库初始化时的案例基准，不代表永久排名。后续所有新系统应使用同一 case、同一 rubric、同一证据要求重新评测，并将复现报告提交至 `benchmarks/<case>/reports/`。
>
> 完整榜单（含更新记录）见 [docs/leaderboard.md](docs/leaderboard.md)；每期评测评价见 [evaluations/](evaluations/)。

## 核心原则

1. **Claim-first**：先定义要验证的科学论断，再评价 Agent。
2. **Evidence-first**：评分必须绑定证据，而不是只看最终报告。
3. **Execution matters**：代码是否真正执行、结果是否来自执行，是核心指标。
4. **Reproducibility is graded**：复现不是二元变量，而是连续等级。
5. **Failure is evidence**：明确识别不可复现部分不会扣“科学诚信分”，隐瞒失败反而应扣分。
6. **Independent verification**：高分结果应支持第三方 clean-environment rerun。
7. **Versioned benchmark**：Benchmark、数据、评分规则和排行榜均版本化。

## 推荐评级

| 分数 | 等级 | 含义 |
|---:|---|---|
| 9.0–10.0 | Excellent | 接近独立科研执行/审计级 |
| 8.0–8.9 | Strong | 高质量科研助手/Agent |
| 7.0–7.9 | Good | 可完成多数科研分析，但闭环存在缺口 |
| 6.0–6.9 | Developing | 有明显科研执行短板 |
| <6.0 | Weak | 不适合作为可靠科研执行系统 |

## 为什么强调可复现

计算科研的可信度不能只靠“报告写得好”。Nature Methods 对计算可复现性提出从 Bronze/Silver/Gold 的渐进标准；Gold 标准要求整个分析能够自动化执行。citeturn0search0

本项目因此把代码、依赖、环境、数据 provenance、执行日志、结果工件和第三方验证纳入评价。

## Roadmap

- [x] 五维评分体系
- [x] Tyson 2004 初始 benchmark
- [x] 科研可信度加权排行榜
- [x] 第二个生命科学 benchmark（多组学：人基因组学 [humangenomics](benchmarks/humangenomics/) + 转录组学 [love2014](benchmarks/love2014/) + 单细胞 [zeisel2015](benchmarks/zeisel2015/)）
- [ ] 化学/材料 benchmark
- [ ] 临床文献与数据分析 benchmark
- [ ] Agent / LLM / Skill 三类统一提交格式
- [ ] 自动 artifact validator
- [ ] clean-room reproduction
- [ ] GitHub Pages 排行榜
- [ ] benchmark versioning + leaderboard history

## License

建议 MIT；具体 benchmark 数据和论文衍生材料应分别遵守其原始许可证与版权要求。
