pessoas = [
    {'Nome': 'Carlos', 'Idade': 32},
    {'Nome': 'Felipe', 'Idade': 21},
    {'Nome': 'Marcao', 'Idade': 44},
]


nome_das_pessoas = list(map(lambda pessoas: pessoas['Nome'], pessoas))
idade_das_pessoas = list(map(lambda pessoas: pessoas['Idade'], pessoas))

frases = map(lambda p: f'{p["Nome"]} tem {p["Idade"]} anos', pessoas)
print(list(frases))