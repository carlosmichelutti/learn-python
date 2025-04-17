while True:
    tabuada = int(input('ESCREVA UM NÚMERO PARA CALCULAR A SUA TABUADA: '))

    if tabuada > -1:
        cont = 1
    else:
        print('VALOR INVALIDO. ENCERRANDO')
        break

    while cont < 11:
        print('{} X {} = {}'.format(tabuada, cont, tabuada*cont))
        cont = cont + 1
   

        
    

