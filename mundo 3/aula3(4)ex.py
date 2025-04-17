'''FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES
O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR
6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA
LISTA COMPOSTA. '''

from random import randint
from time import sleep

print('='*20)
print('MEGA SENA DA VIRADA')
print('='*20)

jogos = int(input("DESEJA REALIZAR QUANTOS JOGOS? "))
print()
jogo = []
jogos1 =[]
cont = 0

for c in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1 
        if cont >= 6:
            break
    cont = 0
    jogos1.append(jogo[:])
    jogo.clear()
    sleep(1)
    print(f'JOGO {c+1}: ', end='')
    print(jogos1[c])
