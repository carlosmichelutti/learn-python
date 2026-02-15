def find_largest_value(numbers: list):
    largest_value = 0
    for number in numbers:
        if number > largest_value:
            largest_value = number
    print(f'The largest value found in the list {numbers} was {largest_value}.')
    
find_largest_value(numbers=[4, 5, 6, 9, 15])
find_largest_value(numbers=[1, 4, 5, 7, 3])
find_largest_value(numbers=[1, 10])
