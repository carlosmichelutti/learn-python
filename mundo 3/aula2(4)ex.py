
qtddenumeros = 0
lista = []

#INICIO DO LOOP INFINITO ATÉ O USUÁRIO NÃO QUERER CONTINUAR MAIS ---------------

while True:
    n = int(input('DIGITE UM NÚMERO QUALQUER: '))
    lista.append(n)

    qtddenumeros = qtddenumeros + 1

    resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

#VERIFICANDO SE O O USUÁRIO QUER OU NÃO CONTINUAR E ESCREVENDO AS INFORMAÇÕES -----    

    if resp == 'N':
        print('')

        print('FORAM DIGITADOS {} NÚMEROS'.format(len(lista)))

        lista.sort(reverse=True)

        print('A LISTA EM ORDEM DECRESCENTE É IGUAL A {}'.format(lista))
    
#VERIFICANDO SE O NÚMERO 5 ESTÁ NA LISTA ------------------------------------------    

        if 5 in lista:
            print('O VALOR 5 FAZ PARTE DA LISTA.')
        else:
            print('O VALOR 5 NÃO FOI ENCONTRADO NA LISTA.')

#ENCERRANDO -----------------------------------------------------------------------

        print('ENCERRANDO...')
        break
    
#VERIFICANDO RESPOSTA DIFERENTE DE 'S' --------------------------------------------

    elif resp != 'S':
        print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE')
        print('')
        resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip
        print('')



    
