# Contributing

欢迎提交新的 benchmark、system evaluation 或 rubric 改进。

## 新增系统 / 提交测评结果

请提供：
1. system 名称、版本、类型
2. benchmark version（**不同版本不可直接比较**）
3. 五维原始分数（D1–D5，R02 起 0–100 制）
4. claim-level evidence
5. runtime / human intervention（若可获得）
6. reproducibility level（R0–R4）
7. reviewer identity / date

## 提交流程

1. 复现报告与证据放入 `benchmarks/<case>/reports/`；
2. 在 `evaluations/` 新建一轮评测记录（Round 编号递增）；
3. 将成绩追加到 `docs/leaderboard.md`（附 reviewer scorecard 以便回溯）。

评分口径与提交协议见 [docs/benchmark-protocol.md](docs/benchmark-protocol.md) 与 [docs/rubric.md](docs/rubric.md)。

## 禁止

- 用不同 benchmark version 直接比较
- 没有执行证据却宣称复现
- 删除失败实验记录
- 用宣传材料代替可核查证据

## Reviewer

建议至少一名具备相关科研领域经验的 reviewer；9 分以上结果建议进行第二位 reviewer 或 clean-room verification。
