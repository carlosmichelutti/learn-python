def calculate_area(width: int, length: int):
    area = width * length
    print(f'The area of a plot of land {width}x{length} is {area}m².')

width = int(input('Enter the width of the plot: '))
length = int(input('Enter the length of the plot: '))

calculate_area(width=width, length=length)
