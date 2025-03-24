def addition(values_list):
    result = values_list[0]
    for i in values_list[1:]:
        result = result + i
    return result

def subtraction(values_list):
    result = values_list[0]
    for i in values_list[1:]:
        result = result - i
    return result

def multiplication(values_list):
    result = values_list[0]
    for i in values_list[1:]:
        result = result * i
    return result

def division(values_list):
    result = values_list[0]
    for i in values_list[1:]:
        result = result / i
    return result

print("Calculator Program in Python\n")

while True:
    n_values = int(input("Enter the number of values: "))
    operation = input("Enter the operation (+, -, /, *): ")
    values = []
    
    for i in range(n_values):
        v = float(input(f"Enter value {i + 1}: "))
        values.append(v)
    
    if operation == "+":
        result = addition(values)
    elif operation == "-":
        result = subtraction(values)
    elif operation == "*":
        result = multiplication(values)
    elif operation == "/":
        result = division(values)
    else:
        print(f"Invalid operation: {operation}")
        print("Valid operations: +, -, *, /")
        quit()
    
    print(f"Result: {result}")
