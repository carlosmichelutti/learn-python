from random import randint

people = [
    {'name': 'Carlos', 'age': randint(10, 99)},
    {'name': 'Felipe', 'age': randint(10, 99)},
    {'name': 'Marcos', 'age': randint(10, 99)},
]

ages = list(map(lambda person: person['age'], people))
names = list(map(lambda person: person['name'], people))

sentences = map(lambda name, age: f'{name} is {age} years old', names, ages)
print(*list(sentences), sep=', ', end='.\n')
