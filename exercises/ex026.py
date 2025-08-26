numero1 = int(input('Digite um número qualquer: '))
numero2 = int(input('Digite outro número qualquer: '))
numero3 = int(input('Digite mais um número qualquer: '))

menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f'O menor valor digitado foi o número: {menor}.')
print(f'O maior valor digitado foi o número: {maior}.')
