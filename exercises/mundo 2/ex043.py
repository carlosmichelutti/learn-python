import os

pessoas_maiores_de_idade = 0
quantidade_de_mulheres = 0
homem_maior_idade = None
menor_idade = 0
maior_idade = 0

for c in range (1, 5):
    sexo = str(input('Qual é o seu sexo? [M/F]? ')).upper().strip()
    nome = str(input('Qual é o seu nome? ')).capitalize().strip()
    idade = int(input(f'Quantos anos você tem {nome}? '))
    os.system('cls')
    if sexo == 'F':
        quantidade_de_mulheres += 1

    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        homem_maior_idade = nome

print(f'Homem com maior idade: {homem_maior_idade} com {maior_idade} anos.')
print(f'Quantidade de mulheres no grupo: {quantidade_de_mulheres}.')
