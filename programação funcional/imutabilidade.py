from calendar import mdays, month_name
from functools import reduce
from os import system


indices = list(filter(lambda indice: mdays[indice] == 31, range(1,13)))
meses_com_31 = list(map(lambda indice: month_name[indice], indices))
system('cls')
print(
    reduce(lambda todos, nome_do_mes: f'{todos} \n- {nome_do_mes}', meses_com_31, 'Meses com 31 dias: '))

print(
    reduce(
            lambda todos, nome_do_mes: f'{todos} \n- {nome_do_mes}', 
        map(
            lambda indice: month_name[indice],
        filter(
            lambda indice: mdays[indice] == 31, range(1, 13)
            )
        ), 'Meses com 31 dias: '
    )
)


print('MESES COM 31 DIAS: ')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'-{month_name[mes]}')






