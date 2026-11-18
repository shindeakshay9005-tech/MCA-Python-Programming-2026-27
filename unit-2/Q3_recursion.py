# Unit 2 - Q3: Recursive Functions

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed) recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(terms, current=0):
    """Recursively build the Fibonacci series with 'terms' values."""
    if current >= terms:
        return []
    return [fibonacci(current)] + fibonacci_series(terms, current + 1)

if __name__ == "__main__":
    num = int(input("Enter a number for factorial: "))
    print(f"Factorial of {num} is {factorial(num)}")

    n = int(input("Enter number of Fibonacci terms: "))
    print("Fibonacci series:", fibonacci_series(n))
