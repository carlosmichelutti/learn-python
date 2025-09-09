from functools import reduce
from random import randint

pessoas = [
    {'nome': 'Mariana', 'idade': randint(10, 99)},
    {'nome': 'Carlos', 'idade': randint(10, 99)},
    {'nome': 'Arthur', 'idade': randint(10, 99)},
    {'nome': 'Rebeca', 'idade': randint(10, 99)},
    {'nome': 'Rodolfo', 'idade': randint(10, 99)},
    {'nome': 'Maria', 'idade': randint(10, 99)}
]

idades = list(map(lambda pessoa: pessoa['idade'], pessoas))
maiores_de_idade = list(filter(lambda pessoa: pessoa > 18, idades))
soma_idades = reduce(lambda soma_idades, idade: soma_idades + idade, maiores_de_idade, 0)
print(f'A soma das idades das pessoas maiores de idade é igual a {soma_idades}.')
