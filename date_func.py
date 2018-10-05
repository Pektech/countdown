from datetime import date



def countdown_xmas():
    today = date.today()
    xmas = date(today.year, 12, 25)
    if xmas < today:
        xmas = xmas.replace(year=today.year + 1)
    days_to_xmas = abs(xmas - today).days
    return days_to_xmas



