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
    Updated for better engagement with more images and variety.

    Returns one of:
    - "python_text"
    - "js_text"
    - "ml_text"
    - "clean_code_text"
    - "tech_news_text"
    - "image_plus_text"
    - "poll"
    - "thread"
    """
    hour = get_local_hour_24()

    # Morning: Python tips with code (6-10 AM)
    if 6 <= hour < 10:
        return "python_text"
    
    # Late Morning: JavaScript with image (10 AM - 1 PM)
    elif 10 <= hour < 13:
        return "image_plus_text"  # Changed from plain js_text
    
    # Afternoon: ML/AI with code examples (1-4 PM)
    elif 13 <= hour < 16:
        return "ml_text"  # Now includes code snippets
    
    # Late Afternoon: Tech News (4-6 PM)
    elif 16 <= hour < 18:
        return "tech_news_text"
    
    # Evening: Clean Code or Image (6-8 PM)
    elif 18 <= hour < 20:
        return "clean_code_text"
    
    # Night: Poll (8-10 PM)
    elif 20 <= hour < 22:
        return "poll"
    
    # Late Night: Thread explainer (10 PM - 6 AM)
    else:
        return "thread"

