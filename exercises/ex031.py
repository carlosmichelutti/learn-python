from datetime import datetime
from time import sleep

ano_nascimento = int(input('Escreva o seu ano de nascimento: '))
idade = datetime.today().year - ano_nascimento
print('Analisando a sua categoria de natação...')
sleep(3)

if idade <= 9:
    print('A sua categoria é a categoria mirim.')
elif idade <= 14:
    print('A sua categoria é a categoria infantil.')
elif idade <= 19:
    print('A sua categoria é a categoria junior.')
elif idade <= 25:
    print('A sua categoria é a categoria senior.')
elif idade > 25:
    print('A sua categoria é a categoria master.')
