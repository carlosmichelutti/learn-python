numextenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
              'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
escolhauser = int(input('ESCOLHA UM NÚMERO ENTRE 0 E 20: '))
while True:
    if escolhauser > 20 or escolhauser < 0:
        escolhauser = int(
            input('NÚMERO INVALIDO! ESCOLHA UM NÚMERO ENTRE 0 E 20: '))
    else:
        break
print('O NÚMERO QUE VOCÊ ESCOLHEU POR EXTENSO É {}.'.format(numextenso[escolhauser]))
