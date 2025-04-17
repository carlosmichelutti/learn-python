n1 = int(input('ESCREVA UM NÚMERO: '))
n2 = int(input('ESCREVA OUTRO NÚMERO: '))
maior = 0
cont = 0


while cont != 5:
    print('=+='*10)
    print('''ESCOLHA O QUE FAZER COM OS NÚMEROS DIGITADOS
    [1] SOMA-LOS
    [2] MULTIPLICA-LOS
    [3] MOSTRAR O MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA.''')
    cont = int(input('ESCOLHA UMA OPÇÃO: '))
    

#verificando a condição 1 ---------------------------------------------

    if cont == 1:
        print('A SOMA DE {} E {} É IGUAL A {}.'.format(n1, n2, n1+n2))
        print('')
        cont = 0

#verificando a condição 2 ---------------------------------------------

    if cont == 2:
        print('A MULTIPLICAÇÃO ENTRE {} E {} É IGUAL A {}.'.format(n1, n2, n1*n2))
        print('')
        cont = 0

#verificando a condição 3 ---------------------------------------------

    if cont == 3:
        if n1 > n2:
            print('O NÚMERO {} É MAIOR.'.format(n1))
        elif n2 > n1:
            print('O NÚMERO {} É MAIOR.'.format(n2))
        elif n2 == n1:
            print('OS NÚMEROS SÃO IGUAIS. ')
        print('')
        cont = 0

#Verificando condição 4 ------------------------------

    if cont == 4:
        n1 = int(input('ESCREVA UM NOVO NÚMERO: '))
        n2 = int(input('ESCREVA OUTRO NOVO NÚMERO: '))
        cont = 0 

#Verificando condição 5 ------------------------------

    if cont == 5:
        print('FIM')






