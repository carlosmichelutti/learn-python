from operator import itemgetter
from random import randint

players = {}
players_in_order = {}
for player in range(0, 4):
    number = randint(1, 6)
    players[f'Player{player + 1}'] = number
    print(f'Player {player + 1} rolled {number}.')

players_in_order = list()
players_in_order = sorted(players.items(), key=itemgetter(1), reverse=True)
for index, value in enumerate(players_in_order):
    print(f'{index + 1}st place: {value[0]} with {value[1]}.')
