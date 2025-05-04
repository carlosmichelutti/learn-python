from random import randint
from time import sleep

print('================= MEGA SENA DA VIRADA =================')
print('=======================================================')
quantidade_jogos = int(input('Deseja realizar quantos jogos? '))

for c in range(0, quantidade_jogos):
    jogo = []
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
        if len(jogo) >= 6:
            break

    print(f'Jogo Nº{c+1}: {jogo}.')
    sleep(1)
