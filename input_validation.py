import datetime
import re
from datetime import date
from datetime import timedelta


def dates_in_range(i):
    start_date = date.today() + datetime.timedelta(-date.today().weekday() - 1)
    end_date = date.today() + datetime.timedelta(-date.today().weekday(), weeks=i)

    return [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]


def date_range(i):
    return [date.today() + datetime.timedelta(-date.today().weekday() - 1),
            date.today() + datetime.timedelta(-date.today().weekday(), weeks=i)]


def convert_date(i):
    return datetime.datetime.strptime(i, '%d-%m-%Y').date()


def is_int(i):
    if int(i):
        return True


def is_float(i):
    return isinstance(i, float)


def is_string(i):
    return isinstance(i, str)


def is_knsa(i):
    if is_int(i):
        if len(str(i)) == 5 or len(str(i)) == 6:
            return True


def is_date(i):
    try:
        datetime.datetime.strptime(i, '%Y-%m-%d')
    except ValueError:
        return False


def is_email(i):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", i):
        return False


def is_password(i):
    if len(i) < 8:
        return False
