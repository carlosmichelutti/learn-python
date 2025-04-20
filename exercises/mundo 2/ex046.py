from random import randint

print('Vamos jogar? Eu vou pensar em um número de 1 a 10 e você tenta adivinhar!!')
jogouser = 0
jogopc = randint(1, 10)
print('Pensei em um número de 1 a 10, tente adivinhar agora!')
quantidade_de_tentativas = 0

while jogopc != jogouser:
    jogouser = int(input('Em que número eu pensei? '))
    if jogouser != jogopc:
        print('Você errou! Tente novamente!')
        quantidade_de_tentativas += 1

print(f'Parabéns você acertou em apenas {quantidade_de_tentativas} tentativas.')
