speed = int(input('Enter the car speed in km/h: '))

if speed > 80:
    fine_amount = (speed - 80) * 7
    print(f'You exceeded the maximum speed by {speed - 80} km/h on the highway. Your fine is ${fine_amount}.')
else:
    print('Congratulations, your speed is within the highway limit. Keep it up!')
