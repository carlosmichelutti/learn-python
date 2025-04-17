import random

num = (random.randint(1, 10), random.randint(1, 10),
       random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), )

print('OS NÚMEROS SORTEADOS FORAM: {}'.format(num))

maior = 0
menor = 0

while True:

    if (num[0]) == (num[0]):
        maior =  num[0]
        menor = num[0]

    if (num[1]) >  maior:
        maior = num[1]

    elif (num[1]) < menor:
        menor = num[1]

    if (num[2]) > maior:
        maior =  num[2]

    elif (num[2]) < menor:
        menor = num[2]

    if (num[3]) > maior:
        maior = num[3]

    elif (num[3]) < menor:
        menor = num[3]

    if (num[4]) > maior:
        maior = num[4]

    elif (num[4]) < menor:
        menor = num[4]
    break
print('O MAIOR VALOR SORTEADO FOI O {}.'.format(maior))
print('O MENOR VALOR SORTEADO FOI O {}.'.format(menor))
