lado1 = float(input('Digite o valor do 1 lado do triângulo: '))
lado2 = float(input('Digite o valor do 2 lado do triângulo: '))
lado3 = float(input('Digite o valor do 3 lado do triângulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 == lado3:
        print('Esse triângulo existe, e é um triângulo equilátero.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Esse triângulo é possível e é um triângulo escaleno.')
    else: 
        print('Esse triângulo é um triângulo isósceles.')
else: 
    print('Esse triângulo não pode existir.')
