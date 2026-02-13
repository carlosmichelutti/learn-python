import random

drawn_numbers = (
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10)
)

print(f'The drawn numbers were: {drawn_numbers}')

highest_number = 0
lowest_number = 0

while True:

    if drawn_numbers[0] == drawn_numbers[0]:
        highest_number = drawn_numbers[0]
        lowest_number = drawn_numbers[0]

    if drawn_numbers[1] > highest_number:
        highest_number = drawn_numbers[1]

    elif drawn_numbers[1] < lowest_number:
        lowest_number = drawn_numbers[1]

    if drawn_numbers[2] > highest_number:
        highest_number = drawn_numbers[2]

    elif drawn_numbers[2] < lowest_number:
        lowest_number = drawn_numbers[2]

    if drawn_numbers[3] > highest_number:
        highest_number = drawn_numbers[3]

    elif drawn_numbers[3] < lowest_number:
        lowest_number = drawn_numbers[3]

    if drawn_numbers[4] > highest_number:
        highest_number = drawn_numbers[4]

    elif drawn_numbers[4] < lowest_number:
        lowest_number = drawn_numbers[4]
    break

print(f'The highest drawn value was {highest_number}.')
print(f'The lowest drawn value was {lowest_number}.')
