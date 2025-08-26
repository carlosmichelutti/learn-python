import random

numeros_sorteados = (
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10)
)

print(f'Os números sorteados foram: {numeros_sorteados}')

maior_numero = 0
menor_numero = 0

while True:

    if (numeros_sorteados[0]) == (numeros_sorteados[0]):
        maior_numero =  numeros_sorteados[0]
        menor_numero = numeros_sorteados[0]

    if (numeros_sorteados[1]) >  maior_numero:
        maior_numero = numeros_sorteados[1]

    elif (numeros_sorteados[1]) < menor_numero:
        menor_numero = numeros_sorteados[1]

    if (numeros_sorteados[2]) > maior_numero:
        maior_numero =  numeros_sorteados[2]

    elif (numeros_sorteados[2]) < menor_numero:
        menor_numero = numeros_sorteados[2]

    if (numeros_sorteados[3]) > maior_numero:
        maior_numero = numeros_sorteados[3]

    elif (numeros_sorteados[3]) < menor_numero:
        menor_numero = numeros_sorteados[3]

    if (numeros_sorteados[4]) > maior_numero:
        maior_numero = numeros_sorteados[4]

    elif (numeros_sorteados[4]) < menor_numero:
        menor_numero = numeros_sorteados[4]
    break

print(f'O maior valor sorteado foi o {maior_numero}.')
print(f'O menor valor sorteado foi o {menor_numero}.')
