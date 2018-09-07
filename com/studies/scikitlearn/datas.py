import datetime
import calendar

# start_date='2017-03-01'
start_date = datetime.datetime.strptime('2017-03-01', '%Y-%m-%d')
start_date1 = datetime.date(start_date.year, start_date.month,
                            calendar.monthrange(start_date.year, start_date.month)[1])
end_date = datetime.datetime.strptime('2018-03-01', '%Y-%m-%d')
end_date = datetime.date(end_date.year, end_date.month, end_date.day)
d = start_date1
while d <= end_date:
    print(d.strftime("%Y-%m-%d"))
    if d.month == 12:
        delta = datetime.timedelta(days=calendar.monthrange(d.year, (d.month + 1) % 12)[1])
        d += delta
    else:
        delta = datetime.timedelta(days=calendar.monthrange(d.year, (d.month + 1))[1])
        d += delta
