nome = str(input('Digite seu nome completo: ')).strip()

print(f'Muito prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {nome.split()[0].capitalize()}.')
print(f'Seu último nome é {nome.split()[-1].capitalize()}.')
