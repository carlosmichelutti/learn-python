from functools import reduce
from random import randint

def soma_sem_lambda(numeros: list[int]) -> int:
    soma = sum(numeros)
    return soma

lista_aleatoria = [randint(1, 10) for _ in range(randint(5, 10))]
soma_sem_lambda(numeros=lista_aleatoria)
soma_com_lambda = reduce(lambda num1, num2: num1 + num2, lista_aleatoria, 0)

lista_impares = list(filter(lambda numero: numero % 2 != 0 , lista_aleatoria))
lista_pares = list(filter(lambda numero: numero % 2 == 0, lista_aleatoria))
lista_potencia = list(map(lambda numero: numero**2, lista_aleatoria))

print(f'Lista aleatória: {lista_aleatoria}')
print(f'Soma sem lambda: {soma_sem_lambda(numeros=lista_aleatoria)}')
print(f'Soma com lambda: {soma_com_lambda}')
print(f'Lista de ímpares: {lista_impares}')
print(f'Lista de pares: {lista_pares}')
print(f'Lista ao quadrado: {lista_potencia}')
