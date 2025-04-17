pessoas = [
    {'nome': 'Mariana','idade': 18},
    {'nome': 'Carlos', 'idade': 19},
    {'nome': 'Arthur', 'idade': 16},
    {'nome': 'Rebeca', 'idade': 34},
    {'nome': 'Rodolfo', 'idade': 24},
    {'nome': 'Maria', 'idade': 21}
]

menores_de_idade = list(filter(lambda p: p['idade']<18, pessoas))
maiores_de_idade = list(filter(lambda p: p['idade']>18, pessoas))
nomes_com_mais_de_seis_caracteres = list(filter(lambda p: len(p['nome']) > 6, pessoas))
print(nomes_com_mais_de_seis_caracteres)
print(menores_de_idade)
print(maiores_de_idade)