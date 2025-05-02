pessoas = []
pessoa = {}
media = 0

while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).lower().strip()
        if sexo in 'mf':
            pessoa['Sexo'] = sexo
            break
        else:
            print('Erro. Digite apenas M ou F.')
            continue

    pessoas.append(pessoa.copy())
    resposta = str(input('Quer continuar? [S/N]: ')).lower().strip()
    if resposta == 'n':
        print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
        for pessoa in pessoas:
            media += pessoa['Idade']
        media = media // len(pessoas)
        print(f'- A MÉDIA DE IDADE É DE {media:}')

# #VERIFICANDO E PRINTANDO O NOME DAS MULHERES CADASTRADAS E CASO NÃO TENHA APARECE OUTRA MENSAGEM INFORMANDO ISSO --
       
#         print('- AS MULHERES CADASTRADAS FORAM: ', end='')
#         for mulheres in range(0, len(pessoas)):
#             if pessoas[mulheres]['Sexo'] == 'F':
#                 print(pessoas[mulheres]['Nome'], end=' ')
#         print('')

# #VERIFICANDO AS PESSOAS COM IDADE MAIOR QUE A MÉDIA DO GRUPO E PRINTANDO ESSES NOMES --------------------------
        
#         print('- LISTA DE PESSOAS ACIMA DA MÉDIA: ')
#         for p in pessoas:
#             if  p['Idade'] > média:
#                 print('     ')
#                 for k, v in p.items():
#                     print(f'{k} = {v}; ', end='')

# #ENCERRANDO O LOOP INFINITO CASO A RESPOSTA SEJA 'N' --------------------------------------------------------

        break

    if resposta != 'S':
        print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE. ')
        resposta = str(input('QUER CONTINUAR [S/N]: ')).upper().strip()
