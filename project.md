Nice, let’s turn this into a clean, drop-in GitHub repo you can literally copy-paste.

I’ll give you:

Full folder structure

All important file contents (ready to upload)

A simple dashboard web app to trigger posts manually

AI prompt templates file for each post type

I’ll keep it focused and not bloated so it’s easy to understand.

1️⃣ Folder Structure (ready for GitHub)
telegram-ai-channel/
├── .github/
│   └── workflows/
│       └── auto-post.yml
├── dashboard/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   │   ├── base.html
│   │   └── dashboard.html
│   └── static/
│       └── styles.css
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── pollinations_client.py
│   ├── telegram_client.py
│   ├── scheduler_logic.py
│   ├── templates.py
│   └── config.py
├── requirements.txt
├── README.md
└── .env.example


You can literally create these folders and files as-is.

2️⃣ Root-Level Files
requirements.txt (root)

This is for the scheduled bot (GitHub Actions / local):

requests
python-dotenv

.env.example
BOT_TOKEN=1234567890:YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=-1001234567890
TIMEZONE_OFFSET_HOURS=5.5


You copy this to .env for local use.
On GitHub, you’ll put these values in Secrets instead.

README.md
# Telegram AI Coding Channel Bot

This repo automatically posts AI-generated coding content to a Telegram **channel**.

Features:
- AI text and image posts (via Pollinations.ai, no API key needed)
- AI-generated polls
- AI-generated mini-threads
- Dashboard web UI (Flask) to manually trigger posts

## 1. Setup Telegram Bot & Channel

1. Talk to **@BotFather** on Telegram:
   - `/newbot` → get `BOT_TOKEN`
2. Add the bot as **Admin** to your channel (with "Post Messages" permission).
3. Find your `CHAT_ID` by calling:

   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`

   Look for `"chat":{"id": ... }` from your channel.

## 2. Local Setup

```bash
git clone <this-repo>
cd telegram-ai-channel

cp .env.example .env   # then edit .env with your bot token and chat id
pip install -r requirements.txt
python -m src.main


This runs one cycle (posts something depending on current time).

3. GitHub Actions Automation

Push this repo to GitHub.

Go to: Settings → Secrets and variables → Actions.

Add these repository secrets:

BOT_TOKEN

CHAT_ID

TIMEZONE_OFFSET_HOURS (e.g. 5.5 for IST)

GitHub Actions will run automatically according to the schedule in .github/workflows/auto-post.yml.

4. Dashboard (Manual Control)
cd dashboard
pip install -r requirements.txt
python app.py


Open http://127.0.0.1:5000 in the browser.

From there you can:

Trigger a Text Tip

Trigger an Image + Text Post

Trigger a Poll

Trigger a Thread


---

## 3️⃣ GitHub Actions Workflow

### `.github/workflows/auto-post.yml`

This runs the bot several times per day.

```yaml
name: Telegram AI Auto Poster

on:
  schedule:
    # Every day at 03:00, 09:00, 15:00, 21:00 UTC
    # (adjust to your taste)
    - cron: "0 3,9,15,21 * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run bot main
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
          TIMEZONE_OFFSET_HOURS: ${{ secrets.TIMEZONE_OFFSET_HOURS }}
        run: |
          python -m src.main

4️⃣ Core Python Code (Bot Logic)
src/config.py
import os

from dotenv import load_dotenv

# Load .env when running locally; in GitHub Actions env vars are set directly
load_dotenv(override=False)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()
TIMEZONE_OFFSET_HOURS = float(os.getenv("TIMEZONE_OFFSET_HOURS", "5.5"))  # default IST

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("BOT_TOKEN or CHAT_ID is not set. Check your environment or .env file.")

src/telegram_client.py
import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, data=data)
    return resp


def send_photo(image_url: str, caption: str = ""):
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption
    }
    resp = requests.post(url, data=data)
    return resp


def send_poll(question: str, options: list[str]):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    resp = requests.post(url, data=data)
    return resp


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)

src/pollinations_client.py

Uses Pollinations.ai (free, no key) for text and image.

import urllib.parse
import requests


def generate_text(prompt: str) -> str:
    """Generate free-form text from Pollinations.ai."""
    encoded = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded}"
    resp = requests.get(url, timeout=30)
    if resp.status_code == 200:
        return resp.text.strip()
    return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations based on prompt."""
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}"

src/templates.py ✅ AI template files for each post type

Here you define all your “prompt patterns” for different kinds of posts.

TEXT_TEMPLATES = {
    "python_tip": (
        "Write a short, unique Python tip for intermediate developers. "
        "Include a brief explanation and a small code example. "
        "Keep it under 120 words."
    ),
    "js_tip": (
        "Write a short JavaScript tip about modern ES6+ features. "
        "Include one small example. Under 120 words."
    ),
    "ml_tip": (
        "Explain a practical machine learning tip for beginners. "
        "Use simple language and one small example. Under 150 words."
    ),
    "clean_code": (
        'Give a concise clean-code principle with an example in any language. '
        "Use a friendly tone. Under 120 words."
    ),
    "thread_explainer": (
        "Explain a single programming concept in 4 short numbered sections. "
        "Each section should be 2-3 sentences. Separate sections with two newlines."
    ),
    "poll_question": (
        "Create ONE multiple choice coding question. "
        "Format strictly as: Question? | Option A, Option B, Option C. "
        "Make it short and clear, suitable for a Telegram poll."
    )
}


IMAGE_TEMPLATES = {
    "coding_hero": "futuristic illustration of a programmer surrounded by glowing code, cyberpunk style, high detail",
    "python_image": "minimalist flat illustration of a snake made of Python code, on a dark background",
    "ml_image": "neural network with glowing connections, abstract art, dark background",
}


You can expand this list however you like.

src/scheduler_logic.py

Simple logic to decide what kind of content to post based on time (in your timezone).

from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour.
    You can tweak this easily.

    Returns one of:
    - "python_text"
    - "js_text"
    - "ml_text"
    - "clean_code_text"
    - "image_plus_text"
    - "poll"
    - "thread"
    """
    hour = get_local_hour_24()

    if 6 <= hour < 10:
        return "python_text"
    elif 10 <= hour < 13:
        return "js_text"
    elif 13 <= hour < 16:
        return "ml_text"
    elif 16 <= hour < 19:
        return "image_plus_text"
    elif 19 <= hour < 21:
        return "poll"
    else:
        return "thread"  # late evening / night

src/main.py ✅ The main orchestrator
from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES


def post_python_tip():
    prompt = TEXT_TEMPLATES["python_tip"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_js_tip():
    prompt = TEXT_TEMPLATES["js_tip"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_ml_tip():
    prompt = TEXT_TEMPLATES["ml_tip"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_clean_code_tip():
    prompt = TEXT_TEMPLATES["clean_code"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_image_plus_text():
    text_prompt = TEXT_TEMPLATES["clean_code"]
    img_prompt = IMAGE_TEMPLATES["coding_hero"]

    caption = ai.generate_text(text_prompt)
    img_url = ai.image_url(img_prompt)

    tg.send_photo(img_url, caption)


def post_poll():
    poll_prompt = TEXT_TEMPLATES["poll_question"]
    raw = ai.generate_text(poll_prompt)

    # Expect format: "Question? | A, B, C"
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
        else:
            tg.send_text("Poll generation failed: not enough options.")
    else:
        tg.send_text("Poll generation failed: invalid format from AI.")


def post_thread():
    thread_prompt = TEXT_TEMPLATES["thread_explainer"]
    raw = ai.generate_text(thread_prompt)
    # Split by double-newline into sections
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if len(parts) == 0:
        tg.send_text(raw)
    else:
        tg.send_thread(parts)


def main():
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    if post_type == "python_text":
        post_python_tip()
    elif post_type == "js_text":
        post_js_tip()
    elif post_type == "ml_text":
        post_ml_tip()
    elif post_type == "clean_code_text":
        post_clean_code_tip()
    elif post_type == "image_plus_text":
        post_image_plus_text()
    elif post_type == "poll":
        post_poll()
    elif post_type == "thread":
        post_thread()
    else:
        tg.send_text("No valid post type decided.")


if __name__ == "__main__":
    main()

5️⃣ Dashboard Web App (Manual Control)

This lets you open a browser and click buttons to trigger posts.

dashboard/requirements.txt
Flask
python-dotenv
requests

dashboard/app.py
import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES, IMAGE_TEMPLATES

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")


@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/send/python-tip")
def send_python_tip():
    text = ai.generate_text(TEXT_TEMPLATES["python_tip"])
    tg.send_text(text)
    flash("Python tip sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/image-post")
def send_image_post():
    caption = ai.generate_text(TEXT_TEMPLATES["clean_code"])
    img_url = ai.image_url(IMAGE_TEMPLATES["coding_hero"])
    tg.send_photo(img_url, caption)
    flash("Image + caption sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/poll")
def send_poll():
    raw = ai.generate_text(TEXT_TEMPLATES["poll_question"])
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
            flash("Poll sent!", "success")
        else:
            flash("Poll generation failed (not enough options).", "error")
    else:
        flash("Poll generation failed (bad format).", "error")
    return redirect(url_for("index"))


@app.route("/send/thread")
def send_thread():
    raw = ai.generate_text(TEXT_TEMPLATES["thread_explainer"])
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if parts:
        tg.send_thread(parts)
        flash("Thread sent!", "success")
    else:
        flash("Thread generation failed.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

dashboard/templates/base.html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Telegram AI Dashboard</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
  <header>
    <h1>Telegram AI Channel Dashboard</h1>
  </header>

  <main>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <div class="flash-container">
          {% for category, message in messages %}
            <div class="flash flash-{{ category }}">{{ message }}</div>
          {% endfor %}
        </div>
      {% endif %}
    {% endwith %}
    {% block content %}{% endblock %}
  </main>

  <footer>
    <p>Powered by Pollinations.ai & Telegram Bot API</p>
  </footer>
</body>
</html>

dashboard/templates/dashboard.html
{% extends "base.html" %}

{% block content %}
<div class="card-grid">
  <div class="card">
    <h2>Python Tip</h2>
    <p>AI-generated Python coding tip with example.</p>
    <a href="{{ url_for('send_python_tip') }}" class="btn">Send to Channel</a>
  </div>

  <div class="card">
    <h2>Image + Text</h2>
    <p>Clean-code tip with a generated coding illustration.</p>
    <a href="{{ url_for('send_image_post') }}" class="btn">Send to Channel</a>
  </div>

  <div class="card">
    <h2>Poll</h2>
    <p>Multiple-choice coding question for your audience.</p>
    <a href="{{ url_for('send_poll') }}" class="btn">Send to Channel</a>
  </div>

  <div class="card">
    <h2>Thread</h2>
    <p>4-part explanation thread on a coding concept.</p>
    <a href="{{ url_for('send_thread') }}" class="btn">Send to Channel</a>
  </div>
</div>
{% endblock %}

dashboard/static/styles.css
body {
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: radial-gradient(circle at top, #1f2933, #020617);
  color: #e5e7eb;
}

header {
  padding: 1.5rem;
  text-align: center;
  border-bottom: 1px solid rgba(148, 163, 184, 0.4);
}

main {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1rem;
}

footer {
  text-align: center;
  padding: 1rem;
  font-size: 0.85rem;
  color: #9ca3af;
}

.card-grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.card {
  background: rgba(15, 23, 42, 0.9);
  border-radius: 1rem;
  padding: 1.25rem;
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(148, 163, 184, 0.3);
}

.card h2 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 0.95rem;
  color: #cbd5f5;
}

.btn {
  display: inline-block;
  margin-top: 0.75rem;
  padding: 0.6rem 1.1rem;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  background: linear-gradient(135deg, #6366f1, #ec4899);
  color: white;
  box-shadow: 0 10px 25px rgba(79, 70, 229, 0.5);
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}

.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 14px 30px rgba(79, 70, 229, 0.7);
}

.flash-container {
  margin-bottom: 1rem;
}

.flash {
  padding: 0.6rem 0.9rem;
  border-radius: 0.5rem;
  margin-bottom: 0.4rem;
  font-size: 0.9rem;
}

.flash-success {
  background: rgba(34, 197, 94, 0.15);
  border: 1px solid rgba(34, 197, 94, 0.6);
}

.flash-error {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.6);
}


If you want, next I can:

Add a “test mode” so you can post to a private test channel first

Add language switches (Python day, JS day, ML day, etc.)

Add an “LLM signature” (e.g., “Generated by AI Tip Engine”) at the bottom of every post.

ChatGPT can make mistakes. Che