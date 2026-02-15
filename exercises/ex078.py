def grades(*scores, show=False):

    average = 0
    grade_data = {}
    grade_data['number_of_tests'] = len(scores)
    grade_data['highest_grade'] = 0
    grade_data['lowest_grade'] = 0
    grade_data['average'] = 0

    for grade in scores:
        average += grade
        if grade_data['highest_grade'] == 0 and grade_data['lowest_grade'] == 0:
            grade_data['highest_grade'] = grade
            grade_data['lowest_grade'] = grade
        elif grade > grade_data['highest_grade']:
            grade_data['highest_grade'] = grade
        elif grade < grade_data['lowest_grade']:
            grade_data['lowest_grade'] = grade

    average = average / len(scores)
    grade_data['average'] = average

    if show:
        if grade_data['average'] > 7:
            grade_data['Status'] = 'GOOD'
        elif grade_data['average'] > 5:
            grade_data['Status'] = 'FAIR'
        else:
            grade_data['Status'] = 'POOR'
        print(grade_data)
    else:
        print(grade_data)

result = grades(9, 4.5, 10, 7, show=True)
