from datetime import datetime
import time

def dt():

    # datetime object containing current date and time
    now = datetime.now()

    print(type(now))
    # dd/mm/YY H:M:S
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))

    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    second = int(now.strftime("%S"))

    date_time = (year, month, day, hour, minute, second, 1, 48, 0) 

    format = "%b %d %Y,  %r"

    datetime_str = time.mktime(date_time) 

    dateTime = time.strftime(format, time.gmtime(datetime_str)) 

    return dateTime

