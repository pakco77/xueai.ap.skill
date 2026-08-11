---
name: vibe-coding-rules-generator
description: Generate the smallest project-specific Vibe Coding rules from the technology stack, project stage, data risk, presence of real users, deployment permission, and involvement of payments, real accounts, or hardware. Use when creating or refining AGENTS.md, CLAUDE.md, or repository instructions that define pre-action checkpoints, confirmation gates, decision retention, full verification, context-drift prevention, protected files, and the minimum test. Do not edit rule files unless implementation is explicitly requested.
---

# Vibe Coding Rules Generator

Generate only the rules this project needs to prevent costly Agent mistakes. Do not output a generic best-practices wall of text.

## Source and boundary

Adapt this workflow from the Vibe Coding, context engineering, collaboration, and engineering-practice themes in [小山学堂 · AI 从入门到精通](https://xueai.app/slides/home.html), created by 洛小山 / 米羊科技. This adaptation was prepared on 2026-08-11. Keep the bundled AGPL-3.0 license and attribution when redistributing it.

Return a proposed rule block by default. Do not create or modify `AGENTS.md`, `CLAUDE.md`, or other repository files unless the user explicitly asks for implementation.

## Collect the project risk profile

Collect or infer from repository evidence:

1. **技术栈** — languages, frameworks, package manager, storage, CI, deployment, and test commands.
2. **项目阶段** — concept, local prototype, internal test, public beta, or production.
3. **数据风险** — no data, synthetic data, user data, sensitive data, secrets, or irreversible data.
4. **是否有真实用户** — none, internal, limited external, or production users.
5. **是否允许部署** — forbidden, allowed, or confirm every deployment.
6. **是否涉及付费或真实账户** — payments, credits, subscriptions, credentials, messages, publishing, or real-account mutation.
7. **是否涉及硬件** — device control, calibration, motion, safety limits, firmware, or irreversible physical effects.

Mark unknown high-risk inputs and ask one focused question when the answer would materially change the rule set. For low-risk unknowns, proceed with a labelled conservative assumption.

Inspect existing rules, README, scripts, CI, code conventions, nested instructions, and dirty work when a repository is available. Reuse an existing source of truth instead of creating overlapping instruction files.

## Scale rules to risk

- For a local prototype with synthetic data, no users, and no external effects, keep the rules extremely light.
- Increase confirmation, preservation, and regression requirements when real users, sensitive data, deployment, payments, accounts, or hardware are present.
- Prefer a test, schema, permission, or platform control over prose when it can enforce the boundary directly.
- Do not invent a fixed rule count. Stop when every demonstrated high-cost failure has one clear guardrail.

For the risk-to-rule mapping and anti-bloat test, read [references/rule-generator.md](references/rule-generator.md).

## Generate seven rule groups

1. **AI 动手前需要哪些断点** — define checkpoints before starting, before changing shared or irreversible state, before external action, and before claiming completion.
2. **哪些操作需要确认** — name project-specific deployment, payment, account, messaging, publishing, destructive, sensitive-data, and hardware actions that require action-time approval.
3. **如何保留决策** — identify the existing decision log, issue, ADR, handoff, or project file; record decision, reason, owner, evidence, and next condition without making chat history the only source.
4. **如何验证完整实现** — define the evidence chain appropriate to this project, such as source inspection, build, focused test, integration, installed artifact, deployment, and real end-to-end behavior.
5. **如何避免上下文漂移** — fix the real project root, current scope, source of truth, protected assumptions, and when the Agent must re-read instructions or hand off resumable state.
6. **哪些文件不能随意改** — identify migrations, lockfiles, generated code, secrets, production configuration, hardware limits, source assets, signed artifacts, or user-owned dirty files from actual project evidence.
7. **最小测试应该是什么** — name the smallest runnable command or observation, expected result, and the failure it catches.

## Write operational rules

Use this shape where useful:

```text
When <project-specific trigger>, do <observable action>.
Do not <high-cost failure>.
Completion requires <evidence>.
```

Delete a rule when it repeats a platform default, cannot be checked, addresses no demonstrated risk, or is better enforced by code or permissions.

## Return

1. **项目风险画像** — supplied facts, inferred facts, and unresolved high-risk inputs.
2. **最小规则集** — a ready-to-paste rule block grouped only where grouping helps scanning.
3. **放在哪里** — the one source-of-truth file and scope; avoid duplicate rule files.
4. **为什么保留这些规则** — map each rule to an actual project risk.
5. **最小验证** — prove the target host discovers the rules and the project still passes its smallest relevant test.

If existing rules already cover the demonstrated risks, recommend no new rule. Preserve unrelated instructions and user changes when implementation is later authorized.
