numero = list()
cont = 0
numerosemordem = []

for c in range (0,5):
    numero = int(input('DIGITE UM NÚMERO QUALQUER: '))
    print('')

    if c == 0:
        numerosemordem.insert(numero, numero)
        aux = c
        cont = cont + 1

    else:

        if numero < numerosemordem[0]:
            numerosemordem.insert(0, numero)
            aux = c
            cont = cont + 1

        else:

            if numerosemordem[0] in numerosemordem:
                numerosemordem.insert(1, numero)
            else:
                if numero > numerosemordem[2]:
                    numerosemordem.insert(1, numero)
                    aux = c
                    cont = cont + 1

        
        if numero > 0:
            print('ADICIONANDO NO COMEÇO DA LISTA...')

        elif numero < 6:
                print('ADICIONANDO NO COMEÇO DA LISTA...')
            
        elif numero >= 6:
                print("ADICIONANDO NO FINAL DA LISTA.")

print('A LISTA EM ORDEM É ESSA')





        
