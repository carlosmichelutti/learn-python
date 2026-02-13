matrix_numbers = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

third_column_sum = 0
highest = 0
even_sum = 0

for row in range(0, 3):
    for column in range(0, 3):
        matrix_numbers[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))

for row in range(0, 3):
    for column in range(0, 3):
        if matrix_numbers[row][column] % 2 == 0:
            even_sum = even_sum + matrix_numbers[row][column]

for row in range(0, 3):
    third_column_sum = third_column_sum + matrix_numbers[row][2]

for column in range(0, 3):
    if column == 0:
        highest = matrix_numbers[1][column]

    elif matrix_numbers[1][column] > highest:
        highest = matrix_numbers[1][column]

for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix_numbers[row][column]:^5}]', end=' ')
    print('')

print(f'The sum of even numbers in the matrix is {even_sum}.')
print(f'The sum of numbers in the 3rd column is {third_column_sum}.')
print(f'The highest value in the second row was {highest}.')
