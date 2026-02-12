from random import choice

print('Let\'s play rock, paper, scissors! ')
print('Rock')
print('Paper')
print('Scissors')
computer_choice = choice(['rock', 'paper', 'scissors']).lower()
user_choice = str(input('Choose an option: ')).lower()

if computer_choice == user_choice:
    print('It\'s a tie! No one won this time.')
elif (computer_choice == 'rock' and user_choice == 'scissors'):
    print('I won! Try again!')
elif (computer_choice == 'scissors' and user_choice == 'paper'):
    print('I won! Try again!')
elif (computer_choice == 'paper' and user_choice == 'rock'):
    print('I won! Try again!')
elif (computer_choice == 'rock' and user_choice == 'paper'):
    print('Congrats! This time you beat me!')
elif (computer_choice == 'scissors' and user_choice == 'rock'):
    print('Congrats! This time you beat me!')
elif (computer_choice == 'paper' and user_choice == 'scissors'):
    print('Congrats! This time you beat me!')
