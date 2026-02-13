numbers_in_order = []
for num in range(0, 5):
    number = int(input('Enter any number: '))
    if num == 0 or number > numbers_in_order[-1]:
        numbers_in_order.append(number)
    else:
        position = 0
        while position < len(numbers_in_order):
            if number <= numbers_in_order[position]:
                numbers_in_order.insert(position, number)
                break
            position += 1

    if number > 0 and number < 6:
        print('Adding to the beginning of the list...')
    elif number > 6:
        print('Adding to the end of the list...')

print(f'The list in order is: {numbers_in_order}')
