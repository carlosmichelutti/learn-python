from calendar import mdays, month_name
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

meses_com_31 = list(map(lambda indice: month_name[indice] if mdays[indice] == 31 else None, range(1, 13)))
meses_com_31 = list(filter(lambda nome_do_mes: nome_do_mes is not None, meses_com_31))
print('Meses com 31 dias:', *[mes.capitalize() for mes in  meses_com_31], sep='\n    * ')
