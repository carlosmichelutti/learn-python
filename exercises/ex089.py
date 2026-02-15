from calendar import mdays, month_name
from functools import reduce
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

def month_has_31(month: int) -> bool:
    return mdays[month] == 31

def get_month_name(month: int) -> str:
    return month_name[month]

def join_months(accumulated: str, month_name_str: str) -> str:
    return f'{accumulated}\n    * {month_name_str.capitalize()}'

print(reduce(join_months, map(get_month_name, filter(month_has_31, range(1, 13))), 'Months with 31 days:'))
