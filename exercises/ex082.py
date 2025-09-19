from functools import reduce
from random import randint

produtos = [
    {'nome': 'Monitor', 'quantidade': randint(1, 100), 'preco': randint(1, 100)},
    {'nome': 'Teclado', 'quantidade': randint(1, 100), 'preco': randint(1, 100)},
    {'nome': 'Mouse', 'quantidade': randint(1, 100), 'preco': randint(1, 100)},
]

valor_total_produtos = list(map(lambda produto: {'nome': produto['nome'], 'total': produto['quantidade'] * produto['preco']}, produtos))
valores = list(map(lambda produto: produto['total'], valor_total_produtos))
valor_total = reduce(lambda valor_total, valor: valor_total + valor, valores, 0)
frases = map(lambda produto: f'    * O produto {produto["nome"]} tem R${produto["total"]} reais investidos.', valor_total_produtos)

print(*list(frases), sep='\n')
print(f'    * Valor total investido: R${valor_total} reais.')
