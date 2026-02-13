simple_list = []
odd_list = []
even_list = []
position = 0
while True:
    number = int(input('Enter any number: '))
    simple_list.append(number)
    answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if answer == 'N':
        while True:
            if simple_list[position] % 2 == 0:
                even_list.append(simple_list[position])
                position += 1
            elif simple_list[position] % 2 == 1:
                odd_list.append(simple_list[position])
                position += 1
            if position == len(simple_list):
                break

        print(f'The normal list entered was: {simple_list}.')
        print(f'The list of odd numbers was: {odd_list}.')
        print(f'The list of even numbers was: {even_list}.')
        break

    elif answer != 'Y':
        print('Invalid response. Try again.')
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
