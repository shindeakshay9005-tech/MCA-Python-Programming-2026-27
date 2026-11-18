# Unit 4 - Q5: Command-Line Arguments
# Usage:
#   python command_line_calculator.py 10 + 5
#   python command_line_calculator.py 10 "*" 5    (quote * so the shell doesn't expand it)

import sys

VALID_OPERATORS = {"+", "-", "*", "/"}

if len(sys.argv) != 4:
    print("Usage: python command_line_calculator.py <num1> <operator> <num2>")
    print("Operators: +, -, *, /")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: the two numbers must be numeric")
    sys.exit(1)

if operator not in VALID_OPERATORS:
    print("Error: operator must be one of +, -, *, /")
    sys.exit(1)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    if num2 == 0:
        print("Error: division by zero")
        sys.exit(1)
    result = num1 / num2

print(f"{num1} {operator} {num2} = {result}")
