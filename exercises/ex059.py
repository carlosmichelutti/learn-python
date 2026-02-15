numbers = list()

highest_number = 0
lowest_number = 0

for num in range(0, 5):
    numbers.append(int(input(f'Enter a value for position {num}: ')))
    if num == 0:
        highest_number = numbers[num]
        lowest_number = numbers[num]

    if numbers[num] > highest_number:
        highest_number = numbers[num]

    elif numbers[num] < lowest_number:
        lowest_number = numbers[num]

print(f'Numbers: {numbers}')
print(
    f'The lowest number entered was {lowest_number} at positions '
    f'{", ".join(str(i) for i, v in enumerate(numbers) if v == lowest_number)}'
)
print(
    f'The highest number entered was {highest_number} at positions '
    f'{", ".join(str(i) for i, v in enumerate(numbers) if v == highest_number)}'
)
