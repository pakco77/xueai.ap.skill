# xueai.ap.skill

五个相互独立、可单独安装的 AI 产品 Skill。没有父 Skill，也没有总路由。

| Skill | 用途 |
|---|---|
| `agent-architecture-review` | 评审 Agent / AI 产品架构 |
| `ai-model-cost-selector` | 模型选型与 Token 成本诊断 |
| `ai-product-ux-review` | 审美、交互与 AI 产品心理学体检 |
| `vibe-coding-rules-generator` | 生成项目专用的最小开发规则 |
| `opc-launch-ip-check` | OPC 上线前资产、知识产权与合规检查 |

复制任一完整的 `skills/<name>/` 目录即可独立使用。Hermes / Claude Code 使用 `/<name>`，Codex 使用 `$<name>`。

## 来源

本项目改编自洛小山主讲、小山学堂 / 米羊科技出品的[《小山学堂 · AI 从入门到精通》](https://xueai.app/slides/home.html)。原始项目：[itshen/learn-ai](https://github.com/itshen/learn-ai)。

本仓库将课程主题重新整理为五个 Agent 工作流，不替代原课程。本改编版本整理于 2026-08-11。Copyright © 2026 洛小山 · Miyang Tech (Zhuhai Hengqin) Co., Ltd.，依据 [GNU AGPL v3.0](LICENSE) 授权。
