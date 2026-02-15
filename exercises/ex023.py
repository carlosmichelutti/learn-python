distance = int(input('How many km will you travel? '))

if distance <= 200:
    print(f'The trip cost is ${(distance * 0.50):.2f}.')
else:
    print(f'The total trip cost will be ${(distance * 0.45):.2f}.')
