from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROME_TZ = ZoneInfo("Europe/Rome")

def to_local(date: datetime, tz=ROME_TZ) -> datetime:
    if date.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware")
    
    return date.astimezone(tz)

def display_date(date: datetime) -> str:
    return date.strftime("%d/%m/%Y %H:%M")