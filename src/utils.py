from datetime import datetime

def get_current_datetime():
    #  Return the current date and time.
    return datetime.now()

def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Spring"
    elif month in [6,7,8]:
        return "Summer"
    return "Autumn"

def is_weekend(date):
    """
    Return True if the given date falls on a weekend.
    """
    return date.weekday() >= 5