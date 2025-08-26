dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

custo = (60 * dias) + (km * 0.15)

print(f'O custo total a ser pago ao devolver o carro é de R${custo:.2f}.')
