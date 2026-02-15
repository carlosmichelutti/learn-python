from random import randint

def generate_numbers():
    numbers = []
    for _ in range(0, 5):
        numbers.append(int(randint(1, 10)))
    return numbers

def sum_numbers(numbers: list):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = generate_numbers()
total = sum_numbers(numbers)

print(f'The sum of the numbers {numbers} is {total}.')
