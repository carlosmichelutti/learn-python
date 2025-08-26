numeros = list()

maior_numero = 0
menor_numero = 0

for num in range (0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {num}: ')))
    if num == 0:
        maior_numero = numeros[num]
        menor_numero = numeros[num]

    if numeros[num] > maior_numero:
        maior_numero = numeros[num]

    elif numeros[num] < menor_numero:
        menor_numero = numeros[num]

print(f'Números: {numeros}')
print(f'O menor número digitado foi o {menor_numero} nas posições {', '.join(str(i) for i, v in enumerate(numeros) if v == menor_numero)}')
print(f'O maior número digitado foi o {maior_numero} nas posições {', '.join(str(i) for i, v in enumerate(numeros) if v == maior_numero)}')
