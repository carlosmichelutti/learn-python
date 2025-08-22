lista_simples = []
lista_impares = []
lista_pares = []
pos = 0
while True:
    numero = int(input('Digite um número qualquer: '))
    lista_simples.append(numero)
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resposta == 'N':
        while True:
            if lista_simples[pos] % 2 == 0:
                lista_pares.append(lista_simples[pos])
                pos += 1
            elif lista_simples[pos] % 2 == 1:
                lista_impares.append(lista_simples[pos])
                pos += 1
            if pos == len(lista_simples):
                break

        print(f'A lista normal digitada foi essa: {lista_simples}.')
        print(f'A lista dos números ímpares foi essa: {lista_impares}.')
        print(f'A lista dos números pares foi essa: {lista_pares}.')
        break

    elif resposta != 'S':
        print('Resposta inválida. Tente novamente.')
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
