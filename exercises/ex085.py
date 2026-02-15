def rainbow_colors():
    yield 'red'
    yield 'orange'
    yield 'yellow'
    yield 'green'
    yield 'blue'
    yield 'indigo'
    yield 'violet'

generator = rainbow_colors()
for color in generator:
    print(color)  
