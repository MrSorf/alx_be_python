num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))


match operation: 
    case "+":
        result = num1 + num2 
    case "-":
        result = num1 - num2 
    case "*":
        result = num1 * num2 

    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
            result = None

    case _:
     print("Invalid operation!")
     result = None

if result is not None:
    print(f"The result is {result}")