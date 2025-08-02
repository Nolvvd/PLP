#this is the first assignment for the intro to python course
num1=int (input("Enter your first number: "))
operator=input("Enter your operator: + - / * : ")
num2=int(input("Enter your second number: "))
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("ERROR: Invalid operator. Please use +, -, *, or /.")