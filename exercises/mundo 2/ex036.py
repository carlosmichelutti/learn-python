from random import choice

print('Vamos brincar de pedra, papel e tesoura? ')
print('Pedra')
print('Papel')
print('Tesoura')
escolha_maquina = choice(['pedra', 'papel', 'tesoura']).lower()
escolha_usuario = str(input('Escolha uma opção: ')).lower()

if escolha_maquina == escolha_usuario:
    print('Empate! Ningúem ganhou dessa vez.')
elif (escolha_maquina == 'pedra' and escolha_usuario == 'tesoura'):
    print('Eu ganhei! Tente novamente!')
elif (escolha_maquina == 'tesoura' and escolha_usuario == 'papel'):
    print('Eu ganhei! Tente novamente!')
elif (escolha_maquina == 'papel' and escolha_usuario == 'pedra'):
    print('Eu ganhei! Tente novamente!')
elif (escolha_maquina == 'pedra' and escolha_usuario == 'papel'):
    print('Parabéns! Dessa vez você me ganhou!')
elif (escolha_maquina == 'tesoura' and escolha_usuario == 'pedra'):
    print('Parabéns! Dessa vez você me ganhou!')
elif (escolha_maquina == 'papel' and escolha_usuario == 'tesoura'):
    print('Parabéns! Dessa vez você me ganhou!')
