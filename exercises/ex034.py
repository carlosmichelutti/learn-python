weight = float(input('Enter your weight (kg): '))
height_cm = float(input('Enter your height (cm): '))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    print('You are underweight.')
elif bmi >= 18.5 and bmi < 25:
    print('You are at an ideal weight.')
elif bmi >= 25 and bmi < 30:
    print('You are overweight.')
elif bmi >= 30 and bmi < 40:
    print('You are obese.')
elif bmi >= 40:
    print('You have morbid obesity.')
