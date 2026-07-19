# Morning Quotes Automation

Every morning this repo generates a fresh good-morning message and a colorful
poster, and sends both to your Telegram. You review them there — if you like
them, share the image to WhatsApp and forward it to your father-in-law. If
not, retrigger the workflow for a new one.

## How it works

1. **GitHub Actions** runs daily on a schedule (and on demand via the
   "Run workflow" button).
2. **Claude** (Anthropic API) writes a short original quote plus a
   WhatsApp-ready message, avoiding anything it has sent before
   (`automation/history.json`).
3. **Playwright** renders the quote onto a colorful poster
   (`automation/templates/poster.html`, 6 rotating color themes) as a
   1080×1350 PNG.
4. **Telegram bot** sends you the poster and the message text.
5. The quote is committed to `automation/history.json` so it never repeats.

## One-time setup

### 1. Create a Telegram bot (~3 minutes)

1. In Telegram, message **@BotFather** and send `/newbot`.
2. Give it a name (e.g. "Morning Quotes") and a username (e.g.
   `saikiran_morning_quotes_bot`).
3. BotFather replies with a **bot token** like `123456789:AAH...` — save it.
4. Open a chat with your new bot and send it any message (e.g. "hi").
5. Get your **chat id**: open
   `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in a browser and
   find `"chat":{"id":123456789,...}` — that number is your chat id.

### 2. Get an Anthropic API key

Create one at https://platform.claude.com (each daily message costs roughly
a cent or two with Claude Opus 4.8).

### 3. Add the three secrets to this repo

GitHub → this repo → **Settings → Secrets and variables → Actions → New
repository secret**:

| Secret name          | Value                     |
| -------------------- | ------------------------- |
| `ANTHROPIC_API_KEY`  | your Anthropic API key    |
| `TELEGRAM_BOT_TOKEN` | the BotFather token       |
| `TELEGRAM_CHAT_ID`   | your numeric chat id      |

That's it — the next scheduled run (or a manual run) will deliver to your
Telegram.

## Daily flow

- The poster + message arrive in Telegram each morning.
- **Like it?** Tap the image → Share → WhatsApp, and forward it (and the
  text) to your father-in-law.
- **Don't like it?** Retrigger: open the GitHub app (or github.com) →
  **Actions → Morning Quote → Run workflow**. A brand-new quote and poster
  arrive in ~2 minutes. Repeat as many times as you like.

## Changing the delivery time

GitHub cron runs in **UTC**. Edit the `cron:` line in
`.github/workflows/morning-quote.yml`:

| You want            | Cron (UTC)      |
| ------------------- | --------------- |
| 6:00 AM US Central  | `0 11 * * *` (CDT) / `0 12 * * *` (CST) |
| 6:00 AM US Eastern  | `0 10 * * *` (EDT) / `0 11 * * *` (EST) |
| 6:00 AM IST (India) | `30 0 * * *`    |
| 7:00 AM IST (India) | `30 1 * * *`    |

Note: GitHub scheduled runs can start a few minutes late at busy times.

## Tweaking the style

- **Message tone/content**: edit `SYSTEM_PROMPT` and `TOPICS` in
  `automation/morning_quote.py` (e.g. add "a touch of spirituality" or
  "occasionally reference Indian festivals").
- **Poster look**: edit `automation/templates/poster.html` — themes are
  plain CSS gradients; add or change them and list the names in `THEMES`
  in the script.

## Testing locally

```bash
pip install playwright requests && playwright install chromium
python automation/morning_quote.py --sample   # renders a sample poster, no API key needed
```

The poster is written to `automation/out/poster.png`. If Telegram secrets
are set in your environment it also sends; otherwise it just renders.
