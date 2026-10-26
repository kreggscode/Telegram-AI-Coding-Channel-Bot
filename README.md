# 🚀 Telegram AI Coding Channel Bot (@kreggscode)

[![Telegram Channel](https://img.shields.io/badge/Telegram-Join%20%40kreggscode-2CA5E0?logo=telegram&style=for-the-badge)](https://t.me/kreggscode)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Automation](https://img.shields.io/badge/GitHub%20Actions-Automated-brightgreen?style=for-the-badge&logo=githubactions)](https://github.com/kreggscode/Telegram-AI-Coding-Channel-Bot/actions)

An automated, enterprise-grade AI engine that generates, formats, and publishes daily elite software engineering content to Telegram channels.

---

## ✨ Features

- 💻 **Syntax-Highlighted Code Blocks**: Enforces `<pre><code class="language-*">` HTML tags ensuring Telegram's native **Copy Code** button and syntax highlighting are always active.
- 🧠 **Interactive Quizzes**: Delivers daily multiple-choice knowledge checks directly through Telegram's native Quiz engine with instant answer validation.
- 📄 **Branded PDF Notes & Daily Magazine**: Generates publication-grade daily cheat sheets and magazines (`fpdf2`) with branded covers.
- 🎯 **Advanced Telegram & Google SEO**: Structured headings, high-volume searchable tags, and Google-indexable previews (`t.me/s/kreggscode`).
- 🛡️ **Zero-Failure Formatter**: Custom Markdown-to-Telegram-HTML conversion engine (`src/formatter.py`) preventing entity parse errors (HTTP 400) and eliminating ugly raw markdown brackets.
- ⏰ **Stateless Automated Scheduling**: Runs on GitHub Actions according to optimal IST dev engagement windows.
- 🎨 **Web Dashboard**: Local Flask UI for triggering manual posts, testing prompts, and managing broadcasts.

---

## 📅 Daily Publishing Tracks & Schedule (IST)

| Time (IST) | Track | Content Deliverable |
| :--- | :--- | :--- |
| **8:10 AM** | 📖 **Daily Magazine** | Full Multi-Page Technical PDF Journal |
| **11:00 AM** | 🐍 **Python Mastery** | Advanced Python Architecture + Code Snippet + Quiz + PDF |
| **1:00 PM** | 💼 **FAANG Interview Prep** | Realistic Technical Question + Optimal Solution + Quiz + PDF |
| **2:00 PM** | ⚡ **JavaScript / TypeScript Pro** | Modern JS/TS Mechanics + Production Code + Quiz + PDF |
| **6:00 PM** | 🤖 **AI / ML Engineering** | Machine Learning Math/Architecture + PyTorch/Sklearn Code + Quiz + PDF |
| **9:00 PM** | 🔓 **Cyber Security & Bug Bounty** | Exploit Logic & Defensive Hardening Script + Quiz + PDF |

---

## 📈 Telegram Channel SEO & Growth Guide

Looking to grow your Telegram channel and understand how top creators gain thousands of organic subscribers?
👉 Read our comprehensive guide: **[TELEGRAM_SEO_GROWTH_GUIDE.md](./TELEGRAM_SEO_GROWTH_GUIDE.md)**

Learn how to:
1. Optimize your Channel Title & Bio for Telegram's In-App Global Search.
2. Maximize forwardability with clean, copy-pasteable code blocks.
3. Index your posts on Google Search via `t.me/s/kreggscode`.
4. Register for free on Telegram directories (TGStat, Telemetr, Lyzem).
5. Leverage cross-promotion (SFS) and GitHub repository badges.

---

## 🛠️ Local Setup & Quickstart

```bash
# Clone the repository
git clone https://github.com/kreggscode/Telegram-AI-Coding-Channel-Bot.git
cd Telegram-AI-Coding-Channel-Bot

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run a test cycle locally
python -m src.main
```

### Environment Variables (`.env`)
```env
BOT_TOKEN=your_telegram_bot_token_from_botfather
CHAT_ID=@kreggscode_or_channel_id
POLLINATIONS_API_KEY=your_pollinations_api_key
AI_MODEL=gemini-fast
TIMEZONE_OFFSET_HOURS=5.5
```

---

## 📁 Project Architecture

```
Telegram-AI-Coding-Channel-Bot/
├── .github/workflows/          # GitHub Actions scheduled automation
│   ├── auto-post.yml           # Multi-track daily posting cron
│   └── keepalive.yml           # Heartbeat to keep GitHub cron alive
├── dashboard/                  # Flask web dashboard for manual posting
│   ├── app.py                  # Dashboard server
│   └── templates/              # Dashboard HTML templates
├── src/                        # Core bot engine
│   ├── config.py               # Environment configuration & secret masking
│   ├── formatter.py            # Rock-solid Markdown to Telegram HTML converter
│   ├── magazine_generator.py   # Multi-page PDF magazine creator
│   ├── notes_generator.py      # Daily branded 1-page notes PDF generator
│   ├── pollinations_client.py  # LLM API integration with model fallback
│   ├── scheduler_logic.py      # Time-based track resolution
│   ├── telegram_client.py      # Telegram API client with HTML & quiz support
│   └── templates.py            # Structured prompt templates & SEO hashtags
├── requirements.txt            # Python dependencies
├── TELEGRAM_SEO_GROWTH_GUIDE.md# Telegram growth blueprint
└── README.md                   # Project documentation
```

---

## 📄 License
MIT License. Built for the **@kreggscode** developer community.
