numbers_in_words = (
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
    'TEN',
    'ELEVEN',
    'TWELVE',
    'THIRTEEN',
    'FOURTEEN',
    'FIFTEEN',
    'SIXTEEN',
    'SEVENTEEN',
    'EIGHTEEN',
    'NINETEEN',
    'TWENTY',
)

user_choice = int(input('Choose a number between 0 and 20: '))
while True:
    if user_choice > 20:
        user_choice = int(input('Invalid number! Choose a number between 0 and 20: '))
    else:
        break

print(f'The number you chose in words was {user_choice} = {numbers_in_words[user_choice]}.')
