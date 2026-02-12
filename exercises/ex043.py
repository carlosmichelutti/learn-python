import os

pessoas_maiores_de_idade = 0
women_count = 0
oldest_man_name = None
youngest_age = 0
oldest_age = 0

for c in range (1, 5):
    gender = str(input('What is your gender? [M/F]? ')).upper().strip()
    name = str(input('What is your name? ')).capitalize().strip()
    age = int(input(f'How old are you, {name}? '))
    os.system('cls')
    if gender == 'F':
        women_count += 1

    if gender == 'M' and age > oldest_age:
        oldest_age = age
        oldest_man_name = name

print(f'Oldest man: {oldest_man_name} at {oldest_age} years old.')
print(f'Number of women in the group: {women_count}.')
