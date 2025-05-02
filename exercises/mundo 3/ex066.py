numeros_impares = []
numeros_pares = []
numeros = []

for _ in range(1, 8):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)

    if numero % 2 == 1: 
        numeros_impares.append(numero)

print(f'Os números pares registrados foram: {numeros_pares}.')
print(f'Os números impares registrados foram: {numeros_impares}.')
