quantidade_numeros = 0
numero = 0
soma = 0
while True:
    numero = int(input('Digite um número inteiro qualquer [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    quantidade_numeros += 1

print(f'A soma de todos os {quantidade_numeros} números digitados é igual a {soma}.')
print(f'A média de todos os {quantidade_numeros} números digitados é igual a {soma / quantidade_numeros}.')
