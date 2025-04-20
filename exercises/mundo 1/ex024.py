from datetime import datetime

ano = int(input('Escreva o ano atual ou digite 0 para escrever o ano atual: '))

if ano == 0:
    ano = datetime.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano especial, é bissexto e possui 366 dias.')
else:
    print(f'O ano {ano} é um ano comum, e não é um ano bissexto.')
