price = float(input('What is the normal price of the product? $'))

print('What is the payment condition? ')
print('[1] Cash/check (upfront)')
print('[2] Card (upfront)')
print('[3] Card in 2 installments')
print('[4] Card in 3 or more installments')

payment_condition = int(input('Enter an option: '))
if payment_condition == 1:
    print(f'The product price gets a 10% discount and the new amount is ${(price * 0.90):.2f}.')

elif payment_condition == 2:
    print(f'The product price gets a 5% discount and the new amount is ${(price * 0.95):.2f}.')

elif payment_condition == 3:
    total_installments = 2
    print(
        f'The product price will be ${(price * 0.95):.2f}, '
        f'in {total_installments} installments of ${((price * 0.95) / total_installments):.2f} each.'
    )

elif payment_condition == 4:
    total_installments = int(input('How many installments will you use? '))
    print(
        f'The product price will be ${(price * 0.95):.2f}, '
        f'in {total_installments} installments of ${((price * 0.95) / total_installments):.2f} each.'
    )
