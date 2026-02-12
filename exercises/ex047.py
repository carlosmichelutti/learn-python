import os

number1 = int(input('Enter a number: '))
number2 = int(input('Enter another number: '))
condition = 0

while True:
    print('Choose what to do with the entered numbers: ')
    print('[1] Add them')
    print('[2] Multiply them')
    print('[3] Show the larger one')
    print('[4] New numbers')
    print('[5] Exit the program')
    condition = int(input('Choose an option: '))

    if condition == 1:
        os.system('cls')
        print(f'The sum of {number1} and {number2} is {number1 + number2}.')
        continue

    if condition == 2:
        os.system('cls')
        print(f'The product of {number1} and {number2} is {number1 * number2}.')
        continue

    if condition == 3:
        os.system('cls')
        if number1 > number2:
            print(f'The number {number1} is greater than {number2}.')
        elif number2 > number1:
            print(f'The number {number2} is greater than {number1}.')
        elif number2 == number1:
            print(f'The numbers {number1} and {number2} are equal.')
        continue

    if condition == 4:
        os.system('cls')
        number1 = int(input('Enter a new number: '))
        number2 = int(input('Enter another new number: '))
        continue

    if condition == 5:
        print('END')
        break
