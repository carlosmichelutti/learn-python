from random import randrange

numerofatorial = randrange(1, 10)
calculo = numerofatorial
fatorial = 0
while numerofatorial >= 1:
    print('{}x'.format(numerofatorial), end=' ')
    numerofatorial = numerofatorial -1
    if numerofatorial > 0:
        calculo = numerofatorial*calculo
print("=", calculo)


    


