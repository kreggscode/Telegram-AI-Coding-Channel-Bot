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
    Updated for 4 posts per day - ALL CODE FOCUSED, TEXT ONLY.

    Returns one of:
    - "magazine" (8 AM)
    - "python_text" (11 AM)
    - "js_text" (2 PM)
    - "ml_text" (6 PM)
    - "clean_code_text" (9 PM)
    - "thread" (Late night)
    """
    hour = get_local_hour_24()

    # Early Morning: Daily Magazine (8 AM)
    if 7 <= hour < 10:
        return "magazine"
    
    # Late Morning: Python tips with code (11 AM)
    elif 10 <= hour < 13:
        return "python_text"
    
    # Afternoon: JavaScript tips with code (2 PM)
    elif 13 <= hour < 17:
        return "js_text"
    
    # Evening: ML/AI with code examples (6 PM)
    elif 17 <= hour < 20:
        return "ml_text"
    
    # Night: Clean Code examples (9 PM)
    elif 20 <= hour < 24:
        return "clean_code_text"
    
    # Late Night/Early Morning: Thread explainer (fallback)
    else:
        return "thread"



