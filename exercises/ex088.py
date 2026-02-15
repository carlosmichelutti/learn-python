from calendar import mdays, month_name
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

months_with_31 = list(map(lambda index: month_name[index] if mdays[index] == 31 else None, range(1, 13)))
months_with_31 = list(filter(lambda month_name_item: month_name_item is not None, months_with_31))
print('Months with 31 days:', *[month.capitalize() for month in months_with_31], sep='\n    * ')
