import os

numero1 = int(input('Escreva um número: '))
numero2 = int(input('Escreva outro número: '))
condicao = 0

while True:
    print('Escolha o que fazer com os números digitados: ')
    print('[1] Soma-los')
    print('[2] Multiplica-los')
    print('[3] Mostrar o maior')
    print('[4] Novos números')
    print('[5] Sair do programa.')
    condicao = int(input('Escolha uma opção: '))

    if condicao == 1:
        os.system('cls')
        print(f'A soma de {numero1} e {numero2} é igual a {numero1 + numero2}.')
        continue

    if condicao == 2:
        os.system('cls')
        print(f'A multiplicação entre {numero1} e {numero2} é igual a {numero1 * numero2}.')
        continue

    if condicao == 3:
        os.system('cls')
        if numero1 > numero2:
            print(f'O número {numero1} é maior que o número {numero2}.')
        elif numero2 > numero1:
            print(f'O número {numero2} é maior que o número {numero1}.')
        elif numero2 == numero1:
            print(f'Os números {numero1} e {numero2} são iguais.')
        continue

    if condicao == 4:
        os.system('cls')
        numero1 = int(input('Escreva um novo número: '))
        numero2 = int(input('Escreva outro novo número: '))
        continue

    if condicao == 5:
        print('FIM')
        break
