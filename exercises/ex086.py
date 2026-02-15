from random import randint

def map_function(function, items):
    for element in items:
        yield function(element)

print(list(map_function(lambda x: x ** 2, [randint(1, 10) for _ in range(randint(1, 10))])))
print(list(map_function(lambda x: x * 2, [randint(1, 10) for _ in range(randint(1, 10))])))
