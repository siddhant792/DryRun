from datetime import datetime, timedelta


def get_submission_interval(created_at: timedelta) -> str:
    time_difference = datetime.now() - created_at
    if time_difference.days > 0:
        days = time_difference.days
        if days <= 30:
            return "less than a month ago"
        elif days < 365:
            return str(int(days/30)) + " months" + " ago"
        else:
            return "more than a year ago"
    else:
        seconds = time_difference.seconds
        if seconds < 60:
            return "a few seconds ago"
        elif int(seconds/60) < 60: 
            return str(int(seconds/60)) + " minute" + ("s" if int(seconds/60) > 1 else "") + " ago"
        else:
            return str(int(seconds/3600)) + " hour" + ("s" if int(seconds/3600) > 1 else "") + " ago"
