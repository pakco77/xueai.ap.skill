---
name: agent-architecture-review
description: Review Agent or AI product architecture from a PRD, architecture diagram, code directory or repository, or product flow. Use when assessing context overflow, tool boundaries, memory necessity, single-versus-multi-Agent design, permissions and approvals, evaluation plans, long-running recovery, or whether a prompt has evolved into a reliable Harness. Return an evidence-backed minimal repair review; do not edit unless explicitly requested.
---

# Agent Architecture Review

Review the actual Agent or AI product architecture and find the smallest repair that makes it reliable. Treat a model prompt as one component of a system, not the whole system.

## Source and boundary

Adapt this workflow from the Agent engineering, Harness, context engineering, and self-improvement themes in [小山学堂 · AI 从入门到精通](https://xueai.app/slides/home.html), created by 洛小山 / 米羊科技. Use it as an independent architecture-review procedure. This adaptation was prepared on 2026-08-11. Keep the bundled AGPL-3.0 license and attribution when redistributing it.

Default to read-only review. Do not change code, diagrams, PRDs, configuration, or production systems unless the user explicitly requests implementation.

## Accept the evidence

Accept any one or more of:

- PRD;
- architecture diagram;
- code directory or repository;
- product flow.

Do not require all four. Extract the product goal, user-critical path, real execution chain, data handled, external effects, and existing model/context/tool/state/approval/evaluation/recovery mechanisms. Mark absent evidence as `未验证`; do not treat a design claim as implemented behavior.

Trace the system when possible:

`trigger → orchestration → model → context → tools → state or memory → external effect → observation → recovery`

## Review eight gates

Assess every gate as `通过`, `风险`, `未验证`, or `不适用`. For each risk, include evidence, failure mode, and the smallest repair.

1. **上下文是否会溢出** — inventory context by stage; estimate average and p95 growth from history, retrieval, and tool output; inspect truncation, compression, summarization, retrieval, and safety margin.
2. **工具边界是否清楚** — inspect schemas, validation, allowlists, side effects, timeouts, cancellation, retries, idempotency, secrets, and observability.
3. **记忆是否真的需要** — require a concrete cross-step, cross-session, or cross-process need; otherwise prefer current context or project files. If memory is justified, define scope, source of truth, correction, deletion, and expiry.
4. **单 Agent 还是多 Agent** — derive Agent count from real concurrency, context or permission isolation, independent evaluation, or independent failure boundaries. Otherwise prefer one Agent with explicit phases.
5. **权限和审批是否合理** — enforce least privilege and action-time confirmation for external writes, deployment, publishing, payment, messages, accounts, hardware, and destructive changes.
6. **有没有评测方案** — require representative tasks, failure taxonomy, separate model/tool/latency/cost/user-outcome metrics, regression gates, and failure-path tests.
7. **长运行任务如何恢复** — inspect durable checkpoints, serializable state, bounded retries, idempotent replay, cancellation, partial-result handling, and restart/resume tests across session or process replacement.
8. **Prompt 是否已经演化成 Harness** — classify the system as `Prompt 足够`, `Prompt 过载`, `部分 Harness`, or `已有 Harness`. Look for structured contracts, context assembly, tool governance, permissions, durable state, validation, evaluations, observability, and recovery outside the prompt.

For a full architecture review, read [references/review-checklist.md](references/review-checklist.md) before forming the verdict. For one narrow conceptual question, use only the relevant gate.

## Prefer the smallest architecture

Stop at the first layer that satisfies the requirement:

1. deterministic code or a native platform feature;
2. one structured model call;
3. one Agent with bounded tools;
4. a durable workflow with checkpoints;
5. multiple Agents only when independently owned work or isolation proves a net benefit.

For build-time Coding Agents, inspect the dependency graph, shared schemas and contracts, file ownership, merge boundaries, and CI. Derive concurrency from independently committable units rather than a requested headcount.

## Return this exact structure

1. **极简结论** — 3 to 6 directly forwardable lines; include overall risk and the Prompt/Harness classification.
2. **架构风险** — prioritized risks with evidence, missing evidence, failure mode, and severity.
3. **保留什么** — existing choices that already reduce risk or complexity.
4. **改什么** — concrete changes only.
5. **为什么** — connect every proposed change to a demonstrated risk or requirement.
6. **最小修复动作** — the smallest reversible action and the check that would prove it worked.

Do not add a generic architecture essay after these sections. Separate source inspection, local tests, installed behavior, deployment, and real end-to-end evidence.
