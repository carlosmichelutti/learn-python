distancia = int(input('Quantos km você vai viajar? '))

if distancia <= 200:
    print(f'O valor da viajem é de R${(distancia*0.50):.2f} reais.')
else:
    print(f'O valor total da viajem será de R${(distancia*0.45):.2f} reais.')
