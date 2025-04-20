nome = str(input('Escreva seu nome completo: ')).strip()
nome = nome.split()

print(f'Muito prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[-1]}.')
