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
                   '-', '+', '*', 'x', '/', '^', '(', ')',
                   '.', ' ']
    for char in string:
        if char not in valid_chars:
            print(f"\'{char}\' is not a valid character.")
            return True
    return False

def tokenize_input(equation:str)->list:
    # clean string
    equation = equation.replace(" ", "")
    #tokenize
    tokens = []
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    current_token = ""
    for i in range(len(equation)):
        if equation[i] in numbers or equation[i]=='.':
            current_token = current_token + str(equation[i])
        else:
            if current_token != '':
                tokens.append(current_token)
                current_token = ''
            tokens.append(equation[i])
    if current_token != '':
        tokens.append(current_token)
    return tokens

class Node:
    id = 0
    def __init__(self, token:str, is_leaf:bool=False, is_saturated:bool=False, left_child=None, right_child=None):
        self.id = Node.id
        Node.id += 1
        self.token=token
        self.left_child:Node = left_child
        self.right_child:Node = right_child
        self.is_leaf:bool = is_leaf
        self.is_saturated:bool = is_saturated

#TODO: THIS WILL GET STUCK AND NOT MOVE BACK UP THE TREE RN
# This might be fixed??
def find_active_node(root:Node)->Node:
    active = root
    depth = 0
    stack=[active]
    while len(stack) > 0:
        if active.is_saturated:
            active = stack.pop()
        elif active.left_child is None:
            return active
        elif active.left_child.is_leaf:
            if active.right_child is None:
                return active
            elif active.right_child.is_leaf:
                active.is_saturated = True
            else:
                stack.append(active)
                active = active.right_child
        else:
            stack.append(active)
            active = active.left_child
        depth += 1
        if depth > 100:
            raise Exception("ERROR: Parse failure, Tree depth >100")
    return active

#TODO: SHOULD I JUST MAKE THIS RECURSIVE???

def build_equation_tree(tokens:list)->Node:
    # if first token isn't a number or bracket, error
    # first token is root node
    # when an operator is hit, the tree probably reshuffles
    # is it easier to convert to RPN first? isn't that just the same task?
    root = Node(tokens.pop(0))
    active_node = root
    while len(tokens) > 0:
        t:Node = Node(tokens.pop())
        #if t is a number, it's a leaf node
        if t.token.isnumeric():
            t.is_leaf = True
            if active_node.left_child is None:
                active_node.left_child = t
            elif active_node.right_child is None:
                active_node.right_child = t
                active_node = find_active_node(root)
                if active_node is None or active_node.is_saturated:
                    break
        #below this, the current token (t) is an operator or bracket
        elif active_node.is_leaf:
            #in this case the ACTIVE NODE is a number. operator token needs to be moved up the tree

            pass
        elif not active_node.is_saturated:
            if active_node.left_child is None:
                active_node.left_child = t
                active_node = t
            elif active_node.right_child is None:
                active_node.right_child = t
        else:
            active_node = find_active_node(root)
            if active_node is None or active_node.is_saturated:
                break



def run_calculator():
    equation = ''
    while(True):
        equation = input("Enter an equation:\n")
        if not check_is_balanced(equation):
            print("Parentheses are unbalanced.\nTry again.")
        elif invalid_characters_present(equation) :
            print("Try again.")
        else:
            break
    print(equation)
    tokens = tokenize_input(equation)
    print(tokens)
    build_equation_tree(tokens)


run_calculator()
