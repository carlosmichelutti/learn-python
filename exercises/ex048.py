from random import randrange

numero_fatorial = randrange(1, 10)
calculo = numero_fatorial
fatorial = 0

while numero_fatorial >= 1:
    print(f'{numero_fatorial} x', end=' ') if numero_fatorial > 1 else print(f'{numero_fatorial} = {calculo}', end=' ')
    numero_fatorial = numero_fatorial - 1
    if numero_fatorial > 0:
        calculo = numero_fatorial * calculo
