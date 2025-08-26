quantidade_numeros = 0
lista = []
while True:
    numero = int(input('Digite um número qualquer: '))
    lista.append(numero)
    quantidade_numeros += 1
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()

    if resposta == 'N':
        print('')
        print(f'Foram digitados {quantidade_numeros} números.')
        lista.sort(reverse=True)
        print(f'A lista em ordem decrescente é igual a {lista}.')
        break

    elif resposta != 'S':
        print('Resposta inválida. Tente novamente')
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()
