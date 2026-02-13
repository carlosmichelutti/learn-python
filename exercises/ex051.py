number_count = 0
largest_number = 0
smallest_number = 0
answer = 'S'
total = 0

while answer == 'S':
    number = int(input('Enter any integer: '))
    number_count += 1
    total += number

    if number_count == 1:
        largest_number = number
        smallest_number = number
    if number > largest_number:
        largest_number = number
    elif number < smallest_number:
        smallest_number = number

    answer =  str(input('Do you want to continue? [Y/N] ')).upper().strip()
    while True:
        if answer not in 'YN':
            print('Invalid option! Try again!')
            answer = str(input('Do you want to continue? [Y/N] ')).upper().strip()
            continue
        break

print(f'The average of all {number_count} numbers entered is {total / number_count}.')
print(f'The largest number entered was {largest_number}.')
print(f'The smallest number entered was {smallest_number}.')
