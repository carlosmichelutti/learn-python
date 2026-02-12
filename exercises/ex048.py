from random import randrange

factorial_number = randrange(1, 10)
product = factorial_number
factorial = 0

while factorial_number >= 1:
    print(f'{factorial_number} x', end=' ') if factorial_number > 1 else print(f'{factorial_number} = {product}', end=' ')
    factorial_number = factorial_number - 1
    if factorial_number > 0:
        product = factorial_number * product
