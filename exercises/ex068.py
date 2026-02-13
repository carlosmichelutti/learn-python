from random import randint
from time import sleep

print('================= MEGA SENA DA VIRADA =================')
print('=======================================================')
game_count = int(input('How many games do you want to play? '))

for c in range(0, game_count):
    game = []
    while True:
        number = randint(1, 60)
        if number not in game:
            game.append(number)
        if len(game) >= 6:
            break

    print(f'Game No.{c + 1}: {game}.')
    sleep(1)
