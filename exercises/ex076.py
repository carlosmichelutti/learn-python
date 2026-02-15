from datetime import datetime

def check_voting_requirement(birth_year: int):

    if (datetime.today().year - birth_year) < 16:
        print(f'At {datetime.today().year - birth_year} years old: voting denied.')
        return
    elif (datetime.today().year - birth_year) >= 18 and (datetime.today().year - birth_year) <= 65:
        print(f'At {datetime.today().year - birth_year} years old: voting mandatory.')
        return
    else:
        print(f'At {datetime.today().year - birth_year} years old: voting optional.')
        return
        
birth_year = int(input('What is your birth year? '))
check_voting_requirement(birth_year)
