# Day 16 of 30 Days of Python

# ---------------------
# | Exercises Level 1 |
# ---------------------

# Part 1
from datetime import datetime
now = datetime.now()
print(now)

print(f'Time today: {now.year}/{now.month}/{now.day}, {now.hour}:{now.minute}')

# Part 2: Formatting Current Time
formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f'Formatted Time: {formatted_time}')

# Part 3: String to Datetime
str_time = '5 December, 2019'
datetime_object = datetime.strptime(str_time, "%d %B, %Y")
print(datetime_object)

# Part 4: Time Difference Pt 1
from datetime import date
new_year = date(year=2025, month=1, day=1)
today = date(year=2024, month=7,  day=27)

print(f'Time left in new year: {new_year - today}')

# Part 4: Time Difference Pt 2
past_date = date(year=1970, month=1, day=1)

print(f'Difference: {today - past_date}')
