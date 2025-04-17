products = ({'quantidade': 10, 'Preço': 10},
            {'quantidade': 20, 'Preço': 20},
            {'quantidade': 5, 'Preço': 100})

soma_total_de_cada_produto = list(map(lambda products: products['quantidade'] * products['Preço'], products))

print(f'Preços totais: {soma_total_de_cada_produto}')
print(f'Preço total total: {sum(soma_total_de_cada_produto)}')
