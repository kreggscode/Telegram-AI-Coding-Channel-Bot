import os
from flask import Flask, render_template, redirect, url_for, flash, request
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES, IMAGE_TEMPLATES, HASHTAGS

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

CURRENT_POST_TYPE = None

# Wrap tg.send_text to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_text = tg.send_text
def custom_send_text(text, parse_mode="Markdown"):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE and CURRENT_POST_TYPE != "thread":
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        text = text + tags
    return _original_send_text(text, parse_mode)
tg.send_text = custom_send_text

# Wrap tg.send_photo to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_photo = tg.send_photo
def custom_send_photo(image_url, caption=""):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE:
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        caption = caption + tags
    return _original_send_photo(image_url, caption)
tg.send_photo = custom_send_photo

# Wrap tg.send_document to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_document = tg.send_document
def custom_send_document(document_path, caption=""):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE:
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        caption = caption + tags
    return _original_send_document(document_path, caption)
tg.send_document = custom_send_document

@app.before_request
def set_post_type():
    global CURRENT_POST_TYPE
    path = request.path
    if path.startswith("/send/"):
        post_type = path.split("/")[-1].replace("-", "_")
        if post_type == "python_tip":
            post_type = "python"
        elif post_type == "js_tip":
            post_type = "javascript"
        elif post_type == "ml_tip":
            post_type = "ml"
        elif post_type == "security_tip":
            post_type = "security"
        elif post_type == "interview_tip":
            post_type = "interview"
        elif post_type == "image_post":
            post_type = "python"
        CURRENT_POST_TYPE = post_type


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
    """Rotates between JS, Python, ML images"""
    import random
    choices = [
        ("js_tip", "js_image"),
        ("python_tip", "python_image"),
        ("ml_tip", "ml_image"),
    ]
    text_key, img_key = random.choice(choices)
    
    caption = ai.generate_text(TEXT_TEMPLATES[text_key])
    img_url = ai.image_url(IMAGE_TEMPLATES[img_key])
    
    tg.send_photo(img_url, caption)
    flash(f"Image sent ({text_key})!", "success")
    return redirect(url_for("index"))


@app.route("/send/tech-news")
def send_tech_news():
    text = ai.generate_text(TEXT_TEMPLATES["tech_news"])
    tg.send_text(text)
    flash("Tech News sent!", "success")
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
        parts[-1] = parts[-1] + HASHTAGS.get("thread", "")
        tg.send_thread(parts)
        flash("Thread sent!", "success")
    else:
        flash("Thread generation failed.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
