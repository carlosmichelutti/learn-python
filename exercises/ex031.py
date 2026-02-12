from datetime import datetime
from time import sleep

birth_year = int(input('Enter your birth year: '))
age = datetime.today().year - birth_year
print('Analyzing your swimming category...')
sleep(3)

if age <= 9:
    print('Your category is the youth category.')
elif age <= 14:
    print('Your category is the child category.')
elif age <= 19:
    print('Your category is the junior category.')
elif age <= 25:
    print('Your category is the senior category.')
elif age > 25:
    print('Your category is the master category.')
