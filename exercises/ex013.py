frase = str(input('Digite uma frase: ')).strip()

frase_maiuscula = frase.upper()
quantidade_a = frase_maiuscula.count('A')
primeiro_a = frase_maiuscula.find('A')
ultimo_a = frase_maiuscula.rfind('A')

print(f'A letra A aparece {quantidade_a} vezes na frase.')
print(f'A primeira letra A apareceu na posição {primeiro_a + 1}.')
print(f'A última letra A apareceu na posição {ultimo_a + 1}.')
