valor = float(input('Qual o valor normal do produto? R$'))

print('Qual a condição de pagamento? ')
print('[1] A vista dinheiro/cheque')
print('[2] A vista no cartão')
print('[3] Em 2x no cartão')
print('[4] Em 3x ou mais no cartão')

condicao_de_pagamento = int(input('Digite alguma opção: '))
if condicao_de_pagamento == 1:
    print(f'O valor a ser pago pelo produto terá um desconto de 10% e o novo valor a ser pago é de R${(valor * 0.90):.2f}.')

elif condicao_de_pagamento == 2:
    print(f'O valor a ser pago pelo produto terá um desconto de 5% e seu novo valor é de R${(valor * 0.95):.2f}.')

elif condicao_de_pagamento == 3:
    total_parcelas = int(input('Você vai parcelar em quantas vezes? '))
    print(f'O valor a ser pago pelo produto será de R${(valor * 0.95):.2f}. Sendo {total_parcelas} parcelas de R${((valor * 0.95)/total_parcelas):.2f} reais cada.')

elif condicao_de_pagamento == 4:
    total_parcelas = int(input('Você vai parcelar em quantas vezes? '))
    print(f'O valor a ser pago pelo produto será de R${(valor * 0.95):.2f}. Sendo {total_parcelas} parcelas de R${((valor * 0.95)/total_parcelas):.2f} reais cada.')
