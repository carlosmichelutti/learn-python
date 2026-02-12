from random import randint

print('Let\'s play? I will think of a number from 1 to 10 and you try to guess it!!')
user_guess = 0
computer_number = randint(1, 10)
print('I picked a number from 1 to 10, try to guess it now!')
attempt_count = 0

while computer_number != user_guess:
    user_guess = int(input('What number did I pick? '))
    if user_guess != computer_number:
        print('You missed! Try again!')
        attempt_count += 1

print(f'Congrats, you got it in just {attempt_count} attempts.')
