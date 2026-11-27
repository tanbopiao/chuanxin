# 分诊矩阵 Triage Matrix — v1.0（2026-11-28）

> 依据 2026-11-28 抓取的全量数据：上游 reworkd/AgentGPT 共 **1082 个 PR**（87 open / 995 closed，历史合并 541 个，最后合并 2025-04-29，main 最后提交 2025-04-28），**469 个 issue**，159 位 PR 作者 + 281 位议题发起人。
> 本矩阵是收编的作业底账：每个条目给出处置（ABSORBED=已收编 / ADOPT=待实现 / REJECT=不收，附理由 / OBSERVE=观察）。只增不覆盖；处置变化走追加记录。

## 一、87 个 open PR 分诊

### A. 真修复（ADOPT-P1，收编优先）— 10 个

| PR | 主题 | 处置 |
| --- | --- | --- |
| #1689 | Docker 构建失败：Debian 基础镜像弃用 + Java 11 | **ADOPT** — 复活构建的第一刀，最高优先 |
| #1666 | platform poetry 与新版 Python 包不兼容 | **ADOPT** — 后端可安装的前提 |
| #1663 | docker-compose 数据库主机/端口配置错误 | **ADOPT** |
| #1653 | OpenAIAgentService chat 方法 AttributeError | **ADOPT** |
| #1602 | mutations 错误处理与日志 | **ADOPT** |
| #1601 | 服务器连接报错修复 | **ADOPT** |
| #1551 | ERR_SOCKET_TIMEOUT：npm 版本对齐 | **ADOPT** |
| #1335 | db host 修复 | **ADOPT**（与 #1663 同主题，择优合并） |
| #1063 | 错误信息加状态页链接 | **ADOPT** |
| #1039 | platform 容器与 weaviate 容器端口冲突 | **ADOPT** |

### B. 功能（ADOPT-P2，逐个评估）— 12 个

| PR | 主题 | 处置 |
| --- | --- | --- |
| #1651 | AgentGPT pip 包 | **ADOPT** — 分发形态升级，价值高 |
| #1373 | openai_proxy 支持（中文用户刚需） | **ADOPT** |
| #1260 | SerpApi 备选搜索 API | **ADOPT** |
| #1245 | Windows CMD 安装流程 | **ADOPT** |
| #1688 | 文档与导航菜单 | **ADOPT**（需审实现质量） |
| #1681 | 智能体仪表板页面 | **ADOPT**（需审实现质量） |
| #1672 #1671 | 代码库文档 + 脚手架改进计划 | **OBSERVE** — 仅计划无实现，看后续 |
| #1421 | IDE 扩展 | **OBSERVE** — 范围大，二期再议 |
| #966 #965 #931 | 主题更新三连（同一作者同一需求 #768） | **OBSERVE** — 择优一个实现 |

### C. 文档（ADOPT-P3）— 3 个

#1652 #1295 #1171 — 逐条评估后批量合入。

### D. 依赖升级（DEPS，批量处理）— 51 个

36 个包的 Dependabot 升级，约 15 个已被同包更新版本取代。处置原则：**不逐个合并**——收编时统一做一次依赖现代化（对齐各包最新已验证版本），在账本中按包记录致谢对应 PR。安全相关升级（cryptography、axios、micromatch 等）优先。

### E. 灌水/无效（REJECT）— 5 个

#1685（Create JOCK）、#1683（ok）、#1686（Mimo cli max development，内容不明）、#1141（Management Section，无说明）、#1618（python-publish.yml，目标不明）——无实质内容或与仓库无关。作者仍列入致谢（参与过），但 PR 不收。

### F. 特别条目 — 2 个

| PR | 主题 | 处置 |
| --- | --- | --- |
| #971 | 🌎 Re enable wikipedia — **作者 @asim-shrestha（AgentGPT 创始人本人）** | **ADOPT** — 创始人的 PR 也卡了两年多，优先收编以示敬意 |
| #1053 | 🔧 Local Socket Server — **作者 @awtkns（reworkd 联合创始人）** | **OBSERVE** — 需评估与现行架构的关系 |

## 二、结构性结论

1. **与玄鉴（Cloudflare 安全审计库）的差别**：AgentGPT 的 87 个 open PR 之间冲突少（分散在不同文件），真正的瓶颈是**仓库已死**——2025-04 后零提交、零合并，Next.js 13 + Python 3.10 技术栈持续老化。
2. **复活路径**：先修构建（#1689 + #1666），再统一依赖现代化（清偿 51 个 bump），再吸收 10 个真修复，最后评估功能类。第一步的目标是「clone 下来能跑起来」。
3. **社区规模**：418 位独立贡献者（159 PR + 281 issue），致谢名单规模是玄鉴的 3.4 倍。

## 三、处置统计

ABSORBED 0（待开工）/ ADOPT-P1 10 / ADOPT-P2 5 / OBSERVE 6 / DOCS 3 / DEPS 51（批量清偿）/ REJECT 5 / 特别 2
