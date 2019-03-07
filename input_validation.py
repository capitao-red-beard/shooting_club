import datetime


def is_int(i):
    return i.isdigit()


def is_float(i):
    return isinstance(i, float)


def is_string(i):
    return isinstance(i, str)


def is_knsa(i):
    if i.length() == 6:
        return True


def is_date(i):
    try:
        datetime.datetime.strptime(i, '%Y-%m-%d')
    except ValueError:
        return False


def is_email(i):
    if '@' not in i:
        return False
