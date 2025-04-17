
soma = 0
qtd = 0
while True:
    num = int(input('ESCREVA UM NÚMERO INTEIRO QUALQUER [999 PARA PARAR]: '))
    if num == 999:
        break
    soma = soma + num
    qtd = qtd + 1
print('A SOMA DE TODOS OS {} NÚMEROS DIGITADOS É {}'.format(qtd, soma))