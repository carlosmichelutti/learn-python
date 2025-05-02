numeros_matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

soma_terceira_coluna = 0
maior = 0
soma = 0 

for linha in range(0, 3):
    for coluna in range(0, 3):
        numeros_matriz[linha][coluna] = int(input(f'DIGITE UM VALOR PARA [{linha}, {coluna}]: '))

for linha in range (0, 3):
    for coluna in range(0, 3):
        if numeros_matriz[linha][coluna] % 2 == 0:
            soma = soma + numeros_matriz[linha][coluna]

for linha in range(0, 3):
    soma_terceira_coluna = soma_terceira_coluna + numeros_matriz[linha][2]

for coluna in range(0, 3):
    if coluna == 0:
        maior = numeros_matriz[1][coluna]

    elif numeros_matriz[1][coluna] > maior:
        maior = numeros_matriz[1][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{numeros_matriz[linha][coluna]:^5}]', end=' ')
    print('')

print(f'A soma dos números pares da matriz é igual a {soma}.')
print(f'A soma dos números da 3 coluna é igual a {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha foi o número {maior}.')
