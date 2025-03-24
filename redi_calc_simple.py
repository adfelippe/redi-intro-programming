def addition(value_a, value_b):
    return value_a + value_b

def subtraction(value_a, value_b):
    return value_a - value_b

def multiplication(value_a, value_b):
    return value_a * value_b

def division(value_a, value_b):
    return value_a / value_b

print("Calculator Program in Python\n")

operation = input("Enter the operation (+, -, /, *): ")
value_1 = float(input("Enter the first value: "))
value_2 = float(input("Enter the second value: "))

if operation == "+":
    result = addition(value_1, value_2)
elif operation == "-":
    result = subtraction(value_1, value_2)
elif operation == "*":
    result = multiplication(value_1, value_2)
elif operation == "/":
    result = division(value_1, value_2)
else:
    print(f"Invalid operation: {operation}")
    print("Valid operations: +, -, *, /")
    quit()

print(f"Result: {result}")
