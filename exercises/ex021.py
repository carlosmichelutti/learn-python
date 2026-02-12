name = str(input('Enter your name: '))

salary = float(input(f'{name}, enter your current salary in R$: '))

if salary > 1250.00:
    raise_amount = salary * (10 / 100)
    print(f'Your previous salary was R${salary:.2f}, and your current salary is R${(salary + raise_amount):.2f}.')
else:
    raise_amount = salary * (15 / 100)
    print(f'Your previous salary was R${salary:.2f}, and your current salary is R${(salary + raise_amount):.2f}.')
