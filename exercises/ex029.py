numero1 = int(input('Digite um número inteiro qualquer: '))
numero2 = int(input('Digite outro número inteiro qualquer: '))

if numero1 > numero2:
    print(f'O primeiro número digitado é maior que o segundo número, {numero1} > {numero2}.')
elif numero2 > numero1:
    print(f'O segundo número digitado é maior que o primeiro número, {numero2} > {numero1}.')
elif numero1 == numero2:
    print(f'Os dois números informados são iguais, {numero1} = {numero2}.')
