numero = list()
cont = 0
numerosemordem = []

for c in range(0, 5):
    numero = int(input('DIGITE UM NÚMERO QUALQUER: '))
    print('')

    if c == 0 or numero > numerosemordem[-1]:
        numerosemordem.append(numero)
    else:
        pos = 0

        while pos < len(numerosemordem):
            if numero <= numerosemordem[pos]:
                numerosemordem.insert(pos, numero)
                break
            pos = pos + 1

    if numero > 0:
            print('ADICIONANDO NO COMEÇO DA LISTA...')
            
    elif numero > 6:
            print("ADICIONANDO NO FINAL DA LISTA.")

print('A LISTA EM ORDEM É ESSA {}'. format(numerosemordem ))

