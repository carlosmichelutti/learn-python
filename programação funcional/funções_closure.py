def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

dobro = multiplicar(2)
triplo = multiplicar(3)
quadruplo = multiplicar(4)
from os import system
system('cls')
print(dobro)
print(triplo)
print(quadruplo)
print(f'O DOBRO DE 2 É {dobro(2)}')
print(f'O TRIPLO DE 3 É {triplo(3)}')
print(f'O QUADRUPLO DE 4 É {quadruplo(4)}')

print('')

def calcular_tabuada(x):
    def expoente_da_tabuada(y):
        return x * y
    return expoente_da_tabuada

x = 9
tabuada = calcular_tabuada(x)

print(f'CALCULANDO TABUADA DO {x}')
for i in range(1, 11):
    print(f'{x} x {i} = {tabuada(i)}')
