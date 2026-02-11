student_name = str(input('Enter the student name: '))

grade1 = float(input(f'Enter the first grade for {student_name}: '))
grade2 = float(input(f'Enter the second grade for {student_name}: '))
average = (grade1 + grade2) / 2

if average >= 7:
    print(f'Congratulations {student_name}, you passed with an average of {average}.')
else:
    print(f'Unfortunately {student_name}, you did not pass with an average of {average}.')
