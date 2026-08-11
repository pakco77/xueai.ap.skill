# xueai.ap.skill

把一门 AI 产品课程，提炼成五个真正能在项目里反复调用的场景 Skill。

这五个 Skill 来自洛小山主讲、小山学堂 / 米羊科技出品的[《小山学堂 · AI 从入门到精通》](https://xueai.app/slides/home.html)。它们不是课程摘要，也不是把 5 个场景塞进一个总入口；每个 Skill 都有独立目录、独立触发名、独立说明、独立许可证，可以只安装你需要的那一个。

## 从课程到五个工作场景

课程讲的是完整知识体系；Skill 要解决的是你工作中反复出现的具体任务。这里选择了五组最适合程序化复用的内容：

| 课程主题 | 提炼后的 Skill | 它替你完成什么 |
|---|---|---|
| Agent 工程、Harness、上下文工程、自我改进 | [`agent-architecture-review`](docs/agent-architecture-review.md) | 从 PRD、架构图、代码或流程中找到 Agent 架构风险和最小修复动作 |
| 模型选型、Token 与成本工程 | [`ai-model-cost-selector`](docs/ai-model-cost-selector.md) | 动态核验官方价格，选择模型层级并算清真实月成本 |
| 审美工程、交互工程、AI 产品心理学 | [`ai-product-ux-review`](docs/ai-product-ux-review.md) | 一次完成视觉、交互、等待、信任和心智模型体检 |
| Vibe Coding、协作与上下文管理 | [`vibe-coding-rules-generator`](docs/vibe-coding-rules-generator.md) | 按项目风险生成一套最小可用、可以直接粘贴的开发规则 |
| 一人公司 OPC、确权与上线合规 | [`opc-launch-ip-check`](docs/opc-launch-ip-check.md) | 盘点六把“锁”，判断上线前现在做什么、什么可延后、什么要专业复核 |

每个独立介绍页都包含：30 秒开始提示、服务场景、需要提供的材料、效果与输出、输入 / 输出 Demo、验收标准和能力边界；页面同时直达可安装的 Skill 目录与 `SKILL.md`。

## 30 秒开始

1. 选一个与你当前任务最接近的场景。
2. 复制该 Skill 的完整 `skills/<name>/` 目录到你的 Agent 技能目录。
3. 附上自己的材料，粘贴它的开箱提示。

常见安装位置：

| 宿主 | 技能目录 | 调用方式 |
|---|---|---|
| Hermes | `~/.hermes/skills/<name>/` | `/<name>` |
| Claude Code | `~/.claude/skills/<name>/` | `/<name>` |
| Codex | `~/.codex/skills/<name>/` | `$<name>` |

例如，把 PRD 或代码目录交给架构评审：

```text
/agent-architecture-review

请评审这个 AI 客服产品的 PRD 和架构图。重点检查上下文、工具边界、
记忆、多 Agent、权限、评测、长任务恢复和 Prompt→Harness，
最后给我最小修复动作。
```

在 Codex 中把第一行换成：

```text
$agent-architecture-review
```

## 五个独立 Skill

### 1. Agent 架构评审

适合：你有 PRD、架构图、代码目录或产品流程，但不确定这套 Agent 设计能不能稳定跑起来。

它会检查上下文溢出、工具边界、记忆必要性、单 / 多 Agent、权限审批、评测、长任务恢复，以及 Prompt 是否已经过载、是否需要演化为 Harness。

- [独立介绍、30 秒提示与 Demo](docs/agent-architecture-review.md)
- [Skill 本体](skills/agent-architecture-review/SKILL.md)
- [完整目录](skills/agent-architecture-review/)

### 2. AI 模型与成本选择

适合：你知道请求量、Token、图片、延迟、质量和预算，希望选出够用的模型，而不是凭模型名拍脑袋。

它不会在 Skill 中写死价格。每次运行都必须查供应商官方页面，带 `source_url` 和 `verified_at`，再给模型层级、月成本区间、成本大头和缓存 / 压缩 / 路由 / 降级建议。

- [独立介绍、30 秒提示与 Demo](docs/ai-model-cost-selector.md)
- [Skill 本体](skills/ai-model-cost-selector/SKILL.md)
- [完整目录](skills/ai-model-cost-selector/)

### 3. AI 产品 UX 体检

适合：你有截图、原型、在线页面、UX 文案或完整产品流程，想得到比“更高级、更简洁”更具体的判断。

它把审美工程、交互工程和 AI 产品心理学合成九项检查，覆盖页面主角、层级、生成状态、不确定性、拟人化、等待感知、心智模型和 AI 标签的价值感。

- [独立介绍、30 秒提示与 Demo](docs/ai-product-ux-review.md)
- [Skill 本体](skills/ai-product-ux-review/SKILL.md)
- [完整目录](skills/ai-product-ux-review/)

### 4. Vibe Coding 项目规则生成

适合：你正让 AI 参与真实项目开发，需要明确什么时候停、什么时候问、哪些文件不能动、怎样才算真的做完。

它根据技术栈、项目阶段、数据风险、真实用户、部署权限、付费 / 账号和硬件风险，生成项目专用规则；默认只给规则草案，不会擅自修改仓库。

- [独立介绍、30 秒提示与 Demo](docs/vibe-coding-rules-generator.md)
- [Skill 本体](skills/vibe-coding-rules-generator/SKILL.md)
- [完整目录](skills/vibe-coding-rules-generator/)

### 5. OPC 上线资产与合规检查

适合：你准备以个人或小团队上线产品，需要先把名称、域名、代码、内容、合作方、核心诀窍和主体关系理清楚。

它用商标、域名、软件著作权、著作权、专利和商业秘密六把“锁”做风险识别与材料准备。它不冒充正式法律意见；涉及法规、备案、费用和平台规则时，必须运行时核验官方来源并带 `verified_at`。

- [独立介绍、30 秒提示与 Demo](docs/opc-launch-ip-check.md)
- [Skill 本体](skills/opc-launch-ip-check/SKILL.md)
- [完整目录](skills/opc-launch-ip-check/)

## 怎么判断该用哪一个

- “这套 Agent 架构会不会失控？” → `agent-architecture-review`
- “这个量级应该用什么模型，一个月多少钱？” → `ai-model-cost-selector`
- “这个 AI 产品为什么看着还行、用起来却不对？” → `ai-product-ux-review`
- “这个项目应该给 AI 定哪些开发规矩？” → `vibe-coding-rules-generator`
- “产品准备上线，名称、代码、内容和核心诀窍怎么保护？” → `opc-launch-ip-check`

一个请求同时需要两种交付物时，可以同时调用两个 Skill；它们仍分别工作，不经过总路由。

## 来源与许可

本项目改编自洛小山主讲、小山学堂 / 米羊科技出品的[《小山学堂 · AI 从入门到精通》](https://xueai.app/slides/home.html)。原始开源项目：[itshen/learn-ai](https://github.com/itshen/learn-ai)。

本仓库将课程主题重新整理为五个 Agent 工作流，不替代原课程。本改编版本整理于 2026-08-11。Copyright © 2026 洛小山 · Miyang Tech (Zhuhai Hengqin) Co., Ltd.，依据 [GNU AGPL v3.0](LICENSE) 授权。
