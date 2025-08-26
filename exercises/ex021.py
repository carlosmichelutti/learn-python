nome = str(input('Digite seu nome: '))

salario = float(input(f'{nome} digite o seu salário atual em R$'))

if salario > 1250.00:
    aumento = salario * (10 / 100)
    print(f'O seu antigo salário era R${salario:.2f} reais, o seu salário atual agora é de R${(salario + aumento):.2f} reais')
else:
    aumento = salario * (15 / 100)
    print(f'O seu antigo salário era R${salario:.2f} reais, o seu salário atual agora é de R${(salario + aumento):.2f} reais')
