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
    if resp.status_code != 200:
        print(f"ERROR: Telegram sendMessage failed ({resp.status_code}): {resp.text}")
    return resp


def send_photo(image_url: str, caption: str = ""):
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Telegram sendPhoto failed ({resp.status_code}): {resp.text}")
    return resp


def send_poll(question: str, options: list[str]):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": True
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Telegram sendPoll failed ({resp.status_code}): {resp.text}")
    return resp


def send_quiz(question: str, options: list[str], correct_option_id: int, explanation: str = ""):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "type": "quiz",
        "correct_option_id": correct_option_id,
        "explanation": explanation,
        "explanation_parse_mode": "Markdown",
        "is_anonymous": True
    }
    resp = requests.post(url, data=data)
    if resp.status_code != 200:
        print(f"ERROR: Telegram sendQuiz failed ({resp.status_code}): {resp.text}")
    return resp


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)


def send_document(file_path: str, caption: str = ""):
    url = f"{BASE_URL}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            files = {"document": f}
            data = {
                "chat_id": CHAT_ID,
                "caption": caption,
                "parse_mode": "Markdown"
            }
            resp = requests.post(url, data=data, files=files)
            if resp.status_code != 200:
                print(f"ERROR: Telegram sendDocument failed ({resp.status_code}): {resp.text}")
            return resp
    except Exception as e:
        print(f"EXCEPTION sending document: {e}")
        return None
