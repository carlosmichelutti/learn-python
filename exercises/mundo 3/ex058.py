numeros = (
    int(input('Digite um número: ')), 
    int(input('Digite um número: ')), 
    int(input('Digite um número: ')), 
    int(input('Digite um número: '))
)

print(f'O número 9 apareceu {numeros.count(9)} vezes.')

if 3 not in numeros:
    print('Nenhum número 3 foi digitado.')
else:
    print(f'O primeiro número 3 foi digitado na {numeros.index(3)+1}ª posição.')

for num in range(0, 4):
    if numeros[num] % 2 == 0:
        print(f'Os valores pares digitados foram {numeros[num]}')

if all(n % 2 != 0 for n in numeros):
    print('Não foi digitado nenhum número par.')
