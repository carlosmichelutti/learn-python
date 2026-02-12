number1 = int(input('Enter any number: '))
number2 = int(input('Enter another number: '))
number3 = int(input('Enter one more number: '))

smallest = number1
if number2 < number1 and number2 < number3:
    smallest = number2
if number3 < number1 and number3 < number2:
    smallest = number3

largest = number1
if number2 > number1 and number2 > number3:
    largest = number2
if number3 > number1 and number3 > number2:
    largest = number3

print(f'The smallest value entered was: {smallest}.')
print(f'The largest value entered was: {largest}.')
