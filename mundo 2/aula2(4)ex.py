soma = 0
print('=+='*10)
print('CONTADOR DE NÚMEROS PARES')
for c in range (1, 7):
    c = int(input(('ESCREVA O {}º NUMERO: '.format(c))))
    if c % 2 == 0:
        soma += c
    else:
        print("{} = VALOR DESCONSIDERADO POR SER IMPAR".format(c))
print("A SOMA DOS NÚMEROS PARES ESCRITOS É IGUAL A {}".format(soma))
print('FIM')