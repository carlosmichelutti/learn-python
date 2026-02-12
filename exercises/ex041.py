number = int(input('Enter any number: '))
divisor_count = 0

for num in range(1, (number + 1)):
    if number % num == 0:
        divisor_count += 1

if divisor_count == 2:
    print(f'The number {number} is a prime number.')
elif divisor_count > 2:
    print(f'The number {number} is not a prime number.')
