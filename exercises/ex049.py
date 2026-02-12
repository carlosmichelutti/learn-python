first_term = int(input('What is the first term of this arithmetic progression? '))
common_difference = int(input('What is the common difference of the progression? '))
next_term = first_term
cont = 1
resp = 1

for num in range(10):
    print(f'{next_term} -> ', end='') if num < 9 else print(next_term)
    next_term += common_difference

quantity_terms = int(input('How many more terms do you want to show? '))
while True:
    for num in range(0, quantity_terms):
        print(f'{next_term} -> ', end='') if num < quantity_terms - 1 else print(next_term)
        next_term += common_difference

    quantity_terms = int(input('How many more terms do you want to show? '))
    if quantity_terms == 0:
        break
