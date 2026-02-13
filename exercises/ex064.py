lowest_names = []
highest_names = []
helper = []
group = []
highest = []
lowest = []
count = 0

while True:
    name = str(input('Enter the name: '))
    weight = float(input('Enter the weight: '))
    helper.append(name)
    helper.append(weight)
    group.append(helper[:])
    helper.clear()
    if count == 0:
        highest.append(group[count][1])
        highest_names.append(group[count][0])
        lowest.append(group[count][1])
        lowest_names.append(group[count][0])
        count += 1

    elif group[count][1] > highest[0]:
        highest.pop()
        highest.append(group[count][1])
        highest_names.pop()
        highest_names.append(group[count][0])
        count += 1

    elif group[count][1] == highest[0]:
        highest_names.insert(1, group[count][0])
        count += 1

    elif group[count][1] < lowest[0]:
        lowest.pop()
        lowest.append(group[count][1])
        lowest_names.pop()
        lowest_names.append(group[count][0])
        count += 1

    elif group[count][1] == lowest[0]:
        lowest_names.insert(1, group[count][0])
        count += 1

    answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if answer == 'N':
        print(f'{len(group)} people were registered.')
        print(f'The highest weight recorded was {highest} kg, belonging to {highest_names}.')
        print(f'The lowest weight recorded was {lowest} kg, belonging to {lowest_names}.')
        break

    elif answer != 'Y':
        print('Invalid response! Try again:')
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
