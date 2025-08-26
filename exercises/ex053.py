print('=' * 50)
print('{:^50}'.format('Banco do brasil'))
print('=' * 50)

notas_de_50 = 0
notas_de_20 = 0
notas_de_10 = 0
notas_de_1 = 0 

saque = float(input('Quanto você quer sacar? '))

while True:
    if saque > 49:
        saque -= 50
        notas_de_50 += 1
    elif saque > 19:
        saque -= 20
        notas_de_20 += 1
    elif saque > 9:
        saque -= 10
        notas_de_10 += 1
    elif saque > 0:
        saque -= 1
        notas_de_1 += 1
    elif saque == 0:
        print(f'Total de cédulas de R$50 - {notas_de_50} cédulas.')
        print(f'Total de cédulas de R$20 - {notas_de_20} cédulas.')
        print(f'Total de cédulas de R$10 - {notas_de_10} cédulas.')
        print(f'Total de cédulas de R$1 - {notas_de_1} cédulas.')
        break
