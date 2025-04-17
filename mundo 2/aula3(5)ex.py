numero = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR? '))
n1 = 0
n2 = 1
n3 = 0

while numero != 0:
    print('{} -> '.format(n1), end='')
    numero = numero - 1
    n1 = n1 + n2
    n2 = n3
    n3 = n1
    
