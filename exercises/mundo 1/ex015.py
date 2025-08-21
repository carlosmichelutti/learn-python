nome = str(input('Digite o seu nome completo: ')).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
total_de_letras = len(nome) - nome.count(' ')
primeiro_nome = nome.split(' ')[0]
primeiro_nome_quantidade_letras = len(primeiro_nome)

print(f'Seu nome em maiúsculas é: {nome_maiusculo}.')
print(f'Seu nome em minúsculas é: {nome_minusculo}.')
print(f'Seu nome tem ao todo {total_de_letras} letras.')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {primeiro_nome_quantidade_letras} letras.')
