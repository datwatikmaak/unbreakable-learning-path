from datetime import datetime, timedelta
from pprint import pprint

PYBITES_BORN = datetime(year=2016, month=12, day=19)
pprint(PYBITES_BORN)


def gen_special_pybites_dates():
    from_date = PYBITES_BORN + timedelta(days=100)
    while True:
        yield from_date
        from_date = from_date + timedelta(days=100)


gen_special_pybites_dates()
