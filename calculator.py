# Member 1 (Janelle): Basic structure with add function and main loop

def add(a, b):
    """Add two numbers"""
    return a + b

def main():
    """Main calculator loop"""
    print("=== Simple Calculator ===")
    print("Available operations: add")
    print("Type 'quit' to exit")
    
    while True:
        operation = input("\nEnter operation (add/quit): ").lower()
        
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
        else:
            print("Unknown operation!")

if __name__ == "__main__":
    main()