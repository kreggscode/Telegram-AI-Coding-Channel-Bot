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
    - "tech_bundle" (All technical Tracks combined)
    """
    hour = get_local_hour_24()

    # Early Morning: Daily Magazine (8 AM)
    if 6 <= hour < 10:
        return "magazine"
    
    # Rest of the day: Master Technical Bundle (Python, JS, ML, Security)
    elif 10 <= hour < 24:
        return "tech_bundle"
    
    else:
        return "tech_bundle" # Fallback to bundle for late night



