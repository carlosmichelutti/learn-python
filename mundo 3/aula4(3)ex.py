jogador = {}
gols = []
totaldegols = 0
gol = 0

jogador['NOME DO JOGADOR'] = str(input('QUAL O NOME DO JOGADOR? ')).upper().strip()
partidas = int(input(f'QUANTAS PARTIDAS O JOGADOR {jogador["NOME DO JOGADOR"]} JOGOU? '))


if partidas != 0:
    for jogo in range(0, partidas):
        gols.append(int(input(f'QUANTOS GOLS {jogador["NOME DO JOGADOR"]} FEZ NA {jogo+1}º PARTIDA? ')))
    jogador['GOL POR PARTIDA'] = gols

    for n in range(0, len(gols)):
        totaldegols = totaldegols + gols[n]
    jogador['TOTAL DE GOLS'] = totaldegols

print('='*40)
for k, v in jogador.items():
    print(f'O CAMPO {k} TEM VALOR {v}.')
print('='*40)

print(f'O JOGADOR {jogador["NOME DO JOGADOR"]} JOGOU {partidas} PARTIDAS')

for partida in range(0, partidas):
    print(f'\t=> NA PARTIDA {partida+1}, fez {gols[partida]} GOLS')
print(f'FOI UM TOTAL DE {totaldegols}')
print('='*40)


