jogador = {}
jogadoreslist = []
gols = []
totaldegols = 0
gol = 0


while True: 

#PERGUNTANDO O NOME E QUANTAS PARTIDAS O JOGADOR JOGOU INFINITAMENTE COM A CONDIÇÃO WHILE ---------------------

    jogador['NOME DO JOGADOR'] = str(input('QUAL O NOME DO JOGADOR? ')).upper().strip()
    partidas = int(input(f'QUANTAS PARTIDAS O JOGADOR {jogador["NOME DO JOGADOR"]} JOGOU? '))

#CONFERINDO E PERGUNTANDO QUANTOS GOLS O JOGADOR FEZ EM CADA PARTIDA QUE ELE JOGOU ----------------------------

    if partidas > 0:
        for jogo in range(0, partidas):

#COLOCANDO OS GOLS EM UMA LISTA --------------------------------------------------------------------------------

            gols.append(int(input(f'QUANTOS GOLS {jogador["NOME DO JOGADOR"]} FEZ NA {jogo+1}º PARTIDA? ')))

#COLOCANDO A LISTA COM OS GOLS EM CADA PARTIDA NO DICIONÁRIO -----------------------------------------------------

        jogador['GOL POR PARTIDA'] = gols.copy()

#CALCULANDO O TOTAL DE GOLS SOMANDO OS GOLS DE CADA PERTIDA EM UMA VARIÁVEL SIMPLES E DEPOIS COLOCANDO NO DICIONÁRIO ---

        for n in range(0, len(gols)):
            totaldegols = totaldegols + gols[n]
        jogador['TOTAL DE GOLS'] = totaldegols
        totaldegols = 0

#COLOCANDO TODO O DICIONÁRIO DO JOGADOR EM UMA LISTA QUE FICARÁ TODOS OS DICIONARIOS DOS JOGADORES ---------------------

        jogadoreslist.append(jogador.copy())
        jogador.clear()
        gols.clear()
        


#PERGUNTANDO A RESPOSTA DE CONTINUAÇÃO PARA TERMINAR O LOOP WHILE OU CADASTRAR OUTRO JOGADOR --------------------------

        resp = str(input('QUER CONTINUAR [S/N]? '))

#CASO A RESPOSTA SEJA 'N' MOSTRAMOS AS INFORMAÇÕES DE TODOS OS JOGADORES E ENCERRAMOS O PRIMEIRO LOOP WHILE ----------

        if resp == 'N':
            print('{:<5}'.format('COD.'), end='')
            print('{:<10}'.format('NOME'), end='')
            print('{:<10}'.format('GOLS'), end='')
            print('{:<10}'.format('TOTAL DE GOLS'))
            print('='*40)

            for pessoa in range(0, len(jogadoreslist)):

                print(f'{pessoa:<5}', end='')
                print(f'{jogadoreslist[pessoa]["NOME DO JOGADOR"]:<10}', end='')
                print(f'{jogadoreslist[pessoa]["GOL POR PARTIDA"]}', end='')
                print(f'{jogadoreslist[pessoa]["TOTAL DE GOLS"]:10}')

#CONDIÇÃO PARA O USUÁRIO ESCOLHER DE QUAL JOGADOR ELE QUER SABER AS INFORMAÇÕES MAIS AFUNDO ------------

            while True:
                mostrardados = int(input('MOSTRAR NÚMEROS DE QUAL JOGADOR? [999 ENCERRA] '))

#CONDIÇÃO 999 PARA TERMINAR O LOOP E ENCERRAR O PROGRAMA ------------------------------------------------

                if mostrardados == 999:
                    print('ENCERRANDO...')
                    break

#CONDIÇÃO CASO O NÚMERO DO JOGADOR NÃO EXISTA ---------------------------------------------------------

                elif mostrardados > len(jogadoreslist):
                    print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE: ')

#CONDIÇÃO PARA MOSTRAR AS INFORMAÇÇOES CORRETAS DE CADA JOGADOR BUSCANDO NA LISTA PELO -------------------------------------------                    
#NUMERO INFORMADO PELO USUÁRIO E DEPOIS PELO INDICE DE DETERMINADA INFORMAÇÃO NO DICIONÁRIO -------------------------------------

                else:
                    print('='*40)
                    print(f'O JOGADOR {jogadoreslist[mostrardados]["NOME DO JOGADOR"]} JOGOU {len(jogadoreslist[mostrardados]["GOL POR PARTIDA"])} PARTIDAS')
                    print('='*40)

#MOSTRANDO QUANTOS GOLS O JOGADOR FEZ EM CADA PARTIDA PROCURANDO NA LISTA DE GOLS POR CADA PARTIDA EM UM LOOP FOR -----------------------------
#E MOSTRANDO O TOTAL DE GOLS ABAIXO

                    for partida in range(0, len(jogadoreslist[mostrardados]["GOL POR PARTIDA"])):
                        print(f'\t=> NA PARTIDA {partida+1}, fez {jogadoreslist[mostrardados]["GOL POR PARTIDA"][partida]}')
                    print(f'FOI UM TOTAL DE {sum(jogadoreslist[mostrardados]["GOL POR PARTIDA"])}')
                    print('='*40)
                
#ENCERRAMENTO DO PROGRAMA COM O 2 BREAK ----------------------------------------------------------------------

            break

#VERIFICANDO CASO A RESPOSTA DE CONTINUAÇÃO ESTEJA INCORRETA OU INVALIDA ------------------------------------

    elif resp != 'S':
        print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE. ')
        resp = str(input('QUER CONTINUAR [S/N]? '))
