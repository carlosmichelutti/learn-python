quantidade_maior_que_1000 = 0
quantidade_de_produtos = 0
menor_valor = 0
menor_nome = ''
resposta = 'S'
menor = 0
soma = 0

while not resposta == 'N':
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? R$'))
    quantidade_de_produtos += 1
    soma += valor

    if valor > 1000:
        quantidade_maior_que_1000 += 1

    if quantidade_de_produtos == 1:
        menor_nome = nome
        menor_valor = valor

    if valor < menor_valor:
        menor_nome = nome
        menor_valor = valor

    while True:
        resposta = str(input('Você quer continuar [S/N]? ')).upper().strip()   
        if resposta not in 'SN':
            print('Resposta inválida. Tente novamente.')
            continue
        if resposta == 'N':
            print(f'O valor total gasto na compra dos {quantidade_de_produtos} produtos foi R${soma} reais.')
            print(f'Foram digitados {quantidade_maior_que_1000} produtos que custam mais de R$1000,00.')
            print(f'O produto mais barato digitado foi o {menor_nome} que custa R${menor_valor} reais.')
            break
        else:
            break
