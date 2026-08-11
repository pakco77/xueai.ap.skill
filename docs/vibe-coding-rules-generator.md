# Vibe Coding Rules Generator｜Vibe Coding 规则生成器

**一句话价值：** 从真实项目风险生成最小、可执行的 Agent 规则，避免用一堵“最佳实践”文字墙拖慢开发。

- [查看 Skill 原文](../skills/vibe-coding-rules-generator/SKILL.md)
- [浏览完整 Skill 目录](../skills/vibe-coding-rules-generator/)

## 服务场景

- 新项目需要一份真正贴合技术栈与阶段的 `AGENTS.md` 或 `CLAUDE.md`。
- 现有规则太长、重复、互相冲突，Agent 仍会误部署、误改文件或错误宣称完成。
- 项目从原型进入公测或生产，需要补上真实用户、数据、付款与回滚边界。
- 多个 Agent 协作时需要固定项目根目录、事实源、交接条件与最低验证标准。
- 涉及真实账户、发布、消息、付费或硬件，需要明确“执行当下再确认”的闸门。

## 30 秒开始

Hermes / Claude Code：

```text
/vibe-coding-rules-generator 请读取当前仓库，给我一份最小规则提案。项目是公开 Beta；有真实用户和 Supabase 数据；每次 Vercel 部署、Stripe 操作都要当下确认。默认不要改任何规则文件。
```

Codex：

```text
$vibe-coding-rules-generator 审查现有 AGENTS.md，保留已有有效规则，只输出建议删改后的 ready-to-paste 规则块和最小验证，不要落盘。
```

## 建议提供的材料

1. 仓库路径、技术栈、包管理器、存储、CI、部署方式和测试命令。
2. 项目阶段：概念、本地原型、内测、公开 Beta 或生产。
3. 数据类型：合成、用户、敏感、密钥或不可逆数据。
4. 用户范围：无用户、内部、有限外部或生产用户。
5. 部署权限：禁止、允许，或每次部署都需确认。
6. 付费与真实账户：款项、点数、订阅、凭据、消息、发布或账户变更。
7. 硬件影响：运动、加热、切割、校准、固件与安全限位。

仓库存在时，Skill 还会读取已有规则、README、脚本、CI、嵌套指令和未提交改动，优先复用现有事实源。

## 生成的七类规则

1. **AI 动手前需要哪些断点**：开工、改共享或不可逆状态、外部操作、宣称完成前分别检查什么。
2. **哪些操作需要确认**：把部署、付款、账户、消息、发布、删除、敏感数据与硬件动作写成项目专用闸门。
3. **如何保留决策**：在现有 issue、ADR、任务说明或交接文件中保留决策、理由、证据、授权人与下一条件。
4. **如何验证完整实现**：明确源码、局部测试、构建、安装产物、部署响应与真实端到端行为的证据链。
5. **如何避免上下文漂移**：固定真实根目录、当前范围、事实源、受保护假设与重读/交接时机。
6. **哪些文件不能随意改**：只根据仓库证据保护迁移、锁文件、生成代码、密钥、生产配置、校准数据和用户脏文件。
7. **最小测试应该是什么**：写清命令或观察、环境、预期结果、可捕获的失败与不能证明的更高证据层。

风险映射和删减规则见[规则生成参考](../skills/vibe-coding-rules-generator/references/rule-generator.md)。规则尽量使用可观察句式：`When <触发条件>, do <动作>. Do not <高成本失败>. Completion requires <证据>.`

## 默认行为：只读提案

默认输出规则建议，不创建或修改 `AGENTS.md`、`CLAUDE.md` 或其他仓库文件。只有用户明确要求实施后，才会在指定事实源中做最小修改，并保留无关指令与用户已有改动。低风险未知项会用保守假设继续；会实质改变规则的高风险未知项，只追问一个聚焦问题。若现有规则已经覆盖风险，正确结果可以是“不新增规则”。

## 效果与输出

- 区分已提供、从仓库推断和仍未解决信息的**项目风险画像**。
- 可直接粘贴、按需分组的**最小规则集**。
- 唯一规则事实源及适用范围建议，避免多份文件重复漂移。
- 每条规则对应的真实失败成本，而不是抽象口号。
- 主机能发现规则、项目仍通过最小检查的验证方法。

## Demo

**输入：**

> Next.js + Supabase + Stripe 的公开 Beta，已有 80 位用户。生产部署走 Vercel，数据库迁移不可回退；仓库有 AGENTS.md、未提交的设计文件，`package.json` 已提供 `npm test -- checkout`。请只输出规则提案。

**输出节选：**

> **风险画像：** 真实用户、生产数据、支付与生产部署均为高影响；未提交设计文件属于用户资产，不在本次范围。
>
> ```text
> Before editing, confirm the real repository root, nearest AGENTS.md, task scope, and unrelated dirty files.
> Do not edit user-owned dirty design files or production migrations outside the authorized scope.
> Before each Vercel production deploy or Stripe/account mutation, show the exact target and payload and obtain action-time confirmation.
> Completion requires the focused test and build; a successful build does not prove production deployment or a real checkout.
> ```
>
> **最小测试：** `npm test -- checkout` 捕获结账状态机回归；它不证明 Stripe 真实账户扣款或生产端到端成功。

## 验收标准

- 七类规则都被评估，但没有为了凑数强行新增。
- 每条保留规则都对应具体风险，并能被观察或执行。
- 不重复平台默认能力，不用“谨慎操作”之类空话。
- 明确确认发生在外部或高影响动作执行当下。
- 不把源码检查、测试、构建、部署和真实行为混成同一层证明。
- 默认没有文件改动；若用户后来授权实施，改动范围唯一且最小。

## 边界

Skill 不替代安全审计、法律判断或硬件现场校准；不会凭空发明受保护路径、测试命令或部署流程。能用测试、schema、权限或平台控制落实的边界，应优先交给这些机制，而不是继续增加规则文本。

## 来源与许可

本 Skill 改编自洛小山主讲、小山学堂 / 米羊科技出品的[《小山学堂 · AI 从入门到精通》](https://xueai.app/slides/home.html)，原始项目为 [itshen/learn-ai](https://github.com/itshen/learn-ai)。本适配版本整理于 2026-08-11；再分发时请保留来源说明与 Skill 目录内的 [GNU AGPL v3.0](../skills/vibe-coding-rules-generator/LICENSE) 许可。
