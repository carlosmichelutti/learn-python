odd_numbers = []
even_numbers = []
numbers = []

for _ in range(1, 8):
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        even_numbers.append(number)

    if number % 2 == 1:
        odd_numbers.append(number)

print(f'The even numbers recorded were: {even_numbers}.')
print(f'The odd numbers recorded were: {odd_numbers}.')
