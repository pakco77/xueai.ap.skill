# Runtime cost method

Use this reference only after current model capabilities and prices have been verified from official provider sources.

## Verification record

Record one row per candidate and price regime:

| Field | Required content |
|---|---|
| candidate | Current official model identifier |
| capability tier | Workload-relative tier, not a permanent ranking |
| source_url | Direct official pricing or model-document URL |
| verified_at | ISO 8601 timestamp with timezone for this verification |
| currency | Billing currency |
| billing unit | Per token, per million tokens, per image, per second, or other official unit |
| input rule | Normal input price and threshold rules |
| cached-input rule | Direct cached price or official discount rule |
| output rule | Output price and threshold rules |
| image rule | Image tokens, units, size, quality, or flat charge |
| caveats | Region, account, batch, priority, commitment, tax, or tier conditions |

If any required price is unverified, do not turn the row into a precise monetary forecast.

## Normalize the workload

Convert request volume into monthly user requests. Keep separate:

- user requests;
- model calls per request;
- expected retry multiplier;
- fallback activation rate;
- input and output tokens per model call;
- image cost per user request or model call, according to the official rule.

Required context length is a capability filter. Do not substitute it for average billed input tokens.

## Formula

Let:

- `R` = monthly user requests;
- `C` = model calls per user request;
- `T` = retry rate expressed as additional calls per base call;
- `I` = average input tokens per model call;
- `O` = average output tokens per model call;
- `H` = fraction of input tokens billed at the cached-input rate;
- `Pi` = normal input price per token unit;
- `Pc` = cached-input price per token unit;
- `Po` = output price per token unit;
- `M` = official token billing unit;
- `V` = image or multimodal cost per user request;
- `F` = other fixed cost per user request.

```text
billable model calls = R × C × (1 + T)
normal input cost    = calls × I × (1 - H) / M × Pi
cached input cost    = calls × I × H / M × Pc
output cost          = calls × O / M × Po
multimodal cost      = R × V
fixed cost           = R × F
monthly total        = sum of all components
```

Model fallbacks with different prices should be calculated as separate rows weighted by activation rate, then added.

## Agent call expansion

Before calculating, map one user action:

| Step | Expected calls | Input tokens | Output tokens | Retry/fallback | Candidate |
|---|---:|---:|---:|---:|---|
| Router | | | | | |
| Planner | | | | | |
| Tool loop | | | | | |
| Generator | | | | | |
| Evaluator | | | | | |

Remove rows that do not exist in the real product. Do not invent an Agent loop to make the cost model look sophisticated.

## Low, base, and high scenarios

Vary the uncertain variables that can change the decision:

- request volume;
- input and output length;
- model calls and retry rate;
- image usage;
- cache hit rate;
- hard-tail or fallback activation.

Keep official unit prices fixed to the same verified pricing regime unless a published threshold changes them.

## Worth doing versus over-engineering

Recommend an optimization only when it targets a measured cost driver, expected savings exceed implementation and maintenance cost, quality and latency remain acceptable, and success can be measured.

Typical over-engineering signals:

- complex routing at low volume;
- caching without a repeated stable prefix;
- compression designed for a theoretical maximum context that production rarely reaches;
- universal downgrade before task-quality evaluation;
- a persistent multi-Agent cost-control layer for a tiny hard tail.
