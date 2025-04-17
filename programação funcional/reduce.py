from functools import reduce

pessoas = [
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Carlos', 'idade': 19},
    {'nome': 'Arthur', 'idade': 16},
    {'nome': 'Rebeca', 'idade': 34},
    {'nome': 'Rodolfo', 'idade': 24},
    {'nome': 'Maria', 'idade': 21}
]

somente_idades = list(map(lambda p: p['idade'], pessoas))
maiores_de_idade = list(filter(lambda p: p>18, somente_idades))
soma_idades = reduce(lambda idades, p: idades + p, maiores_de_idade, 0)
print(f'A SOMA DAS IDADES DAS PESSOAS MAIORES DE IDADE É {soma_idades}')