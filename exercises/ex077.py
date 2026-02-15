def validate_integer():
    while True:
        number = str(input('Enter a number: '))
        if number.isnumeric():
            return int(number)
        else:
            print(f'Error! The value {number} is not a valid integer.')

number = validate_integer()
print(f'You just entered the number {number}.')
