numbers = (
    int(input('Enter a number: ')),
    int(input('Enter a number: ')),
    int(input('Enter a number: ')),
    int(input('Enter a number: '))
)

print(f'The number 9 appeared {numbers.count(9)} times.')

if 3 not in numbers:
    print('No number 3 was entered.')
else:
    print(f'The first number 3 was entered at position {numbers.index(3) + 1}.')

for num in range(0, 4):
    if numbers[num] % 2 == 0:
        print(f'The even values entered were {numbers[num]}')

if all(n % 2 != 0 for n in numbers):
    print('No even number was entered.')
