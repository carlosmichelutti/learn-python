number_count = 0
numbers = []
while True:
    number = int(input('Enter any number: '))
    numbers.append(number)
    number_count += 1
    answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()

    if answer == 'N':
        print('')
        print(f'{number_count} numbers were entered.')
        numbers.sort(reverse=True)
        print(f'The list in descending order is {numbers}.')
        break

    elif answer != 'Y':
        print('Invalid response. Try again')
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
