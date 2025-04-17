num = list()

maior = 0
menor = 0
posiçãomenor = 0
posiçãomaior = 0 


for c in range (0, 5):
    num.append(int(input('DIGITE UM VALOR PARA A POSIÇÃO {}: '.format(c))))
    if c == 0:
        maior = num[c]
        menor = num[c]

    if num[c] > maior:
        maior = num[c]

    elif num[c] < menor:
        menor = num[c]

print(num)
print('O MENOR NÚMERO DIGITADO FOI O {} NAS POSIÇÕES '.format(menor), end='')
for i, v in enumerate (num):
    if v == menor:
        print ('{}...'.format(i))

print('O MAIOR NÚMERO DIGITADO FOI O {} NAS POSIÇÕES '.format(maior), end='')
for i, v in enumerate (num):
    if v == maior:
        print('{}...'.format(i), end='')