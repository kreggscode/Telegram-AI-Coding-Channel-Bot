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
    You can tweak this easily.

    Returns one of:
    - "python_text"
    - "js_text"
    - "ml_text"
    - "clean_code_text"
    - "image_plus_text"
    - "poll"
    - "thread"
    """
    hour = get_local_hour_24()

    if 6 <= hour < 10:
        return "python_text"
    elif 10 <= hour < 13:
        return "js_text"
    elif 13 <= hour < 16:
        return "ml_text"
    elif 16 <= hour < 19:
        return "image_plus_text"
    elif 19 <= hour < 21:
        return "poll"
    else:
        return "thread"  # late evening / night
