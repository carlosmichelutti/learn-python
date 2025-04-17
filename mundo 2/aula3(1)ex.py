from random import randint
from time import sleep

print('VAMOS JOGAR? EU VOU PENSAR EM UM NÚMERO E VOCÊ TENTA ADIVINHAR!!')

sleep(2)

jogopc = randint(1, 10)

print('=+='*10)
print('Pensei em um número, tente adivinhar agora!')
print('=+='*10)

jogouser = 0
qtdjogadas = 0

while jogopc != jogouser:
    jogouser = int(input('EM QUE NÚMERO EU PENSEI? '))
    
    if jogouser != jogopc:
        print('VOCÊ ERROU! TENTE NOVAMENTE!')
        print('=+='*10)
        qtdjogadas = qtdjogadas + 1
print('PARABÉNS VOCÊ ACERTOU EM APENAS {} TENTATIVAS.'.format(qtdjogadas))



