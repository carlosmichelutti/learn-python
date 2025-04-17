from calendar import mdays, month_name
from functools import reduce

def mes_com_31(mes): return mdays[mes] == 31

def nome_do_mes(mes): return month_name[mes]

def juntas_meses(todos, nome_mes): return f'{todos} \n- {nome_mes}'

print(reduce(juntas_meses, map(nome_do_mes, filter(mes_com_31, range(1, 13))), 'Meses com 31 dias: '))