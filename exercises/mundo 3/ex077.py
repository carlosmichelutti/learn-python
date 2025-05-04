def verificar_inteiro() -> int:
    while True:
        numero = str(input('Digite um número: '))
        if numero.isnumeric():
            return int(numero)
        else:
            print(f'Erro! O valor digitado {numero} não é um número inteiro válido.')

numero = verificar_inteiro()
print(f'Você acabou de digitar o número {numero}.')
