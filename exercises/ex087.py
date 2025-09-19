from random import randint

def mapear(function, list):
    return (function(elemento) for elemento in list)

print(list(mapear(lambda x: x ** 2, [randint(1, 10) for _ in range(randint(1, 10))])))
print(list(mapear(lambda x: x * 2, [randint(1, 10) for _ in range(randint(1, 10))])))
