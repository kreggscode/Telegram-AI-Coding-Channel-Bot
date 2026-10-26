from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour (IST).
    
    Schedule (IST):
    - 8:10 AM: Daily Technical Magazine
    - 11:00 AM: Python Mastery
    - 1:00 PM: LeetCode Problem of the Day (POTD)
    - 2:00 PM: JavaScript & TypeScript Pro
    - 6:00 PM: AI & ML Engineering
    - 9:00 PM: Cyber Security & Bug Bounty
    """
    hour = get_local_hour_24()

    if 6 <= hour < 10:
        return "magazine"
    elif 10 <= hour < 12:
        return "python"
    elif 12 <= hour < 14:
        return "leetcode"
    elif 14 <= hour < 16:
        return "javascript"
    elif 16 <= hour < 19:
        return "ml"
    elif 19 <= hour < 24:
        return "security"
    else:
        return "magazine"
