from functools import reduce
from random import randint

people = [
    {'name': 'Mariana', 'age': randint(10, 99)},
    {'name': 'Carlos', 'age': randint(10, 99)},
    {'name': 'Arthur', 'age': randint(10, 99)},
    {'name': 'Rebeca', 'age': randint(10, 99)},
    {'name': 'Rodolfo', 'age': randint(10, 99)},
    {'name': 'Maria', 'age': randint(10, 99)}
]

ages = list(map(lambda person: person['age'], people))
adult_ages = list(filter(lambda age: age > 18, ages))
age_sum = reduce(lambda total, age: total + age, adult_ages, 0)
print(f'The sum of the ages of adults is {age_sum}.')
