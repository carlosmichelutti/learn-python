student_name = str(input('Enter the student name: '))
grade1 = float(input(f'Enter the first grade for {student_name}: '))
grade2 = float(input(f'Enter the second grade for {student_name}: '))

average = float((grade1 + grade2) / 2)

if average < 5.0:
    print('Failed! Your average was below the required level.')
elif average > 5.0 and average < 6.9:
    print('Recovery! Your grade is reasonable. Improve it to pass the year.')
elif average >= 7.0:
    print('Congratulations! You passed and moved on to the next year! See you next year!')
