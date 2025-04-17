from os import system
def soma_sem_lambda(a, b):
    s = a + b
    return s

system('cls')
print(soma_sem_lambda(1, 10))

soma = lambda a, b,c ,d ,e : a+b+c/e*d
print(soma(1, 10, 10, 3, 23))

from functools import reduce
system('cls')
lista = [1, 2, 3, 4, 5, 6]

# eleva ao quadrado os elementos de lista para criar lista1
lista1 = list(map(lambda x: x**2, lista))
print("lista = ", lista, "\n\nlista1 = ", lista1)

lista = [1, 2, 3, 4, 5, 6]
produto = reduce(lambda x,y: x * y, lista) #retorna o produto de todos os elemento de lista
print("lista = ", lista,"\n\nproduto = ", produto)

lista = [1, 2, 3, 4, 5, 6]
lista1 = list(filter(lambda x: x % 2 != 0, lista)) #retorna a lista de números ímpares
print("lista = ", lista,"\n\nlista1 = ", lista1)