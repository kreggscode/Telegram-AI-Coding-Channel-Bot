from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES


def post_technical_bundle():
    """Consolidated 4-Course Elite Bundle in a single message."""
    topics = [
        ("Python Mastery", TEXT_TEMPLATES["python_tip"]),
        ("JS Pro", TEXT_TEMPLATES["js_tip"]),
        ("ML Engineering", TEXT_TEMPLATES["ml_tip"]),
        ("Cyber Security", TEXT_TEMPLATES["security_tip"])
    ]
    
    from .templates import get_current_day
    day = get_current_day()
    
    header = f"🚀 **KREGGSCODE ELITE DAILY - DAY {day}**\n"
    header += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    sections = []
    for name, prompt_fn in topics:
        try:
            print(f"LOG: Generating {name} for bundle...")
            content = ai.generate_text(prompt_fn())
            if "AI generation failed" in content or "API Error" in content:
                print(f"WARNING: Topic {name} failed. Skipping in bundle.")
                continue
            sections.append(content)
        except Exception as e:
            print(f"ERROR: Exception generating {name}: {e}")

    if not sections:
        print("FAILED: All topics in bundle failed generation.")
        return

    # Join with distinct separators
    separator = "\n\n" + "─" * 20 + "\n\n"
    full_message = header + separator.join(sections)
    
    # Cap at Telegram's 4096 limit just in case
    if len(full_message) > 4000:
        full_message = full_message[:3997] + "..."

    tg.send_text(full_message)
    print("SUCCESS: Technical Bundle posted.")


def post_daily_magazine():
    """Generate and post the daily magazine PDF"""
    from .magazine_generator import create_magazine
    try:
        pdf_path = create_magazine()
        caption = "📖 *KREGGSCODE Daily Magazine*\n\nYour deep-dive into Python, ML, and Architecture. Hand-crafted for the @kreggscode community. Enjoy! 🚀"
        tg.send_document(pdf_path, caption=caption)
    except Exception as e:
        print(f"Error posting magazine: {e}")
        tg.send_text("Magazine generation failed today. We'll be back tomorrow!")


def main():
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    if post_type == "magazine":
        post_daily_magazine()
    elif post_type == "tech_bundle":
        post_technical_bundle()
    else:
        print(f"INFO: No valid post type decided for current hour ({sched.get_local_hour_24()}).")


if __name__ == "__main__":
    main()
