from functools import reduce
from random import randint

products = [
    {'name': 'Monitor', 'quantity': randint(1, 100), 'price': randint(1, 100)},
    {'name': 'Keyboard', 'quantity': randint(1, 100), 'price': randint(1, 100)},
    {'name': 'Mouse', 'quantity': randint(1, 100), 'price': randint(1, 100)},
]

total_product_values = list(map(lambda product: {'name': product['name'], 'total': product['quantity'] * product['price']}, products))
values = list(map(lambda product: product['total'], total_product_values))
total_value = reduce(lambda total, value: total + value, values, 0)
sentences = map(lambda product: f'    * The product {product["name"]} has ${product["total"]} invested.', total_product_values)

print(*list(sentences), sep='\n')
print(f'    * Total value invested: ${total_value}.')
