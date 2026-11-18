# Module inside the 'student' package: student details

def get_student_details():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    student_class = input("Enter class: ")
    return {"name": name, "roll_no": roll_no, "class": student_class}
