jogador = {
    'Nome do Jogador': str(input('Qual o nome do jogador? ')).lower().strip(),
    'Total de Gols': 0,
    'Jogos': []
}
partidas = int(input(f'Quantas partidas o jogador {jogador["Nome do Jogador"]} jogou? '))

for jogo in range(0, partidas):
    gols = int(input(f'Quantos gols o jogador {jogador["Nome do Jogador"]} fez na {jogo+1}ª partida? '))
    jogador['Jogos'].append({'partida': jogo+1, 'gols': gols})
    jogador['Total de Gols'] += gols

print(f'O jogador {jogador["Nome do Jogador"]} jogou {partidas} partidas.')

for partida in range(0, partidas):
    print(f'\t=> Na partida {partida+1}, o jogador {jogador["Nome do Jogador"]} fez {jogador["Jogos"][partida]["gols"]} gols.')
