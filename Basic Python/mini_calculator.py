'''Task: Practice functions - Mini calculator
🎯 Outcome (By doing this you should): Practice using separate functions to do each of the
different operations of a mini calculator
Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about
functions.
Create a Python file called calculator.py and complete a viable basic calculator using
functions.
MVP (each of these should be in a separate function):
• Can add 2 numbers
• Can subtract 2 numbers
• Can multiply 2 numbers
• Can divide 2 numbers
Taking it to the next level:
• Implement more complex operations, such as handling parentheses, exponentiation
• More advanced operations should continue to be broken into separate functions'''

def add(x:float, y:float)->float:
    return x + y

def subtract(x:float, y:float)->float:
    return x - y

def multiply(x:float, y:float)->float:
    return x * y

def divide(x:float, y:float)->float:
    return x / y

def exp(x:float, y:float)->float:
    return x ** y

def check_is_balanced(string:str)->bool:
    open_count = 0
    close_count =0
    for char in string:
        if char == '(': open_count += 1
        if char == ')': close_count += 1
    return open_count == close_count

def invalid_characters_present(string:str)->bool:
    valid_chars = ['1','2','3','4','5','6','7','8','9','0',
                   '-', '+', '*', 'x', '/', '^', '(', ')']
    for char in string:
        if char not in valid_chars:
            print(f"\'{char}\' is not a valid character.")
            return True
    return False

def run_calculator():
    while(True):
        equation = input("Enter an equation:\n")
        if not check_is_balanced(equation):
            print("Parentheses are unbalanced.\nTry again.")
        elif invalid_characters_present(equation) :
            print("Try again.")
        else:
            break


run_calculator()
