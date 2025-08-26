auxiliar = []
grupo = []
maior = 0
menor = 0
while True:
    auxiliar.append(str(input('Nome: ')))
    auxiliar.append(float(input('Peso (KG): ')))
    if len(grupo) == 0:
        maior = auxiliar[1]
        menor = auxiliar[1]
    else:
        if auxiliar[1] > maior:
            maior = auxiliar[1]
        if auxiliar[1] < menor:
            menor = auxiliar[1]

    grupo.append(auxiliar[:])
    auxiliar.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta == 'N':
        print(f'Ao todo foram registradas {len(grupo)} pessoas.')
        print(f'O maior peso foi de {maior} kg, foi de ', end='')
        for pessoa in grupo:
            if pessoa[1] == maior:
                print(pessoa[0], end='.\n')

        print(f'O menor peso digitado foi de {menor} kg, foi de ', end='')
        for pessoa in grupo:
            if pessoa[1] == menor:
                print(pessoa[0], end='.\n')
        break

    elif resposta != 'S':
        print('Resposta inválida. Tente novamente: ')
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
