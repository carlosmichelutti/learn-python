num = int(input('ESCREVA UM NÚMERO:  ')) , int(input('ESCREVA UM NÚMERO:  ')), int(input('ESCREVA UM NÚMERO:  ')), int(input('ESCREVA UM NÚMERO:  '))
print(num.index(3))

print('O NÚMERO 9 APARECEU {} VEZES.'.format(num.count(9)))

if num.index(3) == 0:
    print('NENHUM NUMERO 3 FOI DIGITADO.')
else:
    print('O PRIMEIRO NÚMERO 3 FOI DIGITADO NA {}ª POSIÇÃO.'.format(num.index(3)+1))

for c in range(0, 4):
    if num[c] % 2 == 0:
        print('OS VALORES PARES DIGITADOS FORAM {}'.format(num[c]))
    else:
        print('NÃO FOI DIGITADO NENHUM NÚMERO PAR.')



