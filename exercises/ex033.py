lado1 = float(input('Enter the value of the 1st side of the triangle: '))
lado2 = float(input('Enter the value of the 2nd side of the triangle: '))
lado3 = float(input('Enter the value of the 3rd side of the triangle: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 == lado3:
        print('This triangle exists and is an equilateral triangle.')
    elif lado1 != lado2 != lado3 != lado1:
        print('This triangle is possible and is a scalene triangle.')
    else: 
        print('This triangle is an isosceles triangle.')
else: 
    print('This triangle cannot exist.')
