maior = 0
menor = 0
for num in range(1, 6):
    peso = float(input(f'Digite o peso da {num}º pessoa: '))
    if num == 1:
        maior = peso
        menor = peso
        continue
    if peso > maior:
        maior = peso
    elif peso < menor: 
        menor = peso

print(f'O maior peso lido foi {maior}kg.')
print(f'O menor peso lido foi {menor}kg.')
