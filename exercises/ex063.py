helper = []
group = []
highest = 0
lowest = 0
while True:
    helper.append(str(input('Name: ')))
    helper.append(float(input('Weight (KG): ')))
    if len(group) == 0:
        highest = helper[1]
        lowest = helper[1]
    else:
        if helper[1] > highest:
            highest = helper[1]
        if helper[1] < lowest:
            lowest = helper[1]

    group.append(helper[:])
    helper.clear()
    answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if answer == 'N':
        print(f'A total of {len(group)} people were registered.')
        print(f'The highest weight was {highest} kg, belonging to ', end='')
        for person in group:
            if person[1] == highest:
                print(person[0], end='.\n')

        print(f'The lowest weight entered was {lowest} kg, belonging to ', end='')
        for person in group:
            if person[1] == lowest:
                print(person[0], end='.\n')
        break

    elif answer != 'Y':
        print('Invalid response. Try again: ')
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
