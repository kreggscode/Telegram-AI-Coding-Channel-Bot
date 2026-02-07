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
    - "security_text" (9 PM)
    - "thread" (Late night)
    """
    hour = get_local_hour_24()

    # Early Morning: Daily Magazine (8 AM)
    if 7 <= hour < 10:
        return "magazine"
    
    # Late Morning: Python mastery course (11 AM)
    elif 10 <= hour < 13:
        return "python_text"
    
    # Afternoon: JavaScript pro course (2 PM)
    elif 13 <= hour < 17:
        return "js_text"
    
    # Evening: AI/ML engineering course (6 PM)
    elif 17 <= hour < 20:
        return "ml_text"
    
    # Night: Cyber Security & Bug Bounty course (9 PM)
    elif 20 <= hour < 24:
        return "security_text"
    
    # Late Night/Early Morning: Thread explainer (fallback)
    else:
        return "thread"



