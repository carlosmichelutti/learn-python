from random import randint

pessoas = [
    {'nome': 'Carlos', 'idade': randint(10, 99)},
    {'nome': 'Felipe', 'idade': randint(10, 99)},
    {'nome': 'Marcos', 'idade': randint(10, 99)},
]

idades = list(map(lambda pessoa: pessoa['idade'], pessoas))
nomes = list(map(lambda pessoa: pessoa['nome'], pessoas))

frases = map(lambda nome, idade: f'{nome} tem {idade} anos', nomes, idades)
print(*list(frases), sep=', ', end='.\n')
