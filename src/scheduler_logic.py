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
    - "python_text"
    - "js_text"
    - "ml_text"
    - "clean_code_text"
    - "thread" (fallback for late night)
    """
    hour = get_local_hour_24()

    # Morning: Python tips with code (8 AM)
    if 6 <= hour < 10:
        return "python_text"
    
    # Afternoon: JavaScript tips with code (1 PM)
    elif 10 <= hour < 16:
        return "js_text"
    
    # Evening: ML/AI with code examples (6 PM)
    elif 16 <= hour < 20:
        return "ml_text"
    
    # Night: Clean Code examples (9 PM)
    elif 20 <= hour < 24:
        return "clean_code_text"
    
    # Late Night/Early Morning: Thread explainer (fallback)
    else:
        return "thread"



