import pytz
from pytz import timezone

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes"""
    now_aware = pytz.utc.localize(naive_utc_dt)

    australia = now_aware.astimezone(pytz.timezone("Australia/Sydney"))
    spain = now_aware.astimezone(pytz.timezone("Europe/Madrid"))

    return australia, spain
