# Gap analysis: our anti-slop content vs no-ai-slop

Compares `references/ai-slop-blocklist.md` (both copies) against `petergyang/no-ai-slop` (`SKILL.md` + `eval.md`).

**Files under review**

| File | Lines | Used by |
|---|---|---|
| `~/.claude/skills/linkedin-content/references/ai-slop-blocklist.md` | 74 | `linkedin-content` SKILL.md lines 20, 55 |
| `~/.claude/skills/nullhypeai/references/ai-slop-blocklist.md` | 51 | `nullhypeai` SKILL.md lines 38, 88 |
| `no-ai-slop/SKILL.md` + `eval.md` | 94 + 43 | standalone |

Both of our copies derive from AISLOPOPEDIA. The LinkedIn copy is the extended one and is the primary comparison target below.

## Scoreboard

- Yang's pattern categories we cover: **9 of 17 fully, 2 partially, 6 missing.**
- Categories we have that Yang has **zero** coverage of: **15.**
- Structural capabilities he has that we lack: **3.**

We win on breadth for our platforms. He wins on enforcement and on the specific tells that afflict analytical prose.

## Where he covers something we do not

| Yang's pattern | Us | Why it matters here |
|---|---|---|
| **Colon reveals** — "The best part: it learns." | Missing | Top-tier current tell. Fake drama from a noun phrase, colon, lowercase reveal. Extremely common in AI-written X posts. |
| **Superficial analysis** — trailing `-ing` clauses: "highlighting the team's commitment," "underscoring the shift" | Missing | The single highest-value addition. This is exactly what an LLM does when told to write analyst commentary, which is Sai's stated voice on both platforms. |
| **Weasel attribution** — "experts agree," "studies show," "industry reports suggest," "widely regarded as" | Missing | Worst omission relative to strategy. Both skills demand data-backed claims. Neither says *name the source or cut the claim, and never invent one.* |
| **Importance puffery** — "marks a pivotal moment," "stands as a testament," "plays a vital role," "solidifies its position" | Partial | We ban the mic-drop closer and the fake-philosophical closer. We do not catch mid-body puffery, which is where it usually lives. |
| **Synonym cycling** — the agent, then the assistant, then the tool, for the same thing | Missing | Reads as padding to a technical audience. |
| **Fake-strong verbs** — "serves as a centralized hub for" | Missing | We ban a list of smart-sounding verbs. We do not catch the construction, or say to prefer plain "is" and "has." |
| **Negative listing** — "Not a X. Not a Y. A Z." | Missing | Adjacent to our binary-contrast ban but structurally different and not caught by it. |
| **Summary-recap endings** — "In conclusion," "Ultimately," "Overall," or a closing paragraph restating the piece | Missing | We ban several closer types but not the recap. Yang's fix is good: end on the last concrete point instead. |
| **Robotic rhythm** — repeated sentence shapes, identical paragraph structures, stacked punchy fragments | Missing | This is a *shape* check, not a phrase check. Nothing in our file catches it, and our own "short blocks of 1-2 sentences" house style on X actively increases the risk. |
| **Rhetorical setups** — "What if I told you," "Think about it:", "Plot twist:", self-answered question-then-answer | Partial | Our pivot-phrase list catches "Plot twist:" on LinkedIn only. The self-answered Q-A pair is uncaught in both. |

Word-level omissions worth folding in: *delve, foster, utilize, facilitate, empower, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, elevate, embark, harness, ever-evolving*, and the phrases *it's important to note, at its core, in the age of, the reality is, the truth is, in terms of, going forward, in this article*.

## Where we cover something he does not

| Ours | Yang |
|---|---|
| Manufactured urgency ("Stop what you're doing," "PSA:") | None |
| Fake vulnerability and the manufactured story arc, including the rejection cold-open and the too-neat anecdote | None |
| Fill-in-the-blank thought-leader templates ("X isn't just Y. It's Z.", "X is the new Y.") | None |
| False agency, named as a category with eight examples | Principle only ("never let inanimate things do human verbs") |
| Numbered-list-as-synthesis and artificial scarcity ("I read 50 papers so you don't have to") | None |
| "I asked ChatGPT" and the time-lapse brag ("built this in 2 hours") | None |
| Pivot phrases as fake connective tissue, eight examples | Narrower ("rhetorical setups") |
| Qualifier sandwich ("To be fair…", "That said…", "Don't get me wrong…") | Partial, via empty qualifiers |
| CTA slop, ten examples | None |
| Engagement-bait gating ("Comment 'GUIDE' and I'll send it") | None |
| Humble-brag-as-announcement | None |
| Broetry walls, `…see more` cliffhanger hooks, emoji bullets and headers, orphan arrows, all-caps emphasis lines | Generic "formatting slop" only |
| **Comment and reply slop as a full category** | None |
| The four high-risk tells for a product-leader voice specifically | None |
| The persona test: "one sentence only Sai would write," "would Sai say this out loud to another PM" | Weaker equivalent in eval ("would the writer recognize this") |

Two of our design choices are also better than his:

**The clustering rule.** "These are not never-write-these-words rules. One may be fine; a cluster means rewrite." Yang bans 26 words outright, which fires on legitimate quotation and on words that are occasionally correct. Ours degrades gracefully; his does not.

**Genre-level bans.** Yang bans phrases. We ban post archetypes: the manufactured-mentorship anecdote, the fake-metric-plus-tidy-framework post, the "shipping is a mindset" reframe. That operates a level above a phrase list and is considerably harder to write. It is the strongest content in our file.

**One more.** We tie slop to distribution, not just taste: low dwell, no saves, no real discussion, and Grox reading the patterns on X. Yang's rationale is purely craft.

## Structural gaps

### 1. No voice-preservation counterweight

Our file is entirely subtractive. Every line names something to kill. Nothing tells the model what to leave alone.

Yang spends roughly 40% of his skill on protection: preserve cadence, keep hedges that carry real uncertainty, keep profanity and humor and self-interruptions, make the minimum effective edit, do not make every paragraph equally tidy, do not front-load everything into the same shape.

The failure mode this creates for us is specific and already predictable from our own rules. Strip every hedge, ban every soft adverb, demand a number in every paragraph, forbid em dashes, forbid emoji, forbid CTAs, and enforce short blocks. What comes out is uniformly clipped, evidence-dense, declarative prose with identical paragraph shapes. That is a recognizable style. It is Yang's "robotic rhythm," and our own file has no check that would catch it.

The `linkedin-content` self-check items 5 and 6 gesture at this but are checks on *content* originality, not on *cadence* preservation.

### 2. No edit/detect split

Our file is a pre-publish gate. It answers "should this ship." It has no mode that answers "is this AI slop, and where," which is what you want when auditing an existing post, a competitor's post, or a draft you did not write.

Yang's framing is worth adopting verbatim: name the pattern, quote the line, give the fix in a few words, do not rewrite, do not score, do not claim AI wrote it. Detectors guess; named patterns are checkable evidence.

### 3. No verification loop

Ours is seven open questions with no instruction about what to do after a failure and no re-run. Yang's is 20+ binary pass/fail checks in a separate file, plus an explicit loop: *if any check fails, fix the draft and run the checks again.* The separate-file split also matters, because the checks stay outside the context that produced the draft.

## Maintenance bug found

The two copies have drifted apart and there is no shared source.

The X copy is missing, relative to the LinkedIn copy: the fill-in-the-blank templates section, the qualifier sandwich, the "I asked ChatGPT" pattern, engagement-bait gating, humble-brag-as-announcement, the corporate-filler word list, `ultimately` in the adverb list, the formatting-tells section, and self-check items 5 and 6.

Some of those are legitimately LinkedIn-only. Several are not: the templates section, the qualifier sandwich, and "I asked ChatGPT" apply at least as strongly on X.

And line 43 of the X copy reads:

> "Nullhype's edge is sounding like a specific analyst with specific evidence, not like **the median LinkedIn post**."

That is a copy-paste artifact pointing the X skill at the wrong platform.

Recommended fix: promote the shared 80% into one canonical blocklist and keep two thin platform-delta files. Given how the skills load references, the simplest version is to keep both files but mark a clearly delimited shared section that gets updated in lockstep.

## Bottom line

Our content is more sophisticated than Yang's where it overlaps, and covers substantially more ground for the two platforms it targets. It is weaker in three specific ways: eight blind spots that happen to sit right on top of analytical prose, no protection against over-correction, and a self-check with no teeth.

Fixes for all three are in `proposed-blocklist-patch.md`.
