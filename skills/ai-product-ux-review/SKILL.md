---
name: ai-product-ux-review
description: Run a distinctive AI product health check that combines aesthetic engineering, interaction engineering, and AI product psychology. Use for screenshots, prototypes, live URLs, UX copy, or product flows when checking the page's focal point, whitespace and hierarchy, state completeness, visibility of AI work, uncertainty, anthropomorphism, perceived waiting, mental models, and whether AI labeling reduces perceived value. Separate observed evidence from unverified interaction behavior.
---

# AI Product UX Review

Review the product as one experience across visual composition, interaction behavior, and AI-specific psychology. Do not reduce the result to generic taste comments.

## Source and boundary

Adapt this workflow from the aesthetic engineering, interaction engineering, and AI product psychology themes in [小山学堂 · AI 从入门到精通](https://xueai.app/slides/home.html), created by 洛小山 / 米羊科技. This adaptation was prepared on 2026-08-11. Keep the bundled AGPL-3.0 license and attribution when redistributing it.

Default to read-only review. Do not edit designs, code, live products, accounts, or analytics unless implementation is explicitly requested.

## Establish evidence

Accept screenshots, prototypes, live URLs, UX copy, or product flows. Identify the target user, main task, intended value, and evidence level:

- static screenshot or design;
- clickable prototype;
- local build;
- deployed flow;
- observed user behavior or research.

Do not infer a complete interaction from a static screen. Mark invisible behavior as `未验证` and state what artifact or test would verify it.

## Run all nine checks

Mark every item `通过`, `风险`, `未验证`, or `不适用`; do not silently skip one.

1. **页面有没有明确主角** — identify the primary user task, first visual anchor, main action, and competing elements.
2. **留白、层级、一致性是否成立** — inspect breathing room, grouping, reading order, emphasis, component rhythm, copy, visual tokens, and state consistency.
3. **加载、生成、失败、取消状态是否齐全** — trace idle, input, validation, submission, loading, generation, partial result, success, failure, timeout, cancel, and retry as applicable.
4. **用户是否知道 AI 正在做什么** — check truthful acknowledgement, current stage, available action, progress, and external effects.
5. **结果的不确定性如何呈现** — distinguish uncertainty, incomplete evidence, stale data, low confidence, and system failure without hiding them in generic disclaimers.
6. **是否存在过度拟人化** — flag fake emotion, false understanding, invented intent, dependency-inducing language, or personality that obscures system limits and responsibility.
7. **等待时间如何被感知** — inspect immediate feedback, useful progress, streaming, cancellation, preserved input, and whether the wait feels purposeful rather than blocked.
8. **用户是否容易形成正确心智模型** — verify users can predict what the AI knows, remembers, can do, cannot do, and when confirmation is required.
9. **AI 标签是否反而降低价值感** — check whether technology labels overshadow the user's outcome, make the product look like a thin wrapper, or reduce willingness to pay; preserve the AI label only when it explains a meaningful capability or risk.

For a complete product health check, read [references/health-check.md](references/health-check.md). Use the deeper state and psychology prompts only when supported by the supplied evidence.

## Report

Return:

1. **极简结论** — the product's strongest point, biggest user cost, and evidence boundary.
2. **三层体检** — separate findings for `审美工程`, `交互工程`, and `AI 产品心理学`.
3. **九项检查表** — status, evidence, user consequence, and recommended action for every required item.
4. **优先级问题** — use `P0` only for blocking, dangerous, irreversible, or trust-breaking failures.
5. **保留什么** — protect working hierarchy, interaction, or trust mechanisms.
6. **最小改进动作** — the smallest change and how to verify it with the next artifact or user test.

Use concrete visible or observed evidence. Separate findings from design suggestions and static inspection from real end-to-end behavior.
