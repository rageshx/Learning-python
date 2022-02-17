
#Calculator Basic
def calculator_basic():
    print("Calculator Basic")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("Enter your choice: ")
    choice = int(input())
    if choice == 1:
        print("Addition")
        print("Enter first number: ")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print("Result: ", num1 + num2)
        calculator_basic()
    elif choice == 2:
        print("Subtraction")
        print("Enter first number: ")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print("Result: ", num1 - num2)
        calculator_basic()
    elif choice == 3:
        print("Multiplication")
        print("Enter first number: ")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print("Result: ", num1 * num2)
        calculator_basic()
    elif choice == 4:
        print("Division")
        print("Enter first number: ")
        num1 = int(input())
        print("Enter second number: ")
        num2 = int(input())
        print("Result: ", num1 / num2)
        calculator_basic()
    elif choice == 5:
        print("Exit")
        exit()
    else:
        print("Invalid choice")
        calculator_basic()

