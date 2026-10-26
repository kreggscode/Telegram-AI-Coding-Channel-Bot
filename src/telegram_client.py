import json
import re
import requests
from .config import BOT_TOKEN, CHAT_ID
from .formatter import markdown_to_telegram_html, plain_text_fallback_formatter, safe_truncate_html

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def add_social_footer(text: str) -> str:
    """Add sleek, executive social media footer with emojis and hyperlinked channels."""
    if "Connect with kreggscode" in text or "Connect with @kreggscode" in text:
        return text

    footer = """

━━━━━━━━━━━━━━━━━━━━
🚀 **Connect with @kreggscode:**

💬 [Telegram Community](https://t.me/kreggscode) • 📷 [Instagram](https://instagram.com/kreggscode)
✖️ [X / Twitter](https://x.com/kreggscode) • ▶️ [YouTube](https://youtube.com/@kreggscode)
📘 [Facebook](https://www.facebook.com/share/1b95f6Sn3c/) • 🎮 [Play Store Apps](https://play.google.com/store/apps/dev?id=4822923174061161987)
⭐ [GitHub Repositories](https://github.com/kreggscode)
━━━━━━━━━━━━━━━━━━━━"""
    return text.rstrip() + footer


def _post_message_with_retry(data: dict):
    """
    Helper to post sendMessage with resilient retry.
    Guarantees that <pre><code> code blocks and 1-click Copy buttons are ALWAYS preserved!
    """
    url = f"{BASE_URL}/sendMessage"
    try:
        resp = requests.post(url, data=data, timeout=30)
    except Exception as e:
        print(f"EXCEPTION: Telegram sendMessage connection failed: {e}")
        return None

    if resp.status_code != 200:
        print(f"ERROR: Telegram sendMessage failed ({resp.status_code}): {resp.text[:300]}")
        # If Telegram rejects HTML entities (e.g. invalid tag nesting):
        if resp.status_code == 400 and data.get("parse_mode") == "HTML":
            print("LOG: Retrying with simplified HTML (preserving code blocks and copy buttons)...")
            # Strip inline tags (<b>, <i>, <a>, <blockquote>) that may have caused entity errors,
            # but STRICTLY PRESERVE <pre><code ...>!
            simplified = re.sub(r"</?(?:b|i|u|s|a|blockquote)[^>]*>", "", data.get("text", ""))
            data["text"] = simplified
            try:
                resp2 = requests.post(url, data=data, timeout=30)
                if resp2.status_code == 200:
                    print("LOG: Message sent successfully with code block intact!")
                    return resp2
            except Exception as e2:
                print(f"EXCEPTION on retry: {e2}")

        # Absolute last resort: convert <pre> to triple backticks so Telegram renders as Markdown code block
        print("LOG: Last resort fallback with code blocks...")
        raw = data.get("text", "")
        # Convert pre to markdown backticks
        raw = re.sub(r"<pre><code[^>]*>", "\n```\n", raw)
        raw = re.sub(r"</code></pre>", "\n```\n", raw)
        raw = re.sub(r"</?[a-zA-Z0-9]+[^>]*>", "", raw)
        data["text"] = raw[:3950]
        data.pop("parse_mode", None)
        try:
            return requests.post(url, data=data, timeout=30)
        except Exception:
            return resp
    else:
        print("LOG: Message sent successfully to Telegram with syntax-highlighted code blocks")
    return resp


def send_text(text: str, add_footer: bool = True, parse_mode: str = "HTML", post_type: str = None):
    """
    Send formatted message to Telegram channel in ONE clean, complete post.
    Defaults to HTML parse mode with automatic syntax-highlighted code blocks,
    copy code button, and clickable hyperlinks.
    """
    if post_type:
        from .templates import HASHTAGS
        tags = HASHTAGS.get(post_type, "")
        if tags and "#" not in text[-150:]:
            text = text.rstrip() + tags

    if add_footer:
        text = add_social_footer(text)

    if parse_mode == "HTML":
        payload_text = markdown_to_telegram_html(text)
        if len(payload_text) > 4000:
            payload_text = safe_truncate_html(payload_text, max_chars=3950)
    else:
        payload_text = text[:4000]

    data = {
        "chat_id": CHAT_ID,
        "text": payload_text,
        "parse_mode": parse_mode
    }
    return _post_message_with_retry(data)


def send_photo(image_url: str, caption: str = "", add_footer: bool = True, parse_mode: str = "HTML", post_type: str = None):
    """Send photo with beautifully formatted HTML caption (up to 1024 chars)."""
    if post_type:
        from .templates import HASHTAGS
        tags = HASHTAGS.get(post_type, "")
        if tags and "#" not in caption[-150:]:
            caption = caption.rstrip() + tags

    if add_footer and caption:
        caption = add_social_footer(caption)

    if parse_mode == "HTML" and caption:
        caption = markdown_to_telegram_html(caption)
        caption = safe_truncate_html(caption, max_chars=1020)

    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": parse_mode
    }
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200 and resp.status_code == 400:
            data["caption"] = re.sub(r"</?[a-zA-Z0-9]+[^>]*>", "", caption)[:1020]
            data.pop("parse_mode", None)
            resp = requests.post(url, data=data, timeout=30)
        return resp
    except Exception as e:
        print(f"EXCEPTION: Telegram sendPhoto failed: {e}")
        return None


def send_poll(question: str, options: list[str]):
    """Send an interactive multiple-choice poll."""
    safe_q = (question[:295] + "...") if len(question) > 300 else question
    safe_opts = [((o[:95] + "...") if len(o) > 100 else o) for o in options[:10]]
    if len(safe_opts) < 2:
        print("ERROR: send_poll requires at least 2 options")
        return None

    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": safe_q,
        "options": json.dumps(safe_opts),
        "is_anonymous": True
    }
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"ERROR: Telegram sendPoll failed ({resp.status_code}): {resp.text}")
        return resp
    except Exception as e:
        print(f"EXCEPTION: Telegram sendPoll failed: {e}")
        return None


def send_quiz(question: str, options: list[str], correct_option_id: int, explanation: str = ""):
    """Send an interactive quiz with HTML explanation."""
    safe_q = (question[:295] + "...") if len(question) > 300 else question
    safe_opts = [((o[:95] + "...") if len(o) > 100 else o) for o in options[:10]]
    if len(safe_opts) < 2:
        print("ERROR: send_quiz requires at least 2 options")
        return None

    safe_correct = max(0, min(correct_option_id, len(safe_opts) - 1))

    safe_expl = ""
    if explanation:
        safe_expl = markdown_to_telegram_html(explanation.strip())
        if len(safe_expl) > 200:
            safe_expl = safe_truncate_html(safe_expl, max_chars=195)

    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": safe_q,
        "options": json.dumps(safe_opts),
        "type": "quiz",
        "correct_option_id": safe_correct,
        "explanation": safe_expl,
        "explanation_parse_mode": "HTML",
        "is_anonymous": True
    }

    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code != 200:
            print(f"ERROR: Telegram sendQuiz failed ({resp.status_code}): {resp.text[:300]}")
            if resp.status_code == 400 and safe_expl:
                data["explanation"] = re.sub(r"</?[a-zA-Z0-9]+[^>]*>", "", safe_expl)[:195]
                data.pop("explanation_parse_mode", None)
                resp2 = requests.post(url, data=data, timeout=30)
                if resp2.status_code == 200:
                    return resp2
                data.pop("explanation", None)
                return requests.post(url, data=data, timeout=30)
        return resp
    except Exception as e:
        print(f"EXCEPTION: Telegram sendQuiz failed: {e}")
        return None


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)


def send_document(file_path: str, caption: str = "", add_footer: bool = True, parse_mode: str = "HTML", post_type: str = None):
    """Send document (PDF/file) with HTML-formatted caption (up to 1024 chars)."""
    if post_type:
        from .templates import HASHTAGS
        tags = HASHTAGS.get(post_type, "")
        if tags and "#" not in caption[-150:]:
            caption = caption.rstrip() + tags

    if add_footer and caption:
        caption = add_social_footer(caption)

    if parse_mode == "HTML" and caption:
        caption = markdown_to_telegram_html(caption)
        caption = safe_truncate_html(caption, max_chars=1020)

    url = f"{BASE_URL}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            files = {"document": f}
            data = {
                "chat_id": CHAT_ID,
                "caption": caption,
                "parse_mode": parse_mode
            }
            resp = requests.post(url, data=data, files=files, timeout=60)
            if resp.status_code != 200:
                print(f"ERROR: Telegram sendDocument failed ({resp.status_code}): {resp.text[:300]}")
                if resp.status_code == 400:
                    data["caption"] = re.sub(r"</?[a-zA-Z0-9]+[^>]*>", "", caption)[:1020]
                    data.pop("parse_mode", None)
                    f.seek(0)
                    resp = requests.post(url, data=data, files=files, timeout=60)
            else:
                print(f"LOG: Document {file_path} sent successfully to Telegram")
            return resp
    except Exception as e:
        print(f"EXCEPTION sending document: {e}")
        return None
