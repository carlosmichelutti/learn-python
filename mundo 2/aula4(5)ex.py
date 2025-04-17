

print('='*30)
print('{:^30}'.format('BANCO DO BRASIL'))
print('='*30)

notasde50 = 0
notasde20 = 0
notasde10 = 0
notasde1= 0 


saque = float(input('QUANTO VOCÊ QUER SACAR? '))

while True:
    if saque > 49:
        saque = saque - 50
        notasde50 = notasde50 + 1
        
    elif saque > 19:
        saque = saque - 20
        notasde20 = notasde20 + 1

    elif saque > 9:
        saque = saque - 10
        notasde10 = notasde10 + 1

    elif saque > 0:
        saque =  saque - 1
        notasde1 = notasde1 + 1

    elif saque == 0:
        print('TOTAL DE CÉDULAS DE R$50 - {} CÉDULAS.'.format(notasde50))
        print('TOTAL DE CÉDULAS DE R$20 - {} CÉDULAS'.format(notasde20))
        print('TOTAL DE CÉDULAS DE R$10 - {} CÉDULAS.'.format(notasde10))
        print('TOTAL DE CÉDULAS DE R$1 - {} CÉDULAS.'.format(notasde1))
        break