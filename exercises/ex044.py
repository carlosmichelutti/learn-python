phrase = str(input('Enter a phrase: ')).strip().lower().replace(' ', '')
reversed_phrase = phrase[::-1].strip().lower().replace(' ', '')

if phrase == reversed_phrase:
    print(f'The phrase {phrase} is a palindrome and reads the same forward and backward.')
    print(f'Normal phrase: {phrase}.')
    print(f'Reversed phrase: {reversed_phrase}.')
else:
    print(f'The phrase {phrase} is not a palindrome.')
