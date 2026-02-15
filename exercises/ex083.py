from functools import reduce
from random import randint

def sum_without_lambda(numbers: list[int]) -> int:
    total = sum(numbers)
    return total

random_list = [randint(1, 10) for _ in range(randint(5, 10))]
sum_without_lambda(numbers=random_list)
sum_with_lambda = reduce(lambda num1, num2: num1 + num2, random_list, 0)

odd_list = list(filter(lambda number: number % 2 != 0 , random_list))
even_list = list(filter(lambda number: number % 2 == 0, random_list))
squared_list = list(map(lambda number: number**2, random_list))

print(f'Random list: {random_list}')
print(f'Sum without lambda: {sum_without_lambda(numbers=random_list)}')
print(f'Sum with lambda: {sum_with_lambda}')
print(f'Odd list: {odd_list}')
print(f'Even list: {even_list}')
print(f'Squared list: {squared_list}')
