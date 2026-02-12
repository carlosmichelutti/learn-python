number_count = 0
number = 0
total = 0
while True:
    number = int(input('Enter any integer [999 to stop]: '))
    if number == 999:
        break
    total += number
    number_count += 1

print(f'The sum of all {number_count} numbers entered is {total}.')
print(f'The average of all {number_count} numbers entered is {total / number_count}.')
