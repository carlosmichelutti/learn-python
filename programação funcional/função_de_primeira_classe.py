def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

from os import system
system('cls')
d = dobro
print(d(5))

q = quadrado
print(q(5))

funcs = [dobro, quadrado] * 5

for func, numero in zip(funcs, range(1, 11)):
    print(f'O {func.__name__} de {numero} e {func(numero)}')
