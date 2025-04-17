grupo = []
auxiliar = []
maior = 0
menor = 0

while True:
    auxiliar.append(str(input('NOME: ')))
    auxiliar.append(float(input('PESO (KG): ')))

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

    resp = str(input('VOCÊ QUER CONTINUAR? [S/N]: '))

    if resp == 'N':

        print('AO TODO FORAM REGISTRADAS {} PESSOAS.'.format(len(grupo)))
        print('O MAIOR PESO FOI DE {} KG, FOI DE '.format(maior), end='')
        
        for p in grupo:
            if p[1] == maior:
                print('{}, '.format(p[0]), end='')
        print('')

        print('O MENOR PESO DIGITADO FOI DE {} KG, FOI DE '.format(menor), end='')
        
        for p in grupo:
            if p[1] == menor:
                print('{}, '.format(p[0]), end='')
        break
    

    elif resp != 'S':
        print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE: ')
        resp = str(input('VOCÊ QUER CONTINUAR? [S/N]: '))
