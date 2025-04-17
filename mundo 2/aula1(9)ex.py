from random import choice
from time import sleep


print('VAMOS BRINCAR DE PEDRA, PAPEL E TESOURA?!!')
print('=+='*50)

print('EU COMEÇO! VOU PENSAR EM ALGUMA FORMA! EU VOU TE VENCER!!')
sleep(2)
jogomaquina = choice(['pedra', 'papel', 'tesoura']).lower()
print('ESTOU PRONTO! TENTE ME VENCER!')
print('ESCOLHA ENTRE PEDRA, PAPEL, TESOURA E COLOQUE AGORA! VAMOS VER QUEM GANHA! \n')
jogouser = str(input('ESCOLHA UMA OPÇÃO: ')).lower()

if jogomaquina == jogouser:
    print('EMPATE! NINGÚEM GANHOU DESSA VEZ')
elif (jogomaquina == 'pedra' and jogouser == 'tesoura'):
    print('EU GANHEI! TENTE NOVAMENTE!')
elif (jogomaquina == 'tesoura' and jogouser == 'papel'):
    print('EU GANHEI! TENTE NOVAMENTE!')
elif (jogomaquina == 'papel' and jogouser == 'pedra'):
    print('EU GANHEI! TENTE NOVAMENTE!')
elif (jogomaquina == 'pedra' and jogouser == 'papel'):
    print('PARABÉNS! DESSA VEZ VOCÊ ME GANHOU!')
elif (jogomaquina == 'tesoura' and jogouser == 'pedra'):
    print('PARABÉNS! DESSA VEZ VOCÊ ME GANHOU!')
elif (jogomaquina == 'papel' and jogouser == 'tesoura'):
    print('PARABÉNS! DESSA VEZ VOCÊ ME GANHOU!')




