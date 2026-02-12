from datetime import datetime

current_year = datetime.today().year
adults_count = 0
minors_count = 0
for num in range(0, 7):
    birth_year = int(input(f'Enter the birth year of person #{num + 1}: '))
    if current_year - birth_year >= 18:
        adults_count += 1
    else: 
        minors_count += 1

print(f'There are {adults_count} adults in the group.')
print(f'There are {minors_count} minors in the group.')
