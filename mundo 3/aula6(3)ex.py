def leiaint(numero):

    while True:
        numero = str(input('DIGITE UM NÚMERO: '))

        if numero.isnumeric():
            return numero
            break
        
        else:
            print(f'ERRO! O VALOR DIGITADO {numero} NÃO É UM NÚMERO INTEIRO VÁLIDO.')

n = leiaint('Digite um número: ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {n}')
