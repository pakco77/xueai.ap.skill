# Agent architecture review checklist

Load this checklist for a complete PRD, architecture, repository, or product-flow review.

## Evidence map

| Area | Claimed design | Implemented evidence | Runtime evidence | Status |
|---|---|---|---|---|
| Context | | | | |
| Tools | | | | |
| Memory/state | | | | |
| Orchestration | | | | |
| Permissions | | | | |
| Evaluation | | | | |
| Recovery | | | | |
| Harness | | | | |

Never promote a claim to a stronger evidence level without proof.

## 1. Context overflow

- List required context separately for routing, planning, tool use, generation, and evaluation.
- Estimate average and p95 input size, not only the model's advertised maximum window.
- Account for conversation history, retrieved documents, tool output, images, schemas, and repeated system instructions.
- Identify unbounded accumulation and recursive summaries.
- Inspect truncation order and what critical facts could disappear.
- Check whether compression or retrieval has quality tests.
- Preserve a safety margin for output and tool schemas.

## 2. Tool boundaries

- Prefer narrow schemas and explicit allowlists.
- Validate all external inputs and tool outputs at trust boundaries.
- Separate reads from external writes and irreversible effects.
- Define timeout, cancellation, retry, and idempotency behavior.
- Re-check target and payload at the moment of consequential action.
- Keep secrets out of prompts, logs, traces, and returned tool content.
- Make each tool action reconstructable from an audit trail.

## 3. Memory necessity

- Name the information that must survive a step, session, process, or device change.
- Reject memory when current context or a normal project file is sufficient.
- Define task, project, and user scopes separately.
- Identify the source of truth and conflict resolution.
- Provide correction, deletion, retention, and expiry behavior.
- Test restoration after the model or process is replaced.

## 4. Single versus multiple Agents

Use multiple Agents only when at least one is demonstrated:

- independent work can run concurrently;
- contexts or permissions must be isolated;
- an evaluator must be independent from the producer;
- failures and retries need separate ownership.

Count merge, coordination, duplicated context, evaluation, and recovery cost. Otherwise use one Agent with explicit phases.

## 5. Permissions and approvals

- Apply least privilege per tool and role.
- Require action-time confirmation for deployment, publishing, payment, messages, accounts, hardware, destructive writes, and sensitive-data disclosure.
- Preview the exact target, payload, scope, and expected effect.
- Make denial, timeout, and partial failure recoverable.
- Do not treat an early blanket approval as approval for a later changed action.

## 6. Evaluation

- Use representative tasks and a named failure taxonomy.
- Measure model quality, tool correctness, latency, cost, and user outcome separately.
- Define regression gates before changing prompts, models, tools, or context policy.
- Test context truncation, tool failure, permission denial, retry exhaustion, and recovery.
- Confirm production checks exercise the same path users depend on.

## 7. Long-running recovery

- Persist a versioned, serializable checkpoint outside the model session.
- Separate completed effects from planned effects.
- Use bounded retries and idempotency keys.
- Support cancel, redirect, and resume.
- Do not report partial artifacts as completion.
- Run a restart test that replaces the session or process and resumes from the checkpoint.

## 8. Prompt to Harness

Classify:

- `Prompt 足够`: one-shot, no tools or external effects, easy to verify.
- `Prompt 过载`: a large prompt is patching repeated failures that should be enforced elsewhere.
- `部分 Harness`: some contracts, tools, state, or evaluation exist, but reliability still depends on prose.
- `已有 Harness`: contracts, context assembly, tools, permissions, state, validation, evaluation, observability, and recovery are enforced by the runtime.

Identify the smallest missing Harness layer. Do not recommend a platform rewrite when one schema, checkpoint, permission gate, or evaluator closes the demonstrated gap.
