from random import randint
from operator import itemgetter

cont = 0
jogadores = {}
jogadoresemordem = {}

for jogador in range(0, 4):
    número = randint(1, 6)
    jogadores[f'Jogador{jogador+1}'] = número
    print(f'O JOGADOR{jogador+ 1} TIROU {número} ')

jogadoresemordem = list()
jogadoresemordem = sorted(jogadores.items(), key=itemgetter(1), reverse= True)

for k, v in enumerate(jogadoresemordem):
    print(f'O {k+1}º lugar: {v[0]} com {v[1]}')
 
'''for i in sorted(jogadores, key= jogadores.get, reverse= True) : 
    cont = cont + 1
    print(f'{cont}ºLUGAR - ', i, jogadores[i])'''
