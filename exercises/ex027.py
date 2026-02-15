answer = str(input('Do you want to take out a loan? [Y/N] ')).upper().strip()
 
if answer == 'Y':
    total_value = float(input('What is the total price of the house? $'))
    salary = float(input('What is your salary? $'))
    years = int(input('In how many years do you want to pay it off? '))
    monthly_payment = total_value / years / 12

    if monthly_payment > (salary * 0.30):
        print('Error! You cannot take this loan because it exceeds 30% of your monthly salary.')
    else:
        print(f'You can take this loan, and you will pay ${monthly_payment:.2f} per month for {years} years.')
else: 
    print('Thanks, see you later!')
