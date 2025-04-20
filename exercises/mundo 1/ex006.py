carteira = float(input('Quanto de dinheiro você tem na sua carteira? R$'))
dolares = carteira / 5.21
euros = carteira / 5.67
ienes =  carteira * 25.01

print(f'Com R${carteira} você tem U${dolares:.2F} dolares, €{euros:.2f} euros e ¥{ienes:.2f} ienes.')
