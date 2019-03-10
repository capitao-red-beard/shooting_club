import datetime
import re


def is_int(i):
    if int(i):
        return True


def is_float(i):
    return isinstance(i, float)


def is_string(i):
    return isinstance(i, str)


def is_knsa(i):
    if is_int(i):
        if len(i) == 5 or len(i) == 6:
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
