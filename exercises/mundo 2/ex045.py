from datetime import datetime

ano_atual = datetime.today().year
pessoas_maior_de_idade = 0
pessoas_menor_de_idade = 0
for num in range(0, 7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {num+1}º pessoa: '))
    if ano_atual - ano_nascimento >= 18:
        pessoas_maior_de_idade += 1
    else: 
        pessoas_menor_de_idade += 1

print(f'No grupo existem {pessoas_maior_de_idade} pessoas que são maior de idade.')
print(f'No grupo existem {pessoas_menor_de_idade} pessoas que são menores de idade.')
