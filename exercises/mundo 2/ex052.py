pessoas_maior_de_idade = 0
quantidade_mulheres = 0
quantidade_homens = 0
resposta = 's'

while resposta == 's':
    idade = int(input('Quantos anos você tem? '))
    while True: 
        sexo = str(input('Qual é o seu sexo [M/F]? ')).lower().strip()
        if sexo not in 'mf':
            print('Opção invalida! Tente novamente.')
            continue
        break

    if idade > 18:
        pessoas_maior_de_idade += 1
    if sexo == 'm':
        quantidade_homens += 1
    if sexo == 'f':
        quantidade_mulheres += 1

    while True:
        resposta = str(input('Você quer continuar [S/N]? ')).lower().strip()
        if resposta not in 'sn':
            print('Opção invalida! Tente novamente.')
            continue
        if resposta == 'n':
            print(f'Foram digitados {pessoas_maior_de_idade} homens com mais de 18 anos.')
            print(f'Foram digitados {quantidade_mulheres} mulheres.')
            print(f'Foram digitados {quantidade_homens} homens.')

        break
        