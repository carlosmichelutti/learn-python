numbers = [[], []]
value = 0

for c in range(1, 8):
    value = int(input('Enter a value: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)

numbers[0].sort()
numbers[1].sort()
print(f'All numbers {numbers}')
print(f'Even numbers: {numbers[0]}')
print(f'Odd numbers: {numbers[1]}')
