pessoas_maior_de_idade = 0
quantidade_mulheres = 0
quantidade_homens = 0
resposta = 'S'

while resposta == 'S':
    idade = int(input('Quantos anos você tem? '))
    while True: 
        sexo = str(input('Qual é o seu sexo [M/F]? ')).upper().strip()
        if sexo not in 'MF':
            print('Opção invalida! Tente novamente.')
            continue
        break

    if idade > 18:
        pessoas_maior_de_idade += 1
    if sexo == 'M':
        quantidade_homens += 1
    if sexo == 'F':
        quantidade_mulheres += 1

    while True:
        resposta = str(input('Você quer continuar [S/N]? ')).upper().strip()
        if resposta not in 'SN':
            print('Opção invalida! Tente novamente.')
            continue
        print(f'Foram digitados {pessoas_maior_de_idade} homens com mais de 18 anos.')
        print(f'Foram digitados {quantidade_mulheres} mulheres.')
        print(f'Foram digitados {quantidade_homens} homens.')
        break
