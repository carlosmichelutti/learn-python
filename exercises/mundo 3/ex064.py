nomes_menor = []
nomes_maior =[]
auxiliar = []
grupo = []
maior = []
menor = []
cont= 0

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    auxiliar.append(nome)
    auxiliar.append(peso)
    grupo.append(auxiliar[:])
    auxiliar.clear()
    if cont == 0:
        maior.append(grupo[cont][1])
        nomes_maior.append(grupo[cont][0])
        menor.append(grupo[cont][1])
        nomes_menor.append(grupo[cont][0])
        cont = cont +1

    elif grupo[cont][1] > maior[0]:
        maior.pop()
        maior.append(grupo[cont][1])
        nomes_maior.pop()
        nomes_maior.append(grupo[cont][0])
        cont = cont + 1

    elif grupo[cont][1] == maior[0]:
        nomes_maior.insert(1, grupo[cont][0])
        cont = cont + 1

    elif grupo[cont][1] < menor[0]:
        menor.pop()
        menor.append(grupo[cont][1])
        nomes_menor.pop()
        nomes_menor.append(grupo[cont][0])
        cont = cont + 1

    elif grupo[cont][1] == menor[0]:
        nomes_menor.insert(1, grupo[cont][0])
        cont = cont + 1

    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta == 'N':
        print(f'Foram cadastradas {len(grupo)} pessoas.')
        print(f'O maior peso registrado foi de {maior} kg peso de {nomes_maior}.')
        print(f'O menor peso registrado foi de {menor} kg peso de {nomes_menor}.')
        break

    elif resposta != 'S':
        print('Resposta inválida! Tente novamente:')
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
