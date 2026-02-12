from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES

print("LOG: Bot Intelligence v2.1 Activated")


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


def post_single_topic(topic_key: str):
    """Generate and post a single technical topic with an interactive quiz."""
    topic_map = {
        "python": ("Python Mastery", TEXT_TEMPLATES["python_tip"]),
        "javascript": ("JS Pro", TEXT_TEMPLATES["js_tip"]),
        "ml": ("ML Engineering", TEXT_TEMPLATES["ml_tip"]),
        "security": ("Cyber Security", TEXT_TEMPLATES["security_tip"])
    }
    
    if topic_key not in topic_map:
        print(f"ERROR: Unknown topic key {topic_key}")
        return

    name, prompt_fn = topic_map[topic_key]
    try:
        print(f"LOG: Generating {name} with Quiz...")
        content = ai.generate_text(prompt_fn())
        if "AI generation failed" in content or "API Error" in content:
            print(f"ERROR: AI generation failed for {name}.")
            return
        
        # Robust Quiz Parsing
        main_text = content
        quiz_data = None
        
        if "[QUIZ]" in content and "[/QUIZ]" in content:
            try:
                parts = content.split("[QUIZ]")
                main_text = parts[0].strip()
                quiz_block = parts[1].split("[/QUIZ]")[0].strip()
                
                q, opts, correct, expl = "", [], 0, ""
                for line in quiz_block.split("\n"):
                    line = line.strip()
                    if line.lower().startswith("question:"): q = line.split(":", 1)[1].strip()
                    elif line.lower().startswith("options:"): 
                        # Handle comma or bracket separated options
                        raw_opts = line.split(":", 1)[1].strip()
                        opts = [o.strip().strip("[]") for o in raw_opts.split(",")]
                    elif line.lower().startswith("correct:"):
                        import re
                        m = re.search(r"(\d)", line)
                        if m: correct = int(m.group(1))
                    elif line.lower().startswith("explanation:"): expl = line.split(":", 1)[1].strip()

                if q and len(opts) >= 2:
                    # Telegram Limits: Question 255, Option 100, Explanation 200
                    quiz_data = {
                        "question": (q[:250] + "...") if len(q) > 255 else q,
                        "options": [((o[:95] + "...") if len(o) > 100 else o) for o in opts[:10]],
                        "correct_option_id": correct,
                        "explanation": (expl[:195] + "...") if len(expl) > 200 else expl
                    }
            except Exception as pe:
                print(f"WARNING: Quiz parsing error: {pe}")

        # Send Content
        tg.send_text(main_text)
        
        # Send Quiz if available
        if quiz_data:
            print(f"LOG: Sending Quiz for {name}...")
            tg.send_quiz(**quiz_data)
            
        print(f"SUCCESS: {name} posted.")
    except Exception as e:
        print(f"ERROR: Exception generating {name}: {e}")


def post_daily_magazine():
    """Generate and post the daily magazine PDF"""
    """Generate and post the daily magazine PDF"""
    try:
        from .magazine_generator import create_magazine
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
    elif post_type in ["python", "javascript", "ml", "security"]:
        post_single_topic(post_type)
    elif post_type == "tech_bundle":
        post_technical_bundle()
    else:
        print(f"INFO: No valid post type decided for current hour ({sched.get_local_hour_24()}).")


if __name__ == "__main__":
    main()
