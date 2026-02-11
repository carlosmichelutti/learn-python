length = float(input('Enter the wall length: '))
width = float(input('Enter the wall width: '))

area = length * width
paint_needed = area / 2

print(f'Your wall has dimensions {length}x{width} and its area is {area}m^2.')
print(f'A wall with area {area}m^2 needs {paint_needed:.0f} liters of paint to be fully painted.')
