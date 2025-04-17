numeros = []
unicos = list()
while True:
    num = int(input('DIGITE UM NÚMERO QUALQUER: '))

    if num not in numeros:
        numeros.append(num)
    else:
        print('VALOR DUPLICADO.')


#CONDIÇÃO PARA ENCERRAR O WHILE -----------------------------------------------------
    resposta = str(input('QUER CONTINUAR? ')).upper().strip()

    if resposta == 'N':
        numeros.sort()
        print(numeros)
        print('ENCERRANDO...')

        break

    elif resposta != 'S':

        print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE.')
        resposta = str(input('QUER CONTINUAR? '))
    

