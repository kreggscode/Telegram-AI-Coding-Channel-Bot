import os
import re
from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, HASHTAGS, get_current_day

print("LOG: Bot Intelligence v2.3 Activated (LeetCode POTD, Robust Quiz Parser & Executive Notes)")


def parse_quiz_options(raw_opts_str: str, quiz_block: str) -> list[str]:
    """
    Robustly extract 2-10 options without splitting on grammatical commas
    inside option text.
    """
    # 1. Bracketed options: [Option 1], [Option 2, with comma], [Option 3]
    bracketed = re.findall(r"\[([^\]]+)\]", raw_opts_str)
    if len(bracketed) >= 2:
        return [b.strip() for b in bracketed if b.strip()][:10]

    # 2. Pipe-separated options: Option 1 | Option 2, with comma | Option 3
    if "|" in raw_opts_str:
        pipe_opts = [p.strip().strip("[]'\"") for p in raw_opts_str.split("|") if p.strip()]
        if len(pipe_opts) >= 2:
            return pipe_opts[:10]

    # 3. Quoted options: "Opt 1", "Opt 2, with comma", "Opt 3"
    quoted = re.findall(r'["\']([^"\']+)["\']', raw_opts_str)
    if len(quoted) >= 2:
        return [q.strip() for q in quoted if q.strip()][:10]

    # 4. Multiline options: A) Option 1 \n B) Option 2, with comma
    multiline_opts = re.findall(r"^[ \t]*(?:[A-Da-d\d][\.\)\:\-]|[•\-])\s*(.+)$", quiz_block, re.MULTILINE)
    if len(multiline_opts) >= 2:
        return [m.strip().strip("[]'\"") for m in multiline_opts if m.strip()][:10]

    # 5. Comma-split only when followed by option letters (e.g. , B) or , C))
    labeled_split = re.split(r",\s*(?=[A-Da-d\d][\.\)\:\-])", raw_opts_str)
    if len(labeled_split) >= 2:
        return [re.sub(r"^[A-Da-d\d][\.\)\:\-]\s*", "", o).strip() for o in labeled_split if o.strip()][:10]

    # 6. Fallback comma split
    raw_split = [o.strip().strip("[]'\"") for o in raw_opts_str.split(",") if o.strip()]
    if len(raw_split) >= 2:
        return raw_split[:10]

    return []


def extract_quiz_data(content: str):
    """
    Robust extraction of [QUIZ] ... [/QUIZ] blocks using regex.
    Handles optional asterisks around [QUIZ] and ensures main_text has no dangling asterisks.
    Returns (main_text_without_quiz, quiz_dict_or_None).
    """
    quiz_data = None
    main_text = content

    match = re.search(r"(?:\*\*)?\[QUIZ\](?:\*\*)?(.*?)(?:\[/QUIZ\](?:\*\*)?|$)", content, flags=re.DOTALL | re.IGNORECASE)

    if match:
        quiz_block = match.group(1).strip()
        main_text = (content[:match.start()] + content[match.end():]).strip()
        # Clean any trailing bold markers or whitespace from main_text
        main_text = re.sub(r"\*\*+\s*$", "", main_text).strip()

        q, raw_opts, correct, expl = "", "", 0, ""
        for line in quiz_block.split("\n"):
            line = line.strip()
            if not line:
                continue
            lower_line = line.lower()
            if lower_line.startswith("question:"):
                q = line.split(":", 1)[1].strip()
            elif lower_line.startswith("options:"):
                raw_opts = line.split(":", 1)[1].strip()
            elif lower_line.startswith("correct:"):
                m = re.search(r"(\d+)", line)
                if m:
                    correct = int(m.group(1))
            elif lower_line.startswith("explanation:"):
                expl = line.split(":", 1)[1].strip()

        # Parse options safely without comma splitting
        opts = parse_quiz_options(raw_opts, quiz_block)

        if q and len(opts) >= 2:
            quiz_data = {
                "question": q,
                "options": opts,
                "correct_option_id": correct,
                "explanation": expl
            }

    return main_text, quiz_data


def post_technical_bundle():
    """Consolidated 4-Course Elite Bundle cleanly formatted without code truncation."""
    topics = [
        ("Python Mastery", TEXT_TEMPLATES["python_tip"]),
        ("LeetCode POTD", TEXT_TEMPLATES["leetcode_tip"]),
        ("JS Pro", TEXT_TEMPLATES["js_tip"]),
        ("ML Engineering", TEXT_TEMPLATES["ml_tip"]),
        ("Cyber Security", TEXT_TEMPLATES["security_tip"])
    ]
    
    day = get_current_day()
    header = (
        f"🚀 **KREGGSCODE ELITE DAILY BUNDLE - DAY {day}**\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
    )
    
    sections = []
    for name, prompt_fn in topics:
        try:
            print(f"LOG: Generating {name} for bundle...")
            content = ai.generate_text(prompt_fn())
            if "AI generation failed" in content or "API Error" in content:
                print(f"WARNING: Topic {name} failed. Skipping in bundle.")
                continue
            clean_content, _ = extract_quiz_data(content)
            sections.append(clean_content)
        except Exception as e:
            print(f"ERROR: Exception generating {name}: {e}")

    if not sections:
        print("FAILED: All topics in bundle failed generation.")
        return

    separator = "\n\n━━━━━━━━━━━━━━━━━━━━\n\n"
    full_message = header + separator.join(sections)
    
    if len(full_message) <= 3800:
        tg.send_text(full_message, post_type="tech_bundle")
    else:
        print("LOG: Bundle is large, splitting into clean parts...")
        midpoint = len(sections) // 2
        part1 = header + separator.join(sections[:midpoint])
        part2 = f"🚀 **KREGGSCODE ELITE BUNDLE (PART 2) - DAY {day}**\n━━━━━━━━━━━━━━━━━━━━\n\n" + separator.join(sections[midpoint:])
        tg.send_text(part1, post_type="tech_bundle")
        tg.send_text(part2, post_type="tech_bundle")

    print("SUCCESS: Technical Bundle posted.")


def post_single_topic(topic_key: str):
    """Generate and post a single technical topic with code copy button, interactive quiz, and cheat sheet."""
    topic_map = {
        "ai": ("AI & LLM Engineering", TEXT_TEMPLATES["ai_tip"]),
        "python": ("Python Mastery", TEXT_TEMPLATES["python_tip"]),
        "leetcode": ("LeetCode Problem of the Day", TEXT_TEMPLATES["leetcode_tip"]),
        "fullstack": ("Modern Fullstack & TS Pro", TEXT_TEMPLATES["fullstack_tip"]),
        "security": ("Cyber Security & Bug Bounty", TEXT_TEMPLATES["security_tip"]),
        "interview": ("FAANG Interview Prep", TEXT_TEMPLATES["interview_tip"]),
        "javascript": ("JS & TS Pro", TEXT_TEMPLATES["fullstack_tip"]),
        "ml": ("AI & ML Engineering", TEXT_TEMPLATES["ai_tip"])
    }
    
    if topic_key not in topic_map:
        print(f"ERROR: Unknown topic key {topic_key}")
        return

    name, prompt_fn = topic_map[topic_key]
    try:
        print(f"LOG: Generating {name} with Interactive Quiz...")
        content = ai.generate_text(prompt_fn())
        if "AI generation failed" in content or "API Error" in content:
            print(f"ERROR: AI generation failed for {name}.")
            return
        
        # Robust Quiz & Content Extraction
        main_text, quiz_data = extract_quiz_data(content)

        # 1. Post Main Technical Lesson (Syntax Highlighted Code & Copy Button)
        print(f"LOG: Posting {name} lesson...")
        resp_text = tg.send_text(main_text, post_type=topic_key)
        text_ok = resp_text is not None and resp_text.status_code == 200

        # 2. Post Interactive Quiz Poll
        quiz_ok = True
        if quiz_data:
            print(f"LOG: Sending Quiz for {name} ({len(quiz_data['options'])} options)...")
            resp_quiz = tg.send_quiz(**quiz_data)
            quiz_ok = resp_quiz is not None and resp_quiz.status_code == 200
        else:
            print(f"INFO: No quiz block parsed for {name}.")

        # 3. Generate & Post Modern Executive Cheat Sheet PDF
        day = get_current_day()
        try:
            from .notes_generator import generate_notes
            pdf_path = generate_notes(topic_key, day, main_text)
            print(f"LOG: Sending Executive Cheat Sheet PDF to Telegram...")
            tg.send_document(
                pdf_path,
                caption=f"📄 **{name} - Reference Cheat Sheet (Day {day})**\n\nDaily high-performance architecture reference for the @kreggscode community.",
                post_type=topic_key
            )
        except Exception as e:
            print(f"WARNING: Notes PDF generation failed (non-fatal): {e}")

        if text_ok and quiz_ok:
            print(f"SUCCESS: {name} posted successfully.")
        else:
            print(f"WARNING: {name} - text_ok={text_ok}, quiz_ok={quiz_ok}")

    except Exception as e:
        print(f"ERROR: Exception generating {name}: {e}")


def post_daily_magazine():
    """Generate and post the daily magazine PDF."""
    try:
        from .magazine_generator import create_magazine
        pdf_path = create_magazine()
        caption = (
            "📖 **KREGGSCODE Daily Magazine**\n\n"
            "Your comprehensive deep-dive into Software Architecture, Python & AI Systems. "
            "Hand-crafted for the @kreggscode developer community. Enjoy! 🚀"
        )
        tg.send_document(pdf_path, caption=caption, post_type="magazine")
        print("SUCCESS: Daily Magazine posted.")
    except Exception as e:
        print(f"Error posting magazine: {e}")
        tg.send_text("Magazine generation failed today. We'll be back tomorrow!", post_type="magazine")


def main():
    import os
    override = os.getenv("POST_TYPE_OVERRIDE")
    if override and override.strip():
        post_type = override.strip()
        print(f"LOG: Manually overriding post type to: {post_type}")
    else:
        post_type = sched.decide_post_type()
    
    print(f"Decided post type: {post_type}")

    if post_type == "magazine":
        post_daily_magazine()
    elif post_type in ["ai", "python", "leetcode", "fullstack", "security", "interview", "javascript", "ml"]:
        post_single_topic(post_type)
    elif post_type == "tech_bundle":
        post_technical_bundle()
    else:
        print(f"INFO: No valid post type decided for current hour ({sched.get_local_hour_24()}).")


if __name__ == "__main__":
    main()
