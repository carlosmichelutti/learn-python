meters = float(input('Enter a distance in meters: '))

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print(f'The distance of {meters} meters corresponds to:')
print(f'{kilometers} in km.')
print(f'{hectometers} in hm.')
print(f'{decameters} in dam.')
print(f'{decimeters} in dm.')
print(f'{centimeters} in cm.')
print(f'{millimeters} in mm.')
