# Unit 2 - Q1: Functions and Function Arguments

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def calculate(a, b, operation="add"):
    """Default argument: operation defaults to 'add'."""
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    func = operations.get(operation)
    if func is None:
        return "Invalid operation"
    return func(a, b)

if __name__ == "__main__":
    # Positional arguments
    print("Addition (positional):", add(10, 5))
    print("Subtraction (positional):", subtract(10, 5))

    # Keyword arguments
    print("Multiplication (keyword):", multiply(b=4, a=3))
    print("Division (keyword):", divide(b=2, a=9))

    # Default argument
    print("Default operation (add):", calculate(8, 2))
    print("Explicit operation (divide):", calculate(8, 2, operation="divide"))
    print("Explicit operation (multiply):", calculate(8, 2, "multiply"))
