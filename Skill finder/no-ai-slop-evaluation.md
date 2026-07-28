# no-ai-slop

**Repo:** [github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
**Author:** Peter Yang ([@petergyang](https://x.com/petergyang)), Behind the Craft. Open-sourced 22 July 2026.
**License:** MIT.
**Verdict:** Do not install alongside `linkedin-content` and `nullhypeai`. Harvest its content instead.

This is the skill you were asking about. The "popular creator on X" is Peter Yang. Repo README claims 2,700+ stars and a launch post at 611K impressions, 10K+ saves, 13K+ link clicks. Those are the repo's own numbers, not independently checked.

## What it is

A standalone writing-editor skill in three files:

1. `SKILL.md` (94 lines) — editing principles, banned words, 17 pattern categories, a 6-step workflow.
2. `eval.md` (43 lines) — pass/fail checks the skill runs against its own edit before returning it.
3. `.codex-plugin/plugin.json` plus a build script — packaging for Codex and the ChatGPT plugin directory.

Frontmatter description: *"Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting."* No `disable-model-invocation`, so it can self-trigger on any editing request.

## Two modes

**Edit (default).** You paste a draft. It makes "the minimum effective edit" and returns the full edited draft plus a **What changed** section.

**Detect.** You ask whether something reads as AI. It names each pattern, quotes the offending line, gives a short fix, and stops. It is explicitly forbidden from rewriting, scoring, or claiming AI authorship. The reasoning is the sharpest idea in the skill:

> "AI detectors guess. Named patterns are evidence the user can check."

## The 17 patterns

Binary contrasts · throat-clearing openers · faux-insight setups · colon reveals · superficial analysis (trailing `-ing` clauses) · importance puffery · weasel attribution · fake-strong verbs · synonym cycling · negative listing · dramatic fragmentation · robotic rhythm · rhetorical setups · fake-profound kickers · summary-recap endings · formatting slop · em dashes.

Plus three word lists: 26 banned outright (delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving, and three claim phrases), 11 often-empty adverbs, and 18 often-empty phrases.

## The half nobody quotes

Roughly 40% of the skill is about **what not to touch**, and this is the part worth stealing:

- Notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish first. Keep what is personal to the writer.
- "Make the minimum effective edit. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person after editing."
- Do not make every paragraph equally tidy.
- Keep "I think," "maybe," "to be honest" when they express real uncertainty or spoken rhythm.
- Keep profanity, strong opinions, self-interruptions, honest admissions.
- Front-load only when it improves clarity. Do not force every section into the same point-detail-background shape.
- Preserve the writer's structure and detours unless they are hurting the piece.

Step 2 of the workflow makes this operational: identify the core point and **3-5 voice signals to preserve** before editing anything, held as an internal note.

## The verification loop

`eval.md` is 20+ binary checks in four groups. Workflow steps 4 and 5:

> "4. Make the minimum effective changes, then check the edited draft against `eval.md` yourself.
> 5. If any check fails, fix the draft and run the checks again."

Eval check 1 under "Final read" is deliberate: *"Was the edit checked directly against this file without requiring separate editor and evaluator agents?"* It keeps the loop inside one turn rather than spawning a critic.

## Why not to install it

**Two competing authorities on the same question.** Your `linkedin-content` and `nullhypeai` skills each own the anti-slop judgment for their platform. With `no-ai-slop` installed and model-invocable, an editing request can pull it in and you get conflicting instructions with no arbitration rule.

**A direct rule contradiction.** Yang: "In longer drafts, 1-2 [em dashes] are fine if they clearly beat commas, periods, or parentheses." Your house rule: none, ever, both platforms. Also his banned list includes `transformative`, `robust`, `streamline`, `leverage`, `supercharge` outright, whereas your file treats these as high-suspicion patterns where a cluster, not a single use, triggers a rewrite. Yours is the better rule; his would fire on a legitimate quotation.

**Wrong shape for the target.** The skill is essay- and newsletter-shaped. It has no concept of a hook line, a `…see more` cutoff, a comment, a carousel, or engagement-bait gating. On a LinkedIn post it would clean the prose and miss every platform tell that actually gets Sai discounted by a recruiter.

**It does not know the voice.** It preserves whatever voice is in the draft. It has no model of the specific positioning your skills encode, and no equivalent of "is there one sentence only Sai would write."

## What to take instead

Three things, all in `proposed-blocklist-patch.md`:

1. The eight pattern categories our blocklist is missing.
2. A voice-preservation section, which our file has no equivalent of.
3. The pass/fail-and-recheck loop replacing our open-ended self-check.
