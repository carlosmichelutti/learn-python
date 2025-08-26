from operator import itemgetter
from random import randint

jogadores = {}
jogadores_em_ordem = {}
for jogador in range(0, 4):
    numero = randint(1, 6)
    jogadores[f'Jogador{jogador+1}'] = numero
    print(f'O jogador{jogador+1} tirou {numero}.')

jogadores_em_ordem = list()
jogadores_em_ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for index, value in enumerate(jogadores_em_ordem):
    print(f'O {index+1}º lugar: {value[0]} com {value[1]}.')
