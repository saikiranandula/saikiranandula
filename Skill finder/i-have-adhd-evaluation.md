# i-have-adhd

**Repo:** [github.com/ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
**License:** MIT. 12.3k stars, 628 forks at time of review.
**Verdict:** Install. Low risk, moderate value in Claude Code, higher value in Codex or plain chat.

## What it actually is

An output-style skill. It changes how the agent presents information, not what it knows or does. Ten rules, plus a persistence clause, plus six documented override conditions, plus a pre-send checklist.

Credited to *The Adult ADHD Tool Kit* (Ramsay and Rostain), adapted for LLM output rather than human day-planning. No diagnosis required; the README pitches it as a general readability upgrade.

The frontmatter matters for your setup:

```yaml
name: i-have-adhd
disable-model-invocation: true
```

`disable-model-invocation: true` means the model can never load this on its own. It fires only when you type `/i-have-adhd`, and stays on for the rest of the session until you say "stop adhd mode" or "normal mode." That property is what makes it safe to install alongside your content skills.

## The ten rules

1. Lead with the next action. First line is a command, path, or snippet. Prose after, if at all.
2. Number multi-step tasks. One bounded action per step, fewest steps that still work.
3. End with one concrete next action doable in under two minutes.
4. Suppress tangents. Finish the first issue, then offer the second as a separate question.
5. Restate state every turn. "Step 3 of 5 done: schema updated. Next: backfill the column."
6. Give specific time estimates. "About 15 minutes if tests cover this" beats "some work."
7. Make completed work visible in concrete terms. Show what now works and how to see it.
8. Matter-of-fact errors. No "Uh oh." State cause and fix with file and line.
9. Cap lists at five. Past five, split into do-now vs later, or must vs nice-to-have.
10. No preamble, no recap, no closing pleasantries. Explicit forbidden-phrase lists for each.

## What is genuinely additive for you

Claude Code's system prompt already suppresses most of rule 10 and much of rule 8. You are not currently getting "Great question!" or "Hope this helps." So the marginal gain concentrates in four rules:

- **Rule 5 (restate state).** The real win. On long multi-step sessions the agent assumes you remember where you are. Forcing a state line every turn removes scrollback hunting.
- **Rule 6 (time estimates).** Not something Claude Code does by default at all. Useful for deciding whether to wait or context-switch.
- **Rule 3 (one concrete next action).** Converts an open-ended "let me know" ending into something executable.
- **Rule 7 (visible wins).** Turns "I've made some changes" into "Login now works with magic links. Try `npm run dev`, open `/login`."

Rules 1, 2, 4, 9 are useful but closer to what you already get.

## The override clauses are the reason to trust it

Most output-style skills fail by applying their shape to cases that need the opposite. This one enumerates six escapes, and clause 5 is the one that protects your content work:

> "When a rule would delete the answer itself, the task wins; the shape stays. Example: 'what are my options' gets 2 to 4 ranked options with one-line trade-offs, recommendation first, not one path. The options are the answer."

Clause 6 subordinates the skill to the harness system prompt. Clause 1 exempts anything you introduce with "explain" or "walk me through." Clause 2 forces confirmation before destructive actions regardless of brevity.

## Conflict check against your setup

| Against | Risk | Reason |
|---|---|---|
| `linkedin-content` / `nullhypeai` | None | Manual invocation only. It shapes chat messages, not the drafted post body, which the skills deliver in code blocks. Override clause 5 covers the rest. |
| `stop-hook-reply-gate.py`, `user-prompt-submit-reply-reminder.py` | Low | These enforce reply behavior at the harness level. Override clause 6 explicitly yields to the harness. |
| `morning` skill | Low | Renders an HTML artifact; output shaping does not reach artifact content. |
| Claude Code system prompt | None | Clause 6 defers. |

The one real friction: rule 9 (cap lists at five) and rule 4 (suppress tangents) fight any request for a broad survey or a full audit. Clause 5 nominally handles it, but expect to say "explain" or "stop adhd mode" when you want breadth.

## Install

```bash
claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Then `/i-have-adhd` per session. Always-on is `touch ~/.claude/.i-have-adhd-always`.

**Do not turn on always-on.** Start with per-session invocation for a week. The value is concentrated in long implementation sessions, not in content or research work, and always-on removes your ability to notice which is which.

To customize, the README's path is fork, edit `skills/i-have-adhd/SKILL.md`, uninstall upstream (fork and upstream share a name), then add your fork as a marketplace.
