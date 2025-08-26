numero = int(input('Digite um número qualquer: '))
primo = 0

for num in range(1, (numero + 1)):
    if numero % num == 0:
        primo += 1

if primo == 2:
    print(f'O número {numero} é um número primo.')
elif primo > 2:
    print(f'O número {numero} não é um número primo.')
