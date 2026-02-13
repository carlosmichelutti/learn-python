student = {}
student['name'] = str(input('Enter the student name: ')).capitalize().strip()
student['average'] = float(input(f'Enter the average for student {student["name"]}: '))

if student['average'] >= 7.0:
    student['status'] = 'APPROVED'
elif student['average'] >= 5:
    student['status'] = 'RECOVERY'
else:
    student['status'] = 'FAILED'

print(f'{student["name"]} has an average of {student["average"]} and is {student["status"]}.')
