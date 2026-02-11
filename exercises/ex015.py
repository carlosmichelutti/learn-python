full_name = str(input('Enter your full name: ')).strip()

upper_name = full_name.upper()
lower_name = full_name.lower()
total_letters = len(full_name) - full_name.count(' ')
first_name = full_name.split(' ')[0]
first_name_letter_count = len(first_name)

print(f'Your name in uppercase is: {upper_name}.')
print(f'Your name in lowercase is: {lower_name}.')
print(f'Your name has {total_letters} letters in total.')
print(f'Your first name is {first_name} and it has {first_name_letter_count} letters.')
