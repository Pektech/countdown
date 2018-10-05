from datetime import date
import holidays
from holidays import holidays



def countdown(holiday):
    today = date.today()
    holidate = date(today.year, holidays[holiday][0], holidays[holiday][1])

    if holidate < today:
        holidate = holidate.replace(year=today.year + 1)
    days_to_holidate = abs(holidate - today).days
    return (f'{days_to_holidate} till {holiday}')



