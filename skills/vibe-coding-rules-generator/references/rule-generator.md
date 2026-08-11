# Project risk to rule generator

Load this reference when turning a project description or repository into a rule set.

## Input normalization

| Input | Low-risk state | Higher-risk state | Rule effect |
|---|---|---|---|
| Project stage | concept or local prototype | public beta or production | require stronger regression, rollback, and completion evidence |
| Data | synthetic or disposable | personal, sensitive, secret, or irreversible | restrict access, copying, logging, and destructive operations |
| Users | none | real external users | protect compatibility, migration, accessibility, and recovery |
| Deployment | forbidden | allowed with confirmation | define exact deploy target, approval, rollback, and live verification |
| Payment/account | none | real money, credits, credentials, messages, or publishing | require action-time target and payload confirmation |
| Hardware | none | moving, heating, cutting, flashing, or safety-critical device | require calibration, limits, dry run, supervision, and physical stop conditions |

Infer the technology stack and available commands from repository files when possible. Ask instead of guessing when a wrong command could change data or external state.

## Pre-action checkpoints

Select only applicable checkpoints:

- confirm the real project root and nearest instructions;
- inspect current state and unrelated dirty work;
- trace the real flow and shared callers before changing code;
- identify protected data, files, accounts, hardware, and deployment targets;
- confirm a consequential external action at execution time;
- run the smallest relevant check before claiming completion;
- record a resumable handoff only when verified work remains.

## Confirmation gates

Require explicit action-time approval for applicable operations:

- deploy, publish, send, purchase, subscribe, or spend credits;
- change a real account, credential, permission, or customer record;
- delete, overwrite, migrate, reset, or rotate material data;
- run unsupervised hardware motion, heating, cutting, calibration, or firmware changes;
- accept external terms or submit legal or regulatory material.

Read-only inspection and reversible local edits inside the authorized project do not need artificial confirmation.

## Decision retention

Reuse the project's existing issue tracker, ADR, task note, `NOW.md`, `HANDOFF.md`, or equivalent. Store only decisions needed to continue:

- decision and scope;
- reason and rejected alternative;
- evidence or test;
- owner or authorization;
- next condition or rollback point.

Do not create a new memory system when one small project file is sufficient.

## Full verification ladder

Choose the levels the user outcome actually requires:

1. source or configuration inspection;
2. focused local test;
3. build or integration test;
4. installed artifact check;
5. deployment response and executed behavior;
6. real participant-side or hardware behavior.

Never report a lower level as proof of a higher one.

## Protected-file discovery

Look for project-specific evidence before naming protected paths:

- migrations and production data schemas;
- package or dependency lockfiles;
- generated code and vendored assets;
- secrets and signing material;
- production configuration and deployment manifests;
- hardware limits, calibration, or firmware files;
- original media or design source assets;
- user-owned dirty files outside the task.

Protect only what the project actually contains.

## Minimum-test design

The minimum test should fail when the requested behavior breaks and be as small as possible without becoming irrelevant. Name:

- command or observation;
- required environment;
- expected result;
- failure caught;
- evidence level it does and does not prove.

## Anti-bloat test

Delete or merge a proposed rule when:

- it merely says “be careful” or “follow best practices”;
- the host already guarantees it;
- it cannot be observed or enforced;
- it addresses a one-time incident rather than a recurring high-cost risk;
- it conflicts with a narrower instruction closer to the work;
- a script, schema, test, permission, or native setting is smaller and stronger.
