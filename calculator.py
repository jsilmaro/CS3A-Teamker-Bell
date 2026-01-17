# Member 1 (Janelle): Create the add function and the loop then commit.

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def main():
    """Main calculator loop"""
    print("=== Simple Calculator ===")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit")

    while True:
        operation = input("\nEnter operation (add/subtract/multiply/divide/quit): ").lower()

        if operation == 'quit':
            print("Goodbye!")
            break
        elif operation == 'add':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            except ValueError:
                print("Please enter valid numbers!")
        elif operation == 'subtract':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            except ValueError:
                print("Please enter valid numbers!")
        elif operation == 'multiply':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = multiply(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")
            except ValueError:
                print("Please enter valid numbers!")
        elif operation == 'divide':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ValueError:
                print("Please enter valid numbers!")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
        else:
            print("Unknown operation!")

if __name__ == "__main__":
    main()

