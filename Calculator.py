import art
import os
logo = art.logo

def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    print(logo)

    num1 = float(input("Enter First Number : "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter Next Number : "))
        calculations = operations[operation_symbol]
        output_1 = calculations(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {output_1}")

        if input(f"Type 'y' to continue calculating with {output_1} or 'n' to start another operation : ") == "y":
            num1 = output_1
        else:
            should_continue = False
            os.system("cls")
            calculator()

calculator()
