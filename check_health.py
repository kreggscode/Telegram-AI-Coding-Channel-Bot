import requests
import os
from src.config import BOT_TOKEN, CHAT_ID, POLLINATIONS_API_KEY, AI_MODEL, mask_secret

def test_telegram():
    print(f"Testing Telegram API...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            print(f"✅ Telegram: OK (Bot: {resp.json().get('result', {}).get('username')})")
        else:
            print(f"❌ Telegram: FAILED ({resp.status_code}) - {resp.text}")
    except Exception as e:
        print(f"❌ Telegram: EXCEPTION - {e}")

def test_pollinations():
    print(f"Testing Pollinations AI API...")
    url = "https://gen.pollinations.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {POLLINATIONS_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": AI_MODEL,
        "messages": [{"role": "user", "content": "ping"}],
        "max_tokens": 5
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        if resp.status_code == 200:
            print(f"✅ Pollinations: OK (Model: {AI_MODEL})")
        else:
            print(f"❌ Pollinations: FAILED ({resp.status_code}) - {resp.text}")
    except Exception as e:
        print(f"❌ Pollinations: EXCEPTION - {e}")

if __name__ == "__main__":
    print("=== BOT ROBUSTNESS CHECK ===")
    print(f"BOT_TOKEN: {mask_secret(BOT_TOKEN)}")
    print(f"CHAT_ID: {CHAT_ID}")
    print(f"POLLINATIONS_KEY: {mask_secret(POLLINATIONS_API_KEY)}")
    print("----------------------------")
    test_telegram()
    test_pollinations()
    print("============================")
