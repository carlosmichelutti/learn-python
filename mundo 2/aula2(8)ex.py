
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('ESCREVA O PESO DA {}º PESSOA: '.format(c)))
    if peso > maior:
        maior = peso
        menor = peso
    elif peso < menor: 
        menor = peso
print(' ')
print('O MAIOR PESO LIDO FOI {}KG.'.format(maior))
print('O MENOR PESO LIDO FOI {}KG.'.format(menor)) 
    