from datetime import datetime

current_year = datetime.today().year
gender = str(input('Enter your gender [M/F]: ')).upper()

if gender == 'F':
    print('You are not required to enlist in the army. See you later!')
else:
    birth_year = int(input('What year were you born? '))
    age = current_year - birth_year
    if age < 18:
        print(
            f'You are not old enough to enlist in the army. You will be able to '
            f'enlist in {abs(age - 18)} years. Your enlistment will be in '
            f'{birth_year + 18}.'
        )
    elif age == 18:
        print('You are at the right age to enlist in the army. Do not forget.')
    elif age > 18:
        print(
            f'Enlist now! You are {age - 18} years late for your military service. '
            f'Your mandatory enlistment was in {birth_year + 18}.'
        )
