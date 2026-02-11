full_name = str(input('Enter your full name: ')).strip()

print(f'Nice to meet you, {full_name}!')
print(f'Your first name is {full_name.split()[0].capitalize()}.')
print(f'Your last name is {full_name.split()[-1].capitalize()}.')
