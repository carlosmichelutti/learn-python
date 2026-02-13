import os

people_over_18 = 0
women_count = 0
men_count = 0
answer = 'Y'

while answer == 'Y':
    age = int(input('How old are you? '))
    while True:
        gender = str(input('What is your gender [M/F]? ')).upper().strip()
        if gender not in 'MF':
            print('Invalid option! Try again.')
            continue
        break

    if age > 18:
        people_over_18 += 1
    if gender == 'M':
        men_count += 1
    if gender == 'F':
        women_count += 1

    while True:
        answer = str(input('Do you want to continue [Y/N]? ')).upper().strip()
        if answer not in 'YN':
            print('Invalid option! Try again.')
            continue
        if answer == 'N':
            os.system('cls')
            print(f'{people_over_18} men over 18 years old were entered.')
            print(f'{women_count} women were entered.')
            print(f'{men_count} men were entered.')
            break

        os.system('cls')
        break
