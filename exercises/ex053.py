print('=' * 50)
print('{:^50}'.format('Bank'))
print('=' * 50)

notes_50 = 0
notes_20 = 0
notes_10 = 0
notes_1 = 0

withdrawal = float(input('How much do you want to withdraw? $'))

while True:
    if withdrawal > 49:
        withdrawal -= 50
        notes_50 += 1
    elif withdrawal > 19:
        withdrawal -= 20
        notes_20 += 1
    elif withdrawal > 9:
        withdrawal -= 10
        notes_10 += 1
    elif withdrawal > 0:
        withdrawal -= 1
        notes_1 += 1
    elif withdrawal == 0:
        print(f'Total number of $50 notes - {notes_50} notes.')
        print(f'Total number of $20 notes - {notes_20} notes.')
        print(f'Total number of $10 notes - {notes_10} notes.')
        print(f'Total number of $1 notes - {notes_1} notes.')
        break
