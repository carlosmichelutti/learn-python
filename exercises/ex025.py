from time import sleep
import random

computer_number = random.randint(1, 5)
print('Thinking of a number from 1 to 5...')
sleep(2)
user_number = int(input('Guess which number I thought of: '))

if user_number == computer_number:
    print(f'You got it right! I thought of the number {computer_number}.')
else:
    print(f'You got it wrong... I thought of the number {computer_number} and you said {user_number}. Try again!')
