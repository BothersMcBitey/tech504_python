def print_something():
    print("something")

def print_string(string):
    print(string)

def greet(name):
    print(f"Hello, my name is {name}.")

greet("Susan")

def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))

def addition_but_better(int1=2, int2=2):
    return int1 + int2

print(addition_but_better(4, 4))

def print_every_number(*args):
    print(type(args))
    for i in args: print(i)

print_every_number(1,2,2,3,3,4,5,5)

def greeting(a:str):
    print(a)

greeting(24601)

def division(x:int=2, y:int=5)->float:
    return x / y

a:int = 4
b:int = 6
print(division(a,b))

