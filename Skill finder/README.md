# Skill Finder

Evaluations of third-party Claude Code skills against Sai's existing setup.

Evaluated: 2026-07-28.

## Contents

| File | What it covers |
|---|---|
| `i-have-adhd-evaluation.md` | ayghri/i-have-adhd. Install decision. |
| `no-ai-slop-evaluation.md` | petergyang/no-ai-slop. What it actually is. |
| `blocklist-gap-analysis.md` | Head-to-head: our `ai-slop-blocklist.md` vs Peter Yang's skill. |
| `proposed-blocklist-patch.md` | Drop-in text to close the gaps. Not applied. |

## Verdicts

**i-have-adhd: install it, expect a modest gain.** MIT, 12.3k stars, no model-invocation (manual `/i-have-adhd` only), so it cannot fire during content work by accident. Roughly half its ten rules restate what Claude Code's system prompt already enforces. The four that genuinely add something are state restatement across turns, concrete time estimates, one bounded next action, and visible wins. Low risk, real but bounded benefit. Details and the conflict check in `i-have-adhd-evaluation.md`.

**no-ai-slop: do not install as-is, harvest it instead.** It is a general-purpose prose editor for essays and newsletters. Installing it alongside `linkedin-content` and `nullhypeai` creates two competing authorities on the same question, and its em-dash rule (1-2 are fine in longer drafts) directly contradicts the house rule (zero). The value is in its pattern taxonomy and its enforcement architecture, both of which can be lifted into the existing blocklist.

**How our content held up.** Better than expected on taxonomy, worse on enforcement.

Our blocklist covers roughly 60% of Yang's pattern categories and adds about fifteen he has no coverage of at all, including the entire comment/reply category and every platform-native formatting tell. On genre-level bans (the manufactured-mentorship anecdote, the fake-metric-plus-framework post) our file operates a level above his, which is the harder and more useful rule to write.

Three real weaknesses:

1. **Eight missing pattern categories**, and they are the ones that hit an analyst voice hardest: colon reveals, trailing `-ing` clauses, importance puffery, weasel attribution, synonym cycling, negative listing, summary-recap endings, robotic rhythm. Weasel attribution is the worst omission given the whole strategy rests on data-backed claims.
2. **No voice-preservation counterweight.** Our file is purely subtractive. Yang spends half his skill on what not to touch. Applied hard, a pure blocklist produces uniformly clipped evidence-dense prose, which is its own recognizable tell.
3. **No verification loop.** Our self-check is a 7-item list with no instruction to re-run after fixing. Yang's `eval.md` is 20+ binary checks with an explicit fix-and-recheck loop.

Plus one maintenance bug: the two copies of `ai-slop-blocklist.md` have drifted (51 lines vs 74), and the X version tells the model to avoid sounding like "the median LinkedIn post."

Full breakdown in `blocklist-gap-analysis.md`. Ready-to-paste fixes in `proposed-blocklist-patch.md`.

## Sources

- [github.com/ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
- [github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- [Peter Yang's launch post on X](https://x.com/petergyang/status/2079943830024188105)
- [Peter Yang's writeup on Creator Economy](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns)
