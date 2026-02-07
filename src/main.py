from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES


def post_python_tip():
    prompt = TEXT_TEMPLATES["python_tip"]()
    text = ai.generate_text(prompt)
    if "AI generation failed" in text or "API Error" in text:
        print(f"FAILED: Python tip generation failed: {text}")
        return
    tg.send_text(text)
    print("SUCCESS: Python tip posted.")


def post_js_tip():
    prompt = TEXT_TEMPLATES["js_tip"]()
    text = ai.generate_text(prompt)
    if "AI generation failed" in text or "API Error" in text:
        print(f"FAILED: JS tip generation failed: {text}")
        return
    tg.send_text(text)
    print("SUCCESS: JS tip posted.")


def post_ml_tip():
    prompt = TEXT_TEMPLATES["ml_tip"]()
    text = ai.generate_text(prompt)
    if "AI generation failed" in text or "API Error" in text:
        print(f"FAILED: ML tip generation failed: {text}")
        return
    tg.send_text(text)
    print("SUCCESS: ML tip posted.")


def post_security_tip():
    prompt = TEXT_TEMPLATES["security_tip"]()
    text = ai.generate_text(prompt)
    if "AI generation failed" in text or "API Error" in text:
        print(f"FAILED: Security tip generation failed: {text}")
        return
    tg.send_text(text)
    print("SUCCESS: Security tip posted.")


def post_tech_news():
    prompt = TEXT_TEMPLATES["tech_news"]
    text = ai.generate_text(prompt)
    if "AI generation failed" in text or "API Error" in text:
        print(f"FAILED: Tech news generation failed: {text}")
        return
    tg.send_text(text)
    print("SUCCESS: Tech news posted.")


def post_image_plus_text():
    """Post an image with code snippet - rotates between JS, Python, ML"""
    import random
    
    # Rotate between different content types with matching images
    choices = [
        ("js_tip", "js_image"),
        ("python_tip", "python_image"),
        ("ml_tip", "ml_image"),
    ]
    text_key, img_key = random.choice(choices)
    
    text_prompt = TEXT_TEMPLATES[text_key]
    if callable(text_prompt):
        text_prompt = text_prompt()
        
    img_prompt = IMAGE_TEMPLATES[img_key]

    caption = ai.generate_text(text_prompt)
    if "AI generation failed" in caption or "API Error" in caption:
        print(f"FAILED: Image caption generation failed: {caption}")
        return
        
    img_url = ai.image_url(img_prompt)
    tg.send_photo(img_url, caption)
    print("SUCCESS: Image post posted.")


def post_poll():
    poll_prompt = TEXT_TEMPLATES["poll_question"]
    raw = ai.generate_text(poll_prompt)
    if "AI generation failed" in raw or "API Error" in raw:
        print(f"FAILED: Poll generation failed: {raw}")
        return

    # Expect format: "Question? | A, B, C"
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
        else:
            print("FAILED: Poll generation failed: not enough options.")
    else:
        print("FAILED: Poll generation failed: invalid format from AI.")


def post_thread():
    thread_prompt = TEXT_TEMPLATES["thread_explainer"]
    raw = ai.generate_text(thread_prompt)
    if "AI generation failed" in raw or "API Error" in raw:
        print(f"FAILED: Thread generation failed: {raw}")
        return
    # Split by double-newline into sections
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if len(parts) == 0:
        tg.send_text(raw)
    else:
        tg.send_thread(parts)


def post_daily_magazine():
    """Generate and post the 10-15 page daily magazine"""
    from .magazine_generator import create_magazine
    try:
        pdf_path = create_magazine()
        caption = "📖 *KREGGSCODE Daily Magazine*\n\nYour 15-page deep dive into Python, ML, and Architecture. Hand-crafted for the @kreggscode community. Enjoy! 🚀"
        tg.send_document(pdf_path, caption=caption)
        # We don't delete here to keep a local archive if needed, or we could cleanup
    except Exception as e:
        print(f"Error posting magazine: {e}")
        tg.send_text("Magazine generation failed today. We'll be back tomorrow!")


def main():
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    if post_type == "magazine":
        post_daily_magazine()
    elif post_type == "python_text":
        post_python_tip()
    elif post_type == "js_text":
        post_js_tip()
    elif post_type == "ml_text":
        post_ml_tip()
    elif post_type == "security_text":
        post_security_tip()
    elif post_type == "tech_news_text":
        post_tech_news()
    elif post_type == "image_plus_text":
        post_image_plus_text()
    elif post_type == "poll":
        post_poll()
    elif post_type == "thread":
        post_thread()

    else:
        print(f"INFO: No valid post type decided for current hour ({sched.get_local_hour_24()}).")


if __name__ == "__main__":
    main()
