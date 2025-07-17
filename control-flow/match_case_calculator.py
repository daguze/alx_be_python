num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

type_of_operation = (input("Choose the operation (+, -, *, /):"))

match type_of_operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero."
    case _:
        result = "Invalid operation."

print(f"Result: {result}")