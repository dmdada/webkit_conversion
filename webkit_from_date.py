
import datetime
import random


def webkit_from_date(webkit):
    utc8 = datetime.timedelta(hours=8)
    epoch_start = datetime.datetime(1601, 1, 1)
    delta = datetime.timedelta(microseconds=int(webkit))
    delta += utc8
    print(epoch_start + delta)


def date_from_webkit(date):
    c = random.randint(1, 999999)
    epoch_start = datetime.datetime(1601, 1, 1)
    utc8 = datetime.timedelta(hours=8)
    timestamp = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - utc8
    webkit_timestamp = timestamp - epoch_start
    webkit_timestamp = webkit_timestamp.total_seconds()
    webkit_timestamp = str(webkit_timestamp)[0:-2] + str(c)
    print(webkit_timestamp)


date = '2023-02-03 08:34:23'
webkit = 13319858063844031

date_from_webkit(date)
webkit_from_date(webkit)