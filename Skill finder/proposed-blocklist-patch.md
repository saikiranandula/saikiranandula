# Proposed patch to ai-slop-blocklist.md

> **STATUS: all nine patches applied 2026-07-28.**
> Live files updated in `~/.claude/skills/*/references/ai-slop-blocklist.md`.
> Originals in `backup/`. Final files in `patched/`.
> **These live files are ephemeral.** See "Persistence" at the end of this doc.

Drop-in text closing the gaps in `blocklist-gap-analysis.md`.

Targets both copies unless noted:
- `~/.claude/skills/linkedin-content/references/ai-slop-blocklist.md`
- `~/.claude/skills/nullhypeai/references/ai-slop-blocklist.md`

Written in the existing file's voice and house rules (no em dashes, pattern-then-arrow-then-fix, high-suspicion framing rather than hard bans).

---

## Patch 1 — new patterns, append to "Body patterns"

Both files.

```markdown
- **Colon reveal** (fake drama from a noun phrase, a colon, then a lowercase reveal): "The detail that makes it work: a separate agent grades it.", "The best part: it learns.", "The real story: nobody read the eval." → Rewrite as a plain sentence. Colons are for lists, labels, and quotes, not suspense.
- **Superficial analysis** (trailing `-ing` clause that pretends to explain significance): "…, highlighting the team's commitment to X", "…, underscoring the shift toward Y", "…, reflecting a broader trend", "…, showcasing what's possible", "…, signaling a new era." → Replace with the actual consequence: "The launch adds file search, so users can find old drafts without leaving the editor."
- **Importance puffery** (asserting that something matters instead of showing it): "marks a pivotal moment", "stands as a testament to", "plays a vital role in", "solidifies its position as", "underscores the significance of", "represents a major step forward." → State the fact and let the reader judge. "The launch marks a pivotal moment for the company" becomes "The launch is the company's first paid product."
- **Weasel attribution** (a claim with no owner): "experts agree", "studies show", "industry reports suggest", "many argue", "it's widely regarded as", "research indicates", "sources say." → Name the source with a date, or cut the claim. Never invent a source. If there is no source, ask before publishing. This is the hardest rule in the file: the entire positioning rests on claims a reader can check.
- **Fake-strong verbs** (an inflated verb where a plain one is clearer): "serves as a centralized hub for", "acts as a bridge between", "functions as the backbone of", "represents an opportunity to." → Prefer "is" and "has" when they are clearer. "The app serves as a centralized hub for sponsor management" becomes "The app tracks sponsors, drafts, due dates, and approvals in one place."
- **Synonym cycling** (rotating terms for the same thing to avoid repetition): the agent, then the assistant, then the tool, then the system, all meaning one product. → If the clear word is right, repeat it.
- **Negative listing** ("Not a X. Not a Y. A Z."): a cousin of binary contrast with the same tell. → Just say Z.
- **Rhetorical setups**: "What if I told you…", "Think about it:", "Plot twist:", and the self-answered question ("Why does this matter? Because…"). → Drop the setup, make the point.
```

## Patch 2 — new patterns, append to "Closers"

Both files.

```markdown
- **Summary-recap ending** (a final paragraph restating the piece): "In conclusion,", "Ultimately,", "Overall,", "To sum up,", "So what does this all mean?" → The reader was just there. End on the last concrete point, the takeaway, or the real implication.
```

## Patch 3 — new section, "Shape tells"

Both files, after "Word-level tells." This is the one that catches over-correction, and nothing in the current file does.

```markdown
## Shape tells (the over-corrected slop)

Removing every pattern above and nothing else produces a second, subtler kind of slop: uniformly clipped, evidence-dense, declaratively identical prose. It reads as edited-by-machine rather than written-by-a-person. Scan for shape, not just phrases:

- **Robotic rhythm:** three or more consecutive sentences with the same shape (subject, verb, number). Every paragraph the same length. Every block opening with a claim and closing with a stat. Vary the shape unless a repetition is doing real work.
- **Uniform tidiness:** every paragraph equally polished, no digression, no aside, no change of pace. Real writing is uneven.
- **Stacked punchy fragments:** already banned as dramatic fragmentation, but it reappears after heavy editing when long sentences get split. Splitting a tangled sentence is good; splitting a clear one into staccato beats is not.
- **Hedge-stripping:** cutting every "I think," "probably," "my read is" manufactures a confidence the writer does not have. Cut hedges that pad. Keep hedges that carry real uncertainty or match how Sai actually talks.
```

## Patch 4 — new section, "What not to touch"

Both files, immediately before the self-check. Our file currently has no counterweight to the blocklist at all.

```markdown
## What not to touch

The blocklist is subtractive. This section is the limit on it. Over-application costs more credibility than the original slop, because generic-but-clean reads as machine-edited to exactly the senior audience being targeted.

Before editing any draft, note 3 to 5 voice signals to preserve: vocabulary, cadence, bluntness, humor, real uncertainty, digressions, level of polish. Keep the note internal. Then:

- **Make the minimum effective edit.** Fix the patterns above. Leave strong sentences alone. A rough draft with a real voice should sound like the same person afterward.
- **Keep hedges that carry meaning.** "I think," "maybe," "my read is," "to be honest" stay when they express genuine uncertainty, self-awareness, or spoken rhythm. They go only when they pad.
- **Keep the edge.** Strong opinions, blunt phrasing, humor, self-interruption, and honest admissions of being wrong belong to the writer. Do not replace them with safer or more professional wording.
- **Keep a personal aside that earns its place.** The ban is on the manufactured story arc, the engineered lesson, and the "here's what it taught me" hinge. It is not a ban on Sai referencing something he actually did, told plainly with specifics.
- **Do not front-load everything.** Lead with the point when the setup adds nothing. Keep a setup that creates real context or tension.
- **Do not reorganize for neatness.** Preserve the argument's progression and its detours unless the structure is actively hurting the piece. If it is reorganized, say why.
```

## Patch 5 — replace the self-check with a pass/fail loop

Both files. Replaces the existing "Self-check before publishing" section. The change that matters is the last line: a failure means fix and re-run, not note-and-ship.

```markdown
## Self-check before publishing

Answer each as pass or fail. Any fail means fix the draft and run the whole list again.

**Openers and closers**
1. Could the first two lines sit unchanged under any AI announcement or any generic post in this niche? Fail if yes.
2. Any throat-clearer, false-exclusivity, urgency, or fake-vulnerability opener present? Fail if yes.
3. Any CTA, gating ask, fake-philosophical closer, mic drop, or summary recap present? Fail if yes.

**Patterns**
4. Any binary contrast, negative listing, fill-in-the-blank template, or colon reveal? Fail if yes and the contrast is not carried by specific evidence.
5. Any trailing `-ing` significance clause, importance puffery, or fake-strong verb? Fail if yes.
6. Every claim either carries a named source with a date or is Sai's own observation? Fail if any claim rests on "experts agree," "studies show," or an unattributed number.
7. Any pivot phrase, rhetorical setup, dramatic fragmentation, or synonym cycling? Fail if yes.

**Substance**
8. Does every paragraph carry a fact, a comparison, a mechanism, or an advance in the argument? Fail if any line only decorates.
9. Do vague adverbs, empty adjectives, or smart-sounding verbs cluster anywhere (3+ in a paragraph)? Fail if yes.
10. Is there at least one sentence only Sai would write, because of a real tradeoff, adoption bottleneck, or operating consequence he has seen? Fail if no. Add it or kill the draft.
11. Would Sai say this out loud to another PM in a serious conversation? Fail if it would sound like a performance.

**Shape and voice**
12. Three or more consecutive sentences sharing the same shape, or every paragraph the same length? Fail if yes.
13. Would Sai recognize this as his own voice, with his hedges, edge, and cadence intact? Fail if it reads as cleaned-up-generic.

**House rules**
14. No em dashes, no emoji in the body, no engagement-bait CTA, no broetry wall of single lines. Any violation is a fail.
```

## Patch 6 — detect mode

Both files, appended at the end. New capability rather than a fix.

```markdown
## Detect mode

When the ask is "is this AI slop" or "audit this" rather than "publish this", do not rewrite and do not score.

For each pattern found: name the pattern from this file, quote the offending line, give the fix in a few words. Then stop and offer to edit.

Never claim AI wrote something. Detectors guess. Named patterns are evidence the reader can check for themselves.
```

## Patch 7 — word-list additions

Both files, folded into "Word-level tells."

```markdown
- **Additional banned words** (near-certain tells, from the wider corpus): delve, foster, utilize, facilitate, empower, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, elevate, embark, harness, ever-evolving, paradigm shift.
- **Often-empty phrases that delay the point:** "it's important to note", "at its core", "in the age of", "in the world of", "the reality is", "the truth is", "in terms of", "with regard to", "going forward", "in this piece". → Cut when they delay the point. Keep one occasionally if it is genuinely part of Sai's spoken voice and the sentence still earns its place.
```

## Patch 8 — X-copy repairs

`nullhypeai` only. Two are corrections, the rest are backports of LinkedIn-copy content that applies equally on X.

**Correction.** Line 43 currently reads "not like the median LinkedIn post" inside the X skill. Change to "not like the median AI take on the timeline."

**Correction.** Add `ultimately` to the adverb list on line 30.

**Backport from the LinkedIn copy** (all apply on X):
- The fill-in-the-blank thought-leader templates bullet, retargeted at X-native templates ("X is the new Y", "If you're still doing X, you're already behind", "Your agent is only as good as your context window").
- The qualifier sandwich bullet.
- The "I asked ChatGPT" and time-lapse-brag bullet. This is arguably a bigger problem on X than on LinkedIn.
- Artificial scarcity ("I read 50 papers so you don't have to"), which pairs with the existing numbered-list-as-synthesis bullet.

**Do not backport** (LinkedIn-only): broetry and the `…see more` cliffhanger, comment-gating CTAs, humble-brag-as-announcement, the corporate-LinkedIn filler list, the product-leader-specific tells section.

## Patch 9 — the drift problem

The two files share roughly 80% of their content with no shared source, and have already diverged by 23 lines. Every future addition has to be made twice and will eventually be made once.

Options, in order of preference:

1. **Delimited shared block.** Wrap the common content in both files with `<!-- SHARED:BEGIN -->` and `<!-- SHARED:END -->` markers, keep platform deltas outside the markers, and add a line to both SKILL.md reference tables noting that the shared block is updated in lockstep. No tooling required.
2. **Single canonical file plus two deltas.** Cleaner, but depends on whether a skill can load a reference outside its own directory. Verify before committing to it.
3. **Symlink the shared file.** Fragile across skill sync and packaging. Not recommended.

## What was applied

All nine, in one pass. Result:

| File | Before | After |
|---|---|---|
| `linkedin-content/references/ai-slop-blocklist.md` | 74 lines | 159 lines |
| `nullhypeai/references/ai-slop-blocklist.md` | 51 lines | 138 lines |

Both files were rebuilt rather than edited in place, because patch 9 required moving the shared content into one contiguous block. Assembly was `head + shared + tail`, and the shared block was verified byte-identical across both copies (92 lines, md5 prefix `4ef352b47582`).

Two changes beyond the patch spec, both cleanups the rewrite made obvious:

1. **Em dashes removed from the files' own headings.** The originals used them in section headers ("Openers (the most damaging — they set the read)") while instructing that em dashes are banned. Both files are now at zero.
2. **Platform-specific rules pulled out of the shared sections.** Engagement-bait gating, humble-brag announcements, corporate filler, broetry, and the product-leader tells now sit in a LinkedIn-only section below the shared block. The X copy gained a parallel section carrying the emoji rule, the paragraph-based house style, and the note that its 1-to-2-sentence block structure is scannability rather than dramatic fragmentation, with a pointer at the new "Shape tells" section.

### Verification

- All 15 patch markers present in both files.
- `median LinkedIn post` bug gone from the X copy.
- `ultimately` present in the X adverb list.
- Four backports present in the X copy: templates, qualifier sandwich, "I asked ChatGPT", artificial scarcity.
- Five LinkedIn-only rules confirmed absent from the X copy.

### Open question deliberately left alone

Patch 8 specified *not* backporting engagement-bait gating to X, and that was followed. Reply-gating ("reply 'AI' and I'll DM you") is common on X too, so this is arguably worth revisiting as a tenth patch.

## Persistence

**The live edits will not survive this container.** Both skills are `source: custom` in `~/.claude/skills/manifest.json`, meaning they sync down from claude.ai and local edits do not sync back. The `nullhypeai` SKILL.md additionally declares itself a packaged snapshot whose source of truth is the private repo `saikiranandula/nullhype-content-os`, which is not in this session's scope.

To make the change permanent, one of:

1. **LinkedIn copy:** upload `patched/linkedin-content--ai-slop-blocklist.md` to the `linkedin-content` skill on claude.ai, replacing `references/ai-slop-blocklist.md`.
2. **X copy:** commit `patched/nullhypeai--ai-slop-blocklist.md` to `saikiranandula/nullhype-content-os` at `references/ai-slop-blocklist.md`, then repackage the skill snapshot.

Both patched files are committed in this repo under `patched/`, so nothing is lost when the container is reclaimed.
