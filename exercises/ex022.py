velocidade = int(input('Digite a velocidade do carro em KM/H: '))

if velocidade > 80:
    valor_da_multa = (velocidade - 80) * 7
    print(f'Você ultrapassou a velocidade máxima em {velocidade - 80} KM/H na rodovia, sua multa é de R${valor_da_multa} reais.')
else:
    print('Parabéns, a sua velocidade é adequada a velocidade máxima na rodovia, continue assim!')
