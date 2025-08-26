numeros_em_ordem = []
for num in range(0, 5):
    numero = int(input('Digite um número qualquer: '))
    if num == 0 or numero > numeros_em_ordem[-1]:
        numeros_em_ordem.append(numero)
    else:
        position = 0
        while position < len(numeros_em_ordem):
            if numero <= numeros_em_ordem[position]:
                numeros_em_ordem.insert(position, numero)
                break
            position += 1

    if numero > 0 and numero < 6:
        print('Adicionando no começo da lista...')
    elif numero > 6:
        print('Adicionando no final da lista...')

print(f'A lista em ordem é essa: {numeros_em_ordem}')
