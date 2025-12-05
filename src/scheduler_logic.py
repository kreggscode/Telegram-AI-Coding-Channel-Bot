from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour.
    Updated for 5 posts per day with better engagement.

    Returns one of:
    - "python_text"
    - "js_text"
    - "ml_text"
    - "clean_code_text"
    - "tech_news_text"
    - "image_plus_text"
    - "poll"
    - "thread"
    - "motivational_tip"
    """
    hour = get_local_hour_24()

    # Morning: Python tips with code (6-10 AM)
    if 6 <= hour < 10:
        return "python_text"
    
    # Late Morning: JavaScript with image (10 AM - 1 PM)
    elif 10 <= hour < 13:
        return "image_plus_text"
    
    # Afternoon: ML/AI with code examples (1-4 PM)
    elif 13 <= hour < 16:
        return "ml_text"
    
    # Late Afternoon: Tech News (4-7 PM)
    elif 16 <= hour < 19:
        return "tech_news_text"
    
    # Evening: Clean Code or Poll (7-10 PM)
    elif 19 <= hour < 22:
        return "clean_code_text"
    
    # Late Night: Motivational/Career Tips (10 PM - 12 AM)
    elif 22 <= hour < 24:
        return "motivational_tip"
    
    # Very Late Night/Early Morning: Thread explainer (12 AM - 6 AM)
    else:
        return "thread"


