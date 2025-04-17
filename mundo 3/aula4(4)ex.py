
pessoas = []
cidadão = {}
média = 0

while True:
#PERGUNTANDO AS INFOMRAÇÕES DE CADA PESSOA A SER CADASTRADA ----------------------------------------------
    cidadão['NOME'] = str(input('NOME: '))
    cidadão['IDADE'] = int(input('IDADE: '))
    while True:
        sexo = str(input('SEXO [M/F]: ')).upper().strip()
        if sexo == 'M' or sexo == 'F':
            cidadão['SEXO'] = sexo
            break
        if sexo != 'M' or sexo != 'F':
            print("ERRO. POR FAVOR DIGITE APENAS M OU F")
        
#COPIANDO OS VALORES DO DICIONARIO EM UMA LISTA ÚNICA SEPARANDO CADA DICIONARIO(PESSOA) DE OUTRA PESSOA --------

    pessoas.append(cidadão.copy())

#PERGUNTANDO SE O USUÁRIO QUER CADASTRAR OUTRA PESSOA -----------------------------------------------------

    resp = str(input('QUER CONTINUAR [S/N]: ')).upper().strip()
    print('')

#VERIFICANDO RESPOSTAS ------------------------------------------------------------------------------------

    if resp == 'N':

#MOSTRANDO QUANTAS PESSOAS FORAM CADASTRADAS AO TOTAL -----------------------------------------------------

        print(f'AO TODO FORAM CADASTRADAS {len(pessoas)} PESSOAS')

#CALCULANDO A MÉDIA DO GRUPO CADASTRADO --------------------------------------------------------------------

        for idade in range(0, len(pessoas)):
            média = média + pessoas[idade]['IDADE']
        média = média/len(pessoas)
        print(f'- A MÉDIA DE IDADE É DE {média:.2f}')

#VERIFICANDO E PRINTANDO O NOME DAS MULHERES CADASTRADAS E CASO NÃO TENHA APARECE OUTRA MENSAGEM INFORMANDO ISSO --
       
        print('- AS MULHERES CADASTRADAS FORAM: ', end='')
        for mulheres in range(0, len(pessoas)):
            if pessoas[mulheres]['SEXO'] == 'F':
                print(pessoas[mulheres]['NOME'], end=' ')
        print('')

#VERIFICANDO AS PESSOAS COM IDADE MAIOR QUE A MÉDIA DO GRUPO E PRINTANDO ESSES NOMES --------------------------
        
        print('- LISTA DE PESSOAS ACIMA DA MÉDIA: ')
        for p in pessoas:
            if  p['IDADE'] > média:
                print('     ')
                for k, v in p.items():
                    print(f'{k} = {v}; ', end='')

#ENCERRANDO O LOOP INFINITO CASO A RESPOSTA SEJA 'N' --------------------------------------------------------

        break

    if resp != 'S':
        print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE. ')
        resp = str(input('QUER CONTINUAR [S/N]: ')).upper().strip()
