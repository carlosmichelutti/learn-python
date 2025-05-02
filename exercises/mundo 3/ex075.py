from random import randint

def sortear_numeros() -> list:
    numeros = []
    for _ in range(0, 5):
        numeros.append(int(randint(1, 10)))
    return numeros

def somar_numeros(numeros: list) -> int:
    total = 0
    for numero in numeros:
        total += numero
    return total

numeros = sortear_numeros()
total = somar_numeros(numeros)

print(f'A soma dos números {numeros} é igual a {total}.')
