# Unit 2 - Q4: Scope, Lifetime and Lambda Functions

# ---- Global variable (created when the program starts, lives until it ends)
counter = 10

def show_local():
    # ---- Local variable (created when the function is called,
    #      destroyed when the function returns)
    local_msg = "I exist only inside show_local()"
    print(local_msg)
    print("Reading global inside function:", counter)

def modify_global():
    global counter          # tells Python to use the global 'counter'
    counter += 5
    print("Counter after global update (inside function):", counter)

def try_access_local():
    inner = 42
    return inner

if __name__ == "__main__":
    print("Global counter at start:", counter)
    show_local()
    modify_global()
    print("Global counter after modify_global():", counter)

    # Local variable is not accessible outside its function
    try:
        print(local_msg)
    except NameError as e:
        print("Accessing local outside function ->", e)

    print("Value returned from local scope:", try_access_local())

    # Lifetime explanation:
    # - Global variables live from program start until program end.
    # - Local variables live only during one function call; each call creates new ones.

    # Lambda functions
    square = lambda x: x ** 2
    cube = lambda x: x ** 3
    maximum = lambda a, b: a if a > b else b
    addition = lambda a, b: a + b

    print("Square of 4:", square(4))
    print("Cube of 3:", cube(3))
    print("Maximum of 7 and 12:", maximum(7, 12))
    print("Addition of 5 and 9:", addition(5, 9))
