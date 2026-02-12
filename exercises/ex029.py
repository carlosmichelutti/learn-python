number1 = int(input('Enter any integer: '))
number2 = int(input('Enter another integer: '))

if number1 > number2:
    print(f'The first number is greater than the second, {number1} > {number2}.')
elif number2 > number1:
    print(f'The second number is greater than the first, {number2} > {number1}.')
elif number1 == number2:
    print(f'The two numbers are equal, {number1} = {number2}.')
