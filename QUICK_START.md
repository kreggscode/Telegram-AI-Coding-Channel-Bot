# Quick Start Commands

## 🚀 To Push to GitHub (Run these commands):

```bash
# 1. Create a new repository on GitHub first, then run:
git remote add origin https://github.com/YOUR_USERNAME/telegram-ai-coding-channel.git
git branch -M main
git push -u origin main
```

## 🧪 To Test Locally:

```bash
# 1. Create .env file from template
cp .env.example .env

# 2. Edit .env with your BOT_TOKEN and CHAT_ID

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the bot
python -m src.main
```

## 🎨 To Run Dashboard:

```bash
cd dashboard
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:5000
```

## 📋 GitHub Secrets to Add:

After pushing to GitHub, go to Settings → Secrets and variables → Actions:

1. `BOT_TOKEN` - Your Telegram bot token
2. `CHAT_ID` - Your channel ID (negative number)
3. `TIMEZONE_OFFSET_HOURS` - Your timezone offset (e.g., 5.5 for IST)

---

For detailed instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)
