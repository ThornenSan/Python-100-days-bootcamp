import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(now, type(now))
print(year, type(year))
print(day_of_week, type(day_of_week))

# Create datetime
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
