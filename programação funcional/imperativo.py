from calendar import mdays, month_name
from os import system

system('cls')

print('MESES COM 31 DIAS')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')