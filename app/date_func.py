from datetime import date
from app import holidays
from app.holidays import holidays
from random import choice
from app.quotes import XMAS_QUOTE


def countdown(holiday):
    today = date.today()
    holidate = date(today.year, holidays[holiday][0], holidays[holiday][1])

    if holidate < today:
        holidate = holidate.replace(year=today.year + 1)
    days_to_holidate = abs(holidate - today).days
    random_quote = choice(XMAS_QUOTE)
    return (f'{days_to_holidate} till {holiday}. {random_quote}')



