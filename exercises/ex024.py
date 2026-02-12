from datetime import datetime

year = int(input('Enter a year, or type 0 for the current year: '))

if year == 0:
    year = datetime.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'The year {year} is a leap year and has 366 days.')
else:
    print(f'The year {year} is a common year, not a leap year.')
