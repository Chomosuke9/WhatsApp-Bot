from datetime import datetime, timedelta, timezone
from Configs import time_zone

time_zone = 0 - time_zone
def get_remaining_seconds():
    now = datetime.now(timezone.utc)  # Waktu saat ini dengan timezone UTC
    time_19 = datetime(now.year, now.month, now.day, 4, 0, tzinfo=timezone.utc)
    time_19 += timedelta(hours=time_zone)
    time_difference = time_19 - now
    remaining_seconds = int(time_difference.total_seconds())
    remaining_seconds += 86400
    if remaining_seconds < 0:
        remaining_seconds += 86400
    return remaining_seconds

print(get_remaining_seconds())
if __name__ == "__main__":
    print(get_remaining_seconds())