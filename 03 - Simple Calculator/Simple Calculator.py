# MISSION: BUGFIX and improvement
import os
def cls():
    """Clearing VS Code previous logs"""
    os.system('cls' if os.name == 'nt' else 'clear')  # only works on VS code


# calculator function
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Math operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """User interaction"""
    num1 = float(input("What's the first number?: "))
    calculation = True
    while calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: ")) 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        proceed = input(f'Last output: {answer}\ntype "y" to continue using calculator type "n" to restart\n').lower()
        if proceed == "y": 
            num1 = answer 
        else:
            calculation = False
            cls() 
            calculator() 
calculator()

