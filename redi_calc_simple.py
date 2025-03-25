# ReDI calculator - Intro to Python class

# Functions we define
# Remember they are not executed by the Python interpreter
# unless we call them later in the code. That's why we define
# them here at the top
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("ReDI School - Intro to Python\n")

operation = input("Enter the operation (+, -, *, /): ")\

# Solution to invalid operations suggested by the students
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print(f"Invalid operation {operation}")
    quit()

value_1 = float(input("Enter the first value: "))
value_2 = float(input("Enter the second value: "))

# Solution to division by zero suggested by the students
if operation == "/" and value_2 == 0:
    print(f"Cannot divide by zero")
    quit()

# Solution to undeclared 'result' variable suggested by the students
result = None

if operation == "+":
    result = addition(value_1, value_2)
elif operation == "-":
    result = subtraction(value_1, value_2)
elif operation == "*":
    result = multiplication(value_1, value_2)
elif operation == "/":
    result = division(value_1, value_2)
#else:
    # Else removed on purpose
    # We already deal with invalid operations at the top
    # We cannot leave a blank else, because Python expects code idented after

# Solution to undeclared 'result' variable suggested by the students
if result is not None:
    print(f"Result: {result}")
