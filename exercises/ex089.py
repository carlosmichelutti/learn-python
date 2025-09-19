from calendar import mdays, month_name
from functools import reduce
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

def mes_com_31(mes: int) -> bool:
    return mdays[mes] == 31

def nome_do_mes(mes: int) -> str:
    return month_name[mes]

def juntar_meses(todos: str, nome_mes: str) -> str:
    return f'{todos}\n    * {nome_mes.capitalize()}'

print(reduce(juntar_meses, map(nome_do_mes, filter(mes_com_31, range(1, 13))), 'Meses com 31 dias:'))
