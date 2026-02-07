import os

from dotenv import load_dotenv

# Load .env when running locally; in GitHub Actions env vars are set directly
load_dotenv(override=False)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "").strip()
TIMEZONE_OFFSET_HOURS = float(os.getenv("TIMEZONE_OFFSET_HOURS", "5.5"))

# Default AI Model for better performance
# Options: gemini-fast, openai, qwen-coder, gemini-large, claude, mistral, deepseek
AI_MODEL = os.getenv("AI_MODEL", "gemini-fast").strip()

# Secret verification for logs (masked)
def mask_secret(s):
    if not s: return "MISSING"
    return s[:4] + "*" * (len(s) - 8) + s[-4:] if len(s) > 8 else "****"

print(f"--- CONFIG VERIFICATION ---")
print(f"BOT_TOKEN: {mask_secret(BOT_TOKEN)}")
print(f"CHAT_ID: {CHAT_ID}")
print(f"POLLINATIONS_API_KEY: {mask_secret(POLLINATIONS_API_KEY)}")
print(f"AI_MODEL: {AI_MODEL}")
print(f"---------------------------")

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("BOT_TOKEN or CHAT_ID is not set. Check your environment or .env file.")

# Course tracking logic (Stateless 'Day X' calculation)
# We calculate days since this date to show "Day 1", "Day 2", etc.
COURSE_START_DATE = "2026-02-01" 
