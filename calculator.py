def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    option = input("Enter option: ")
    
    if option in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if option == '1':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif option == '2':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif option == '3':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif option == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    return
                result = num1 / num2

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the calculator
calculator()