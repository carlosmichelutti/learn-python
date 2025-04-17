import random

qtddevitorias = 0

while True:
    maquina = random.randint(1, 10)
    valoruser = int(input('DIGITE UM VALOR: '))
    resp = str(input('PAR OU IMPAR [P/I]? ')).upper().strip()
    

    if resp == 'P':
        if (maquina + valoruser) % 2 == 0:
            qtddevitorias = qtddevitorias + 1
            print('VOCÊ JOGOU {} E O COMPURADOR JOGOU {} E O TOTAL DEU PAR.'.format(valoruser, maquina))
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE')
            print('')

        elif (maquina + valoruser)% 2 == 1:
            print('VOCÊ JOGOU {} E O COMPURADOR JOGOU {} E O TOTAL DEU IMPAR.'.format(valoruser, maquina))
            print('VOCÊ PERDEU!')
            print('=+='*10)
            print('GAME OVER! VOCÊ VENCEU {} VEZES.'.format(qtddevitorias))
            break

    elif resp == 'I':
        if (maquina + valoruser)% 2 == 1:
            qtddevitorias = qtddevitorias + 1
            print('VOCÊ JOGOU {} E O COMPURADOR JOGOU {} E O TOTAL DEU IMPAR.'.format(valoruser, maquina))
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE')
            print('')

        if (maquina + valoruser) % 2 == 0:
            print('VOCÊ PERDEU!')
            print('VOCÊ JOGOU {} E O COMPURADOR JOGOU {} E O TOTAL DEU PAR.'.format(valoruser, maquina))
            print('=+='*10)
            print('GAME OVER! VOCÊ VENCEU {} VEZES.'.format(qtddevitorias))
            break

        

        


