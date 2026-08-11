# AI product health-check reference

Load this reference for a complete product review.

## Aesthetic engineering

### Focal point

- State the single primary user job on the page.
- Identify the first visual anchor and the dominant action.
- Check whether navigation, decoration, AI branding, secondary cards, or promotional copy competes with that job.
- Confirm the strongest visual weight matches the most valuable next action.

### Whitespace, hierarchy, and consistency

- Check grouping and separation, not the amount of empty space in isolation.
- Verify reading order, heading levels, emphasis, density, and progressive disclosure.
- Compare component spacing, radius, typography, color roles, icon style, copy tone, and interactive states.
- Treat intentional contrast as valid; flag accidental inconsistency that changes meaning or increases learning cost.

## Interaction engineering

### State coverage

Inspect the relevant path:

`idle → input → validation → submission → loading → generation → partial result → success`

Also inspect `empty`, `failure`, `timeout`, `cancel`, `retry`, `offline`, `permission denied`, `rate limited`, `unsafe request`, and `stale result` when applicable.

For each state ask:

- What does the user think is happening?
- What can the user do now?
- Is progress tied to real work?
- Can the user cancel, correct, retry, or recover without losing input?
- Are completed external actions separated from suggestions or planned actions?

### Perceived waiting

- Acknowledge input immediately.
- Show only real stage changes; avoid decorative progress claims.
- Stream partial output only when it is safe and useful.
- Make cancellation available for costly or slow work.
- Preserve input and completed work across failure and retry.
- Use time estimates only when the system can support them.

## AI product psychology

### Uncertainty

- Place source, confidence, missing evidence, and stale-data signals near the affected result.
- Distinguish uncertainty from technical failure.
- Avoid generic disclaimers that make every answer equally suspect.
- Offer a verification or correction path for consequential results.

### Anthropomorphism

- Flag claims of feeling, intention, understanding, certainty, or loyalty that exceed actual capability.
- Check whether a persona clarifies the interaction or pressures the user emotionally.
- Preserve responsibility boundaries for professional, financial, legal, medical, or external actions.
- Do not confuse friendly language with a claim of human-like agency.

### Mental model

- Can users predict what data the AI sees?
- Can users understand what it remembers and edit or delete that memory?
- Can users distinguish generation, retrieval, automation, and completed external actions?
- Are permissions and confirmation points explained when relevant?
- Does the UI reveal limitations at the point of decision rather than after failure?

### AI-label value

- Identify the user outcome that deserves emphasis before the implementation technology.
- Check whether repeated AI badges lower perceived craftsmanship or imply a commodity wrapper.
- Keep an AI label when users need it to understand variability, provenance, safety, capability, or pricing.
- Prefer outcome language when the AI mechanism is not itself the value.

## Evidence-safe issue table

| Priority | Layer | Check | Evidence | Status | User consequence | Keep/change | Verification |
|---|---|---|---|---|---|---|---|

Do not mark an interaction `通过` from a screenshot alone. Use `未验证` and request a state screenshot, recording, prototype, deployed path, accessibility tree, or observed user session as appropriate.
