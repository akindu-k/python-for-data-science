from datetime import date
from datetime import datetime
my_date = date(2002,5,29)

print("Date passed as argument is %s"% my_date)

today = date.today()

print("today's date is %s"% today)

print("Current year:  %s" % today.year)
print("Current month: %s" % today.month)
print("Current day: %s" % today.day)


date_time = datetime.fromtimestamp(1887639468)
print("datetime from timestamp: %s" % date_time)

