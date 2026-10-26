from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS


def get_local_now() -> datetime:
    """Return current local datetime based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    return now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)


def get_local_hour_24() -> int:
    """Return current local hour (0-23)."""
    return get_local_now().hour


def decide_post_type() -> str:
    """
    High-Signal Publishing Cadence (IST):
    - Morning (07:00 - 11:00):
        Sunday -> 'magazine' (Weekly Comprehensive Journal)
        Mon/Wed/Fri/Sun -> 'ai' (Generative AI & LLM Systems)
        Tue/Thu/Sat -> 'python' (Advanced Python Backend Architecture)
    - Midday (11:00 - 16:00):
        'leetcode' (FAANG LeetCode Problem of the Day)
    - Evening (16:00 - 23:59):
        'fullstack' (Modern TypeScript / Fullstack Systems) or 'security'
    """
    now = get_local_now()
    hour = now.hour
    weekday = now.weekday()  # 0=Monday, 6=Sunday

    if 6 <= hour < 11:
        if weekday == 6:  # Sunday morning magazine
            return "magazine"
        elif weekday in (0, 2, 4):  # Mon, Wed, Fri -> AI
            return "ai"
        else:  # Tue, Thu, Sat -> Python
            return "python"
    elif 11 <= hour < 16:
        return "leetcode"
    elif 16 <= hour < 24:
        return "fullstack" if weekday % 2 == 0 else "security"
    else:
        return "ai"
