max_weight = 0
min_weight = 0
for num in range(1, 6):
    weight = float(input(f'Enter the weight of person #{num}: '))
    if num == 1:
        max_weight = weight
        min_weight = weight
        continue
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight: 
        min_weight = weight

print(f'The highest weight read was {max_weight}kg.')
print(f'The lowest weight read was {min_weight}kg.')
