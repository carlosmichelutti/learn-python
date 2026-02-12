first_term = int(input('What is the first term of this arithmetic progression? '))
common_difference = int(input('What is the common difference of the progression? '))

for num in range(first_term, (first_term + (11 - 1) * common_difference), common_difference):
    print(num, end=' -> ') if num < (first_term + (11 - 1) * common_difference - common_difference) else print(num)
