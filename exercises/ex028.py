number = int(input('Enter an integer: '))

print('You want to convert this number to:')
print('[1] - Binary')
print('[2] - Octal')
print('[3] - Hexadecimal')

conversion = int(input('Choose an option: '))

if conversion == 1:
    print(f'The number {number} converted to binary is {bin(number)[2:]}.')
elif conversion == 2:
    print(f'The number {number} converted to octal is {oct(number)[2:]}.')
elif conversion == 3:
    print(f'The number {number} converted to hexadecimal is {hex(number)[2:]}.')
