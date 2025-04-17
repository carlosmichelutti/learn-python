grupo = []
auxiliar = []
maior = []
menor = []
nomesmaior =[]
nomesmenor = []
cont= 0

while True:
    nome = str(input('ESCREVA O NOME: '))
    peso = float(input('ESCREVA O PESO: '))
    auxiliar.append(nome)
    auxiliar.append(peso)
    grupo.append(auxiliar[:])
    auxiliar.clear()
    print(grupo)

    if cont == 0:
        maior.append(grupo[cont][1])
        nomesmaior.append(grupo[cont][0])
        menor.append(grupo[cont][1])
        nomesmenor.append(grupo[cont][0])
        cont = cont +1

    elif grupo[cont][1] > maior[0]:
        maior.pop()
        maior.append(grupo[cont][1])
        nomesmaior.pop()
        nomesmaior.append(grupo[cont][0])
        cont = cont + 1

    elif grupo[cont][1] == maior[0]:
        nomesmaior.insert(1, grupo[cont][0])
        cont = cont + 1
    
    elif grupo[cont][1] < menor[0]:
        menor.pop()
        menor.append(grupo[cont][1])
        nomesmenor.pop()
        nomesmenor.append(grupo[cont][0])
        cont = cont + 1
    
    elif grupo[cont][1] == menor[0]:
        nomesmenor.insert(1, grupo[cont][0])
        cont = cont + 1
    

#VERIFICAÇÃO DE RESPOSTA DE CONTINUAÇÃO ---------------------------------------

    resp = str(input("QUER CONTINUAR? [S/N]: ")).upper().strip()

    if resp == 'N':
        print('FORAM CADASTRADAS {} PESSOAS.'.format(len(grupo)))
        print('O MAIOR PESO REGISTRADO FOI DE {}. KG PESO DE {}.'.format(maior, nomesmaior))
        print('O MENOR PESO REGISTRADO FOI DE {}. KG PESO DE {}.'.format(menor, nomesmenor))
        break
    
    
    elif resp != 'S':
        print('RESPOSTA INVÁLIDA! TENTE NOVAMRNTE :')
        resp = str(input("QUER CONTINUAR? [S/N]: ")).upper().strip()
