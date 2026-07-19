"""Daily morning-quote automation.

Pipeline: generate a fresh good-morning message with Claude -> render a
colorful poster (HTML -> PNG via Playwright) -> send both to Telegram for
review -> record the quote in history.json so it never repeats.

Run with --sample to skip the Claude call and render/send a canned quote
(useful for testing the poster and Telegram wiring without an API key).
"""

import datetime
import html
import json
import os
import random
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).parent
HISTORY_FILE = ROOT / "history.json"
TEMPLATE_FILE = ROOT / "templates" / "poster.html"
OUT_DIR = ROOT / "out"

THEMES = ["sunrise", "ocean", "garden", "lavender", "golden", "forest"]

TOPICS = [
    "gratitude", "new beginnings", "friendship", "perseverance", "kindness",
    "health and wellbeing", "contentment and peace of mind", "nature's beauty",
    "positive thinking", "family bonds", "learning at every age", "hope",
    "living in the present moment", "smiling and spreading joy",
    "gratitude to God for a new day", "blessings and good deeds",
    "inner peace and prayer", "timeless wisdom from the Bhagavad Gita",
    "doing one's duty with a cheerful heart",
]

SYSTEM_PROMPT = """\
You write daily good-morning messages for a warm, retired Telugu gentleman who
sends them every morning to his friends and former colleagues on WhatsApp. The
tone is positive, gentle, and uplifting — motivational without being preachy,
sentimental without being saccharine. The messages should feel personal and
shareable, the kind people enjoy receiving with their morning tea.

Style touches he and his friends love (use naturally, not all at once):
- A gentle touch of spirituality: gratitude to God, blessings, inner peace,
  or occasionally a simple piece of wisdom in the spirit of the Bhagavad Gita.
  Keep it warm and universal, never heavy or sermon-like.
- An occasional Telugu phrase in Telugu script with its meaning alongside —
  for example opening the message with "శుభోదయం (Good morning)" or closing
  with a short Telugu blessing. Use Telugu in roughly one message out of
  three, and only in the WhatsApp message, not in the poster quote.
- Festival awareness: if today (or tomorrow) is a notable Indian or Telugu
  festival — Sankranti, Ugadi, Sri Rama Navami, Varalakshmi Vratam, Vinayaka
  Chavithi, Dasara, Deepavali, Karthika Masam, and the like — open with a
  heartfelt festival greeting and let the message reflect its spirit. On
  ordinary days, no festival mention.
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "poster_text": {
            "type": "string",
            "description": (
                "A short original inspirational quote for the poster image. "
                "Maximum 160 characters. No emojis, no attribution."
            ),
        },
        "message": {
            "type": "string",
            "description": (
                "The WhatsApp-ready good morning message: 40-80 words, starts "
                "with a morning greeting, weaves in the same idea as the "
                "poster quote, uses 2-4 tasteful emojis, and ends with a warm "
                "wish for the day."
            ),
        },
    },
    "required": ["poster_text", "message"],
    "additionalProperties": False,
}

SAMPLE = {
    "poster_text": (
        "Every sunrise is a quiet reminder that life gives us "
        "a fresh page each day — write something beautiful on it."
    ),
    "message": (
        "Good morning, my dear friends! \U0001F305 Every sunrise hands us a fresh "
        "page — yesterday's worries need not be copied onto it. Fill today's page "
        "with a kind word, a warm smile, and a little gratitude. \U0001F33B May your "
        "day be peaceful, your tea be perfect, and your heart be light. Have a "
        "wonderful day! ☀️"
    ),
}


def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return []


def save_history(history):
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n")


def generate_quote(history):
    from anthropic import Anthropic

    client = Anthropic()
    recent = [entry["quote"] for entry in history[-80:]]
    topic = random.choice(TOPICS)

    today = datetime.date.today().strftime("%A, %d %B %Y")
    prompt = (
        f"Today is {today}. Write today's good-morning message. "
        f"Suggested theme (set it aside if a festival takes precedence): {topic}."
    )
    if recent:
        prompt += (
            "\n\nIt must be a completely fresh idea — do NOT repeat or closely "
            "paraphrase any of these previously sent quotes:\n"
            + "\n".join(f"- {q}" for q in recent)
        )

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        output_config={"format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(block.text for block in response.content if block.type == "text")
    return json.loads(text)


def render_poster(data):
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(exist_ok=True)
    theme = random.choice(THEMES)
    quote = data["poster_text"]

    if len(quote) <= 90:
        font_size = 66
    elif len(quote) <= 130:
        font_size = 58
    else:
        font_size = 50

    today = datetime.date.today().strftime("%A, %d %B %Y")
    page_html = (
        TEMPLATE_FILE.read_text()
        .replace("{{THEME}}", theme)
        .replace("{{QUOTE}}", html.escape(quote))
        .replace("{{DATE}}", today)
        .replace("{{FONT_SIZE}}", str(font_size))
    )
    html_path = OUT_DIR / "poster.html"
    html_path.write_text(page_html)
    png_path = OUT_DIR / "poster.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=os.environ.get("CHROMIUM_PATH") or None
        )
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        page.goto(html_path.as_uri())
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(500)
        page.screenshot(path=str(png_path))
        browser.close()

    print(f"Poster rendered: {png_path} (theme: {theme})")
    return png_path


def send_to_telegram(png_path, data):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID not set — skipping send.")
        return

    api = f"https://api.telegram.org/bot{token}"
    with open(png_path, "rb") as photo:
        resp = requests.post(
            f"{api}/sendPhoto",
            data={"chat_id": chat_id},
            files={"photo": photo},
            timeout=60,
        )
    resp.raise_for_status()
    resp = requests.post(
        f"{api}/sendMessage",
        data={"chat_id": chat_id, "text": data["message"]},
        timeout=60,
    )
    resp.raise_for_status()
    print("Sent poster and message to Telegram.")


def main():
    sample_mode = "--sample" in sys.argv

    history = load_history()
    data = SAMPLE if sample_mode else generate_quote(history)

    print(f"Quote: {data['poster_text']}")
    png_path = render_poster(data)
    send_to_telegram(png_path, data)

    if not sample_mode:
        history.append(
            {
                "date": datetime.date.today().isoformat(),
                "quote": data["poster_text"],
                "message": data["message"],
            }
        )
        save_history(history)
        print("History updated.")


if __name__ == "__main__":
    main()
