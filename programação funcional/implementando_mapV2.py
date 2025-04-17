def mapear(function, list):
    return (function(elemento) for elemento in list)

print(list(mapear(lambda x: x ** 2, [2, 3, 4])))