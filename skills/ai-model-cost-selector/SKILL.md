---
name: ai-model-cost-selector
description: Select an AI model tier and diagnose token and multimodal costs from request volume, average input and output tokens, context length, image usage, latency and quality targets, and budget. Use for monthly cost ranges, cost-driver analysis, caching, compression, routing, fallback decisions, and identifying over-engineering. Verify current model capabilities and prices from official sources at runtime and report source URLs with verified_at; never rely on embedded prices.
---

# AI Model Cost Selector

Select the lowest model tier that satisfies the workload, then calculate a defensible monthly cost range. Do not choose a model from reputation or price alone.

## Source and boundary

Adapt this workflow from the model-selection and Token cost-engineering themes in [小山学堂 · AI 从入门到精通](https://xueai.app/slides/home.html), created by 洛小山 / 米羊科技. This adaptation was prepared on 2026-08-11. Keep the bundled AGPL-3.0 license and attribution when redistributing it.

Never store or reuse provider prices, model availability, context limits, or image-pricing rules as permanent Skill knowledge. Verify them during every run.

## Collect the workload

Collect or visibly estimate:

- request volume and period; normalize it to monthly requests;
- average input tokens;
- average output tokens;
- required context length;
- whether images are included, plus count, size, quality, or provider billing unit when relevant;
- latency requirement;
- minimum acceptable quality;
- monthly budget and currency.

Also collect cacheable-prefix ratio, retries, fallback rate, tool calls, and model calls per user request when they materially affect the bill.

Distinguish required context capacity from actual billed input. A model may need a long context window while typical requests remain short. If data is missing, construct labelled low/base/high scenarios; never hide assumptions inside one precise number.

## Verify live model facts before calculating

Before naming a current model or producing a monetary estimate:

1. Open the provider's official pricing page.
2. Open the provider's official model or capability documentation.
3. Verify availability, context capacity, vision support, latency or service tier, input price, cached-input rule, output price, and image rule relevant to this workload.
4. Record, for every candidate:
   - `source_url`;
   - `verified_at` as ISO 8601 with timezone, representing when the source was actually checked;
   - currency and billing unit;
   - region, account, batch, priority, or tier caveats.

Search summaries, blogs, leaderboards, and aggregators may provide leads but are not pricing evidence. If an official source is unavailable, account-specific, or contradictory, mark the candidate `unverified` and do not produce a pseudo-precise monthly price. Provide the formula or explicitly use a user-provided price instead.

If currency conversion is needed, verify the exchange-rate source separately and give its own `verified_at`.

## Select the model tier

Filter candidates in this order:

1. required context and modality;
2. minimum task quality;
3. latency and regional constraints;
4. privacy or deployment constraints;
5. budget and operational resilience.

Name a suitable capability tier before recommending a specific current model. A higher tier is justified only by measured quality, context, modality, latency, or reliability needs. Use a small task-specific evaluation set when quality differences could change the recommendation.

## Calculate the monthly range

Read [references/cost-method.md](references/cost-method.md) when calculating a production estimate. Use `scripts/cost_calculator.py` only after supplying prices verified during this run. The calculator contains no model catalog or provider price defaults.

Calculate low/base/high scenarios and include:

- uncached input;
- cached input;
- output;
- image or multimodal charges;
- model calls per user request;
- retries and fallback activation;
- fixed per-request or tool costs.

Expand an Agent request into router, planner, tool loop, generator, and evaluator calls when those steps exist. The visible answer is not the whole bill.

## Judge optimizations

Evaluate caching, compression, routing, and degradation against the actual dominant cost. For each proposal, state expected impact, implementation and maintenance effort, prerequisite evidence, quality or latency risk, and one of:

- `现在做`;
- `收集数据后做`;
- `暂不做`.

Call an optimization over-engineering when volume or savings are small, the presumed repeated prefix or hard tail is unmeasured, quality has not been evaluated, or the operational system would cost more than it saves.

## Return this structure

1. **适合的模型层级** — capability tier, current candidates, and why they pass the constraints.
2. **月成本区间** — low/base/high with assumptions and budget comparison.
3. **成本主要花在哪里** — input, cached input, output, images, retries, fallback, and hidden Agent steps.
4. **缓存、压缩、路由、降级建议** — quantified where evidence allows.
5. **哪些优化值得做** — impact, effort, evidence, and validation.
6. **哪些属于过度工程** — rejected work and why.
7. **价格核验** — candidate, official `source_url`, `verified_at`, currency, billing unit, and caveats.

Do not claim that a cost calculation proves task quality. Separate provider claims, benchmarks, local evaluations, production measurements, and estimates.
