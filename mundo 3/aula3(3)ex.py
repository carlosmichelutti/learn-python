núm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

valor = 0
soma = 0 
soma3coluna = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        núm[l] [c] = int(input(f'DIGITE UM VALOR PARA [{l}, {c}]'))

for l in range (0, 3):
    for c in range(0, 3):
        if núm [l][c] % 2 == 0:
            soma = soma + núm[l][c]
            
for l in range(0, 3):
    soma3coluna = soma3coluna + núm[l][2]

for c in range(0, 3):
    if c == 0:
        maior = núm[1][c]
    
    elif núm [1][c] > maior:
        maior = núm [1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{núm[l][c]:^5}]', end=' ')
    print(' ')
print(f'A soma dos números pares da matriz é igual a {soma}')
print(f'A soma dos números da 3 coluna é igual a {soma3coluna}.')
print(f'O maior valor da segunda linha foi o número {maior}.')
