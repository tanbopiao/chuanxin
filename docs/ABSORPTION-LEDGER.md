# Absorption Ledger — 吸收账本

> 只增不覆盖。每个收编条目记录来源（上游 PR/issue）、去向（落点文件）与状态。
> 快照基准：上游 reworkd/AgentGPT，2026-11-28，87 open PR / 469 issues。

| 来源 | 主题 | 状态 | 落点 |
| --- | --- | --- | --- |
| （开工前占位——首批评估后填写） | — | — | — |

## Publication record (append-only)

- **2026-11-28** — 收编启动：本地分诊矩阵 v1.0 完成（87 个 open PR 全处置：修复 10 / 功能 5 / 文档 3 / 依赖 51 批量 / 拒绝 5 / 观察 6 / 特别 2），致谢名单生成（418 位共建者）。公开上站候宗源当次令。
- **2026-11-28** — 定名「传薪 (Chuanxin)」（宗源核字），落 README / NOTICE / ACKNOWLEDGMENTS。
- **2026-11-28** — 公开上站 `tanbopiao/chuanxin`（宗源令「执行」）：main 分支推送成功，topics 8 枚，GPL-3.0 核验一致。
- **2026-11-28** — 上站前历史净化（改前备份 /tmp/chuanxin-pre-rewrite.bundle）：①上游两笔 2023 年提交（#1042 Slack webhook block 及后续改进）将 Slack webhook 地址硬编码进 `slack_webhook.py`，全史替换为 `REDACTED_SLACK_WEBHOOK` 占位符（提交信息/作者/时间保留，哈希链变更：上游基 18b073ab→de317ff，收编提交 66a4833a→413cece、065b5c51→cb6ddc6）；②清除两枚 NFS 存储残留文件。全史复扫零残留。
- **2026-11-28** — 上游邀约受阻实锤：reworkd/AgentGPT 已整仓归档（archived，只读），issue/PR/Discussions 均不可写，公告 issue 无法送达（API 403）。邀约公告以本仓 README 承载；对外社区触达候宗源当次令。
