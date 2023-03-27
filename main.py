import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
if year == 2020:
    print("The planned pandemic has begun")
if year == 2023:
    print("The year is 2023, the fall of the global banking system has begun")
print(year)
print(month)
print(day_of_the_week)

date_of_birth = dt.datetime(year=1980, month=12, day=31)
print(f"You were born on {date_of_birth}, you are old as hell!")

