listasimples = []
listapares = []
listaimpares = []
pos = 0
while True:
    numero = int(input('ESCREVA UM NÚMERO QUALQUER: '))
    listasimples.append(numero)

#PERGUNTANDO E VERIFICANDO A RESPOSTA DE ENCERRADA ---------------------------------------------------------------------
    
    resposta = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

#VERIFICANDO SE CADA NÚMERO É PAR OU IMPAR E COLOCANDO EM SUAS RESPECTIVAS LISTAS ---------------------------------

    if resposta == 'N':
        
        while True:
            if listasimples[pos] % 2 == 0:
                listapares.append(listasimples[pos])
                pos += 1
                    

            elif listasimples[pos] % 2 == 1:
                listaimpares.append(listasimples[pos])
                pos += 1
            
            if pos == len(listasimples):
                break

    #ESCREVENDO AS INFORMAÇÕES ---------------------------------------------------------------------------------------------
        
        print('A LISTA NORMAL DIGITADA FOI ESSA: {}'.format(listasimples))
        print('A LISTA DOS NÚMEROS IMPERES FOI ESSA: {}'.format(listaimpares))
        print('A LISTA DOS NÚMEROS PARES FOI ESSA: {}'.format(listapares))
        print('')
        print('ENCERRANDO...')
        break

    elif resposta != 'S':
        print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE')
        print('')
        resposta = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
        print('')

        
        
        



