from time import sleep
import random

numero_pc = random.randint(1, 5)
print('Pensando em um número de 1 a 5...')
sleep(2)
numero_usuario = int(input('Adivinhe em qual número o eu pensei: '))

if numero_usuario == numero_pc:
    print(f'Você acertou eu pensei no número {numero_pc}')
else:
    print(f'Você errou... eu pensei no número {numero_pc} e você falou {numero_usuario}, tente novamente!')
