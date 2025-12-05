# Telegram AI Coding Channel Bot

This repo automatically posts AI-generated coding content to a Telegram **channel**.

## Features
- 🤖 AI text and image posts (via Pollinations.ai, no API key needed)
- 📊 AI-generated polls
- 🧵 AI-generated mini-threads
- 🎨 Dashboard web UI (Flask) to manually trigger posts
- ⏰ Automated scheduling via GitHub Actions

## 1. Setup Telegram Bot & Channel

1. Talk to **@BotFather** on Telegram:
   - `/newbot` → get `BOT_TOKEN`
2. Add the bot as **Admin** to your channel (with "Post Messages" permission).
3. Find your `CHAT_ID` by calling:

   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```

   Look for `"chat":{"id": ... }` from your channel.

## 2. Local Setup

```bash
git clone <this-repo>
cd telegram-ai-channel

cp .env.example .env   # then edit .env with your bot token and chat id
pip install -r requirements.txt
python -m src.main
```

This runs one cycle (posts something depending on current time).

## 3. GitHub Actions Automation

1. Push this repo to GitHub.

2. Go to: **Settings → Secrets and variables → Actions**.

3. Add these repository secrets:
   - `BOT_TOKEN`
   - `CHAT_ID`
   - `TIMEZONE_OFFSET_HOURS` (e.g. 5.5 for IST)

GitHub Actions will run automatically according to the schedule in `.github/workflows/auto-post.yml`.

## 4. Dashboard (Manual Control)

```bash
cd dashboard
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in the browser.

From there you can:
- ✅ Trigger a Text Tip
- ✅ Trigger an Image + Text Post
- ✅ Trigger a Poll
- ✅ Trigger a Thread

## Project Structure

```
telegram-ai-channel/
├── .github/workflows/     # GitHub Actions automation
├── dashboard/             # Flask web UI for manual posting
├── src/                   # Core bot logic
│   ├── config.py         # Configuration management
│   ├── telegram_client.py # Telegram API wrapper
│   ├── pollinations_client.py # AI generation
│   ├── templates.py      # AI prompt templates
│   ├── scheduler_logic.py # Time-based posting logic
│   └── main.py           # Main orchestrator
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## Customization

- **Edit prompts**: Modify `src/templates.py` to change AI generation prompts
- **Change schedule**: Edit `.github/workflows/auto-post.yml` cron schedule
- **Adjust posting logic**: Modify `src/scheduler_logic.py` to change what posts when

## License

MIT

---

**Powered by Pollinations.ai & Telegram Bot API**
