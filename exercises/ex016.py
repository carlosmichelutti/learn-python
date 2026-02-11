days = int(input('How many days rented? '))
kilometers = int(input('How many kilometers driven? '))

total_cost = (60 * days) + (kilometers * 0.15)

print(f'The total cost to pay when returning the car is R${total_cost:.2f}.')
