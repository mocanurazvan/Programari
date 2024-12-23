import calendar
from datetime import date, timedelta
from django import template

register = template.Library()

@register.simple_tag
def get_next_month_weeks():
    today = date.today()
    current_year = today.year
    current_month = today.month

    # Calculate the next month
    if current_month == 12:  # If December, roll over to January next year
        next_month = 1
        year = current_year + 1
    else:
        next_month = current_month + 1
        year = current_year

    # Generate calendar for the next month
    cal = calendar.Calendar(firstweekday=1)
    month_days = cal.monthdayscalendar(year, next_month)

    # Remove zeros (padding days from other months)
    month_weeks = [[day for day in week if day != 0] for week in month_days]

    return month_weeks
