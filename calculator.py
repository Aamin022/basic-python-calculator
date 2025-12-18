num1 = float(input("Enter first number: "))
op = input("choose (+, -, *, /) : ")
num2 = float(input("Choose second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error:Cant divide by zero")
else:
    print("wrong operation")
