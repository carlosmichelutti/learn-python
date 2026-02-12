table_number = int(input('Choose a number for its multiplication table: '))

for num in range(1, 10 + 1):
    print(f'{table_number} x {num} = {table_number * num}')
