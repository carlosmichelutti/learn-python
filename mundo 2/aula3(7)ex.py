resp = 'S'
maior = 0
menor = 0
qtd = 0
soma = 0

#INICIO DA CONDIÇÃO
while resp == 'S':
#PERGUNTANDO UM NÚMERO QUALQUER E MANIPULANDO ELE DA FORMA QUE FOI REQUERIDA
    num = int(input('ESCREVA UM NÚMERO INTEIRO QUALQUER: '))
    qtd = qtd + 1
    soma = soma + num
    
    if qtd == 1:
        maior = num
        menor = num
    else:
#verificação de menor e maior ---------------------------------------------------------------------------
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

#perguntando se o usuário quer continuar

    resp =  str(input('QUER CONTINUAR? [S/N]')).upper().strip()
    print('')

#mostrando as informações 

print('A MÉDIA DE TODOS OS {} NÚMEROS DIGITADOS É {}.'.format(qtd,soma/qtd))
print('O MAIOR NÚMERO DIGITADO FOI O {}.'.format(maior))
print('O MENOR VALOR DIGITADO FOI O {}.'.format(menor))