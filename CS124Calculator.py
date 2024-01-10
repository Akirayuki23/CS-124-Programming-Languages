def add(e, b):
    return e + b

def subtract(e, b):
    return e - b

def multiply(e, b):
    return e * b

def divide(e, b):
    try:
        result = e / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    
    print("Result: ", result)
else:
    print("Invalid input")