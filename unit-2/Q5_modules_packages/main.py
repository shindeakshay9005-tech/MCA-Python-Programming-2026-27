# Main program: uses the user-defined module and package.
# Run from this folder:  python main.py

import arithmetic                                  # import entire module
from arithmetic import add, subtract               # import selected functions
from student import get_student_details, calculate_grade   # via __init__.py
from student import results                        # import package module

if __name__ == "__main__":
    print("Addition:", arithmetic.add(12, 8))
    print("Subtraction:", subtract(12, 8))
    print("Multiplication:", arithmetic.multiply(12, 8))
    print("Division:", arithmetic.divide(12, 8))

    print("\n--- Student Details ---")
    details = get_student_details()
    print(details)

    marks = [78, 65, 82]
    print("\nGrade (using __init__ import):", calculate_grade(marks))
    print("Grade (using results module):", results.calculate_grade([35, 45, 50]))
