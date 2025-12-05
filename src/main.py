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


def post_tech_news():
    prompt = TEXT_TEMPLATES["tech_news"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


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
    img_prompt = IMAGE_TEMPLATES[img_key]

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
    elif post_type == "tech_news_text":
        post_tech_news()
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
