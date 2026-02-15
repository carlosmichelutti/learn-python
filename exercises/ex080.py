from random import randint

people = [
    {'name': 'Mariana', 'age': randint(10, 99)},
    {'name': 'Carlos', 'age': randint(10, 99)},
    {'name': 'Arthur', 'age': randint(10, 99)},
    {'name': 'Rebeca', 'age': randint(10, 99)},
    {'name': 'Rodolfo', 'age': randint(10, 99)},
    {'name': 'Maria', 'age': randint(10, 99)}
]

names_with_more_than_six_characters = list(filter(lambda person: len(person['name']) > 6, people))
minors = list(filter(lambda person: person['age'] < 18, people))
adults = list(filter(lambda person: person['age'] > 18, people))
print(f'Names with more than 6 characters: {list(map(lambda person: person["name"], names_with_more_than_six_characters))}')
print(f'Minors: {list(map(lambda person: person["name"], minors))}')
print(f'Adults: {list(map(lambda person: person["name"], adults))}')
