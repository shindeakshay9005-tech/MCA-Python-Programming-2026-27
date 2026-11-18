# Unit 4 - Q1: Exception Handling

def divide(a, b):
    return a / b

def get_index_value(items, index):
    return items[index]

# 1. ZeroDivisionError
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = divide(num, den)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:                              # 2. Invalid numerical input
    print("Error: please enter valid integers")
else:                                           # runs only when no exception occurs
    print("Division result:", result)
finally:                                        # always runs
    print("Division block finished\n")

# 3. IndexError
items = [10, 20, 30]
try:
    idx = int(input("Enter list index to access (0-2): "))
    print("Value:", get_index_value(items, idx))
except IndexError:
    print("Error: list index out of range")
except ValueError:
    print("Error: index must be an integer")
finally:
    print("Index block finished\n")

# 4 & 7. raise ValueError when age < 18
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above to register")
    return "Registration successful"

try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except ValueError as e:
    print("Error:", e)
finally:
    print("Age check finished")
