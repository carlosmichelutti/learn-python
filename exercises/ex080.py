from random import randint

pessoas = [
    {'nome': 'Mariana','idade': randint(10, 99)},
    {'nome': 'Carlos', 'idade': randint(10, 99)},
    {'nome': 'Arthur', 'idade': randint(10, 99)},
    {'nome': 'Rebeca', 'idade': randint(10, 99)},
    {'nome': 'Rodolfo', 'idade': randint(10, 99)},
    {'nome': 'Maria', 'idade': randint(10, 99)}
]

nomes_com_mais_de_seis_caracteres = list(filter(lambda pessoa: len(pessoa['nome']) > 6, pessoas))
menores_de_idade = list(filter(lambda pessoa: pessoa['idade'] < 18, pessoas))
maiores_de_idade = list(filter(lambda pessoa: pessoa['idade'] > 18, pessoas))
print(f'Nomes com mais de 6 caracteres: {list(map(lambda pessoa: pessoa["nome"], nomes_com_mais_de_seis_caracteres))}')
print(f'Menores de idade: {list(map(lambda pessoa: pessoa["nome"], menores_de_idade))}')
print(f'Maiores de idade: {list(map(lambda pessoa: pessoa["nome"], maiores_de_idade))}')
