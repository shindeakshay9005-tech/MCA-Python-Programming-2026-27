# Module inside the 'student' package: student results

def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Class"
    elif average >= 40:
        return "Pass"
    return "Fail"
