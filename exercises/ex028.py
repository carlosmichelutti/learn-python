numero = int(input('Digite um número inteiro: '))

print('Você quer converter esse número para:')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')

conversao = int(input('Escolha uma opção: '))

if conversao == 1:
    print(f'O número {numero} convertido para número binário é igual a {bin(numero)[2:]}.')
elif conversao == 2:
    print(f'O número {numero} convertido para o formato octal é igual a {oct(numero)[2:]}.')
elif conversao == 3:
    print(f'O número {numero} convertido para o formato hexadecimal é igual a {hex(numero)[2:]}.')
