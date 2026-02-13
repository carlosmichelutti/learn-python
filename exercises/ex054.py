count_over_1000 = 0
product_count = 0
lowest_price = 0
lowest_name = ''
answer = 'Y'
lowest = 0
total = 0

while answer != 'N':
    name = str(input('What is the product name? '))
    price = float(input('What is the product price? R$'))
    product_count += 1
    total += price

    if price > 1000:
        count_over_1000 += 1

    if product_count == 1:
        lowest_name = name
        lowest_price = price

    if price < lowest_price:
        lowest_name = name
        lowest_price = price

    while True:
        answer = str(input('Do you want to continue [Y/N]? ')).upper().strip()
        if answer not in 'YN':
            print('Invalid response. Try again.')
            continue
        if answer == 'N':
            print(f'The total amount spent on the {product_count} products was R${total}.')
            print(f'{count_over_1000} products cost more than R$1000.00.')
            print(f'The cheapest product entered was {lowest_name}, costing R${lowest_price}.')
            break
        else:
            break
