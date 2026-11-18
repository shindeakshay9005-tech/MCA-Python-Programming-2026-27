# Unit 2 - Q2: Variable-Length Arguments and Return Statement

def student_result(*marks):
    """*args collects marks of any number of subjects."""
    total = sum(marks)
    average = total / len(marks) if marks else 0
    highest = max(marks) if marks else 0
    return total, average, highest

def display_result(name, info, marks):
    """**kwargs collects extra student information."""
    total, average, highest = student_result(*marks)
    print("=" * 40)
    print(f"{'Student Result':^40}")
    print("=" * 40)
    print(f"{'Name':<15}: {name}")
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title():<15}: {value}")
    print("-" * 40)
    print(f"{'Total Marks':<15}: {total}")
    print(f"{'Average Marks':<15}: {average:.2f}")
    print(f"{'Highest Marks':<15}: {highest}")
    print("=" * 40)

def get_student_data():
    name = input("Enter student name: ")
    count = int(input("Number of subjects: "))
    marks = []
    for i in range(1, count + 1):
        marks.append(float(input(f"Marks in subject {i}: ")))
    roll_no = input("Roll number: ")
    student_class = input("Class: ")
    return name, marks, {"roll_no": roll_no, "class": student_class}

if __name__ == "__main__":
    name, marks, info = get_student_data()
    display_result(name, info, marks)
