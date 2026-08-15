def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return 
    print("Division by zero is not allowed")
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Result =", add(num1, num2))
    case "-":
        print("Result =", subtract(num1, num2))
    case "*":
        print("Result =", multiply(num1, num2))
    case "/":
        print("Result =", divide(num1, num2))
    case _:
        print("Invalid operator!")