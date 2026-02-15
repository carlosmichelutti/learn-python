def count_numbers(start: int, end: int, step: int):
    if start > end:
        end -= 1
    else:
        end += 1
    for number in range(start, end, step):
        print(number, end=' - ')
    print('')

count_numbers(start=1, end=10, step=1)
count_numbers(start=10, end=0, step=-2)
start = int(input('Start: '))
end = int(input('End: '))
step = int(input('Step: '))
count_numbers(start=start, end=end, step=step)
