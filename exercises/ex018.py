from random import shuffle

student1 = input('Enter the name of the 1st student: ')
student2 = input('Enter the name of the 2nd student: ')
student3 = input('Enter the name of the 3rd student: ')
student4 = input('Enter the name of the 4th student: ')

students = [student1, student2, student3, student4]
shuffle(students)

print(f'The presentation order will be: {students}.')
