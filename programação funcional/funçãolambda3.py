products = ({'quantidade': 10, 'Preço': 10},
            {'quantidade': 20, 'Preço': 20},
            {'quantidade': 5, 'Preço': 100})


def calc_preco_total(products):
    return products['quantidade'] * products['Preço']


soma_total_de_cada_produto = list(map(calc_preco_total, products))

print(f'Preços totais: {soma_total_de_cada_produto}')
print(f'Preço total total: {sum(soma_total_de_cada_produto)}')