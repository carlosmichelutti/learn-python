numero = int(input('ESCREVA UM NÚMERO QUALQUER: '))
primo = 0
for c in range(1, (numero+1)):
    if numero % c == 0:
        primo = primo + 1
if primo == 2:
    print('O NÚMERO {} É UM NÚMERO PRIMO.'.format(numero))
elif primo > 2:
    print('O NÚMERO {} NÃO É UM NÚMERO PRIMO.'.format(numero))
