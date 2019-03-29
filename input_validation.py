import datetime
import re
from datetime import date
from datetime import timedelta

from geopy.geocoders import Nominatim


def dates_in_range(i):
    start_date = date.today() + datetime.timedelta(-date.today().weekday() - 1)
    end_date = date.today() + datetime.timedelta(-date.today().weekday(), weeks=i)
    return [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]


def date_range(i):
    return [date.today() + datetime.timedelta(-date.today().weekday() - 1),
            date.today() + datetime.timedelta(-date.today().weekday(), weeks=i)]


def date_from_today(i):
    return date.today() + datetime.timedelta(-date.today().weekday(), weeks=i)


def date_from_human(i):
    return datetime.datetime.strptime(i, '%d-%m-%Y').date()


def date_to_human(i):
    return datetime.datetime.strptime(i, '%Y-%m-%d').date().strftime('%d-%m-%Y')


def is_date(i):
    try:
        datetime.datetime.strptime(i, '%Y-%m-%d')
    except ValueError:
        return False


def is_int(i):
    if isinstance(i, int):
        return True
    else:
        return False


def is_float(i):
    return isinstance(i, float)


def is_string(i):
    return isinstance(i, str)


def is_knsa(i):
    if is_int(i):
        if len(i) not in range(5, 7):
            return False
        else:
            return True


def is_email(i):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", i):
        return False
    else:
        return True


def is_phone_number(i):
    if len(i) != 10:
        return False
    else:
        return True


def is_password(i):
    if len(i) < 8:
        return False
    else:
        return True


def is_address(address, city, post_code):
    details = '{}, {}, {}'.format(address, city, post_code)
    geolocator = Nominatim(user_agent='shooting_club')
    location = geolocator.geocode(details)
    return location
