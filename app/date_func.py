from datetime import date
from app import holidays
from app.holidays import holidays
from random import choice
from app.quotes import *
from random import choice






def countdown(holiday):
    check_holiday = check_holiday_exists(holiday)
    if check_holiday is False:
        return ("I dont know that holiday")
    today = date.today()
    holidate = date(today.year, holidays[holiday][0], holidays[holiday][1])

    if holidate < today:
        holidate = holidate.replace(year=today.year + 1)
    days_to_holidate = abs(holidate - today).days
    random_quote = get_random_quote(holiday)
    return (f'{days_to_holidate} till {holiday}. {random_quote}')


def get_random_quote(holiday):
    holiday_quote = HOLIDAY_QUOTES[holiday]
    random_quote = choice(holiday_quote)
    return random_quote


def check_holiday_exists(holiday):
    return holiday in holidays
