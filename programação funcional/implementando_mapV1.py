def mapear(function, list):
    for elemento in list:
        yield function(elemento)

print(list(mapear(lambda x: x ** 2, [2, 3, 4])))