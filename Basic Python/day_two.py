## What is a variable?
# It's a named piece of data that can change in value

## Why is it called a variable?
# It can change value (it varies).

num = 5
dec = 4.5
word = "concrete"

## How is using '==' different?
# == is a comparator

print(str(num) + ", " + str(dec) + ", " + word)

### What does it mean that Python is...
## A strongly typed language? Compare to a weakly typed language. Include a code example
# Strongly typed languages aren't well-defined (ironically). Generally, in a
# weakly typed language variables of different types can stand in for each other,
# while in strongly typed languages the can't.
#   e.g. in a strong language "3" == 3 returns false (or an error)
#   in a weak language "3" == 3 might return true

## A dynamically typed language? Compare to a statically typed language.
# In a dynamically typed language variable type is checked and controlled at runtime,
# allowing for variables to change type. In a statically typed language types
# are checked at compile time and are fixed.
#    e.g. in python (dynamic typing) a = 10; a = "cheese" is totally fine, but
#    in a static language this would be an error

## Overwrite the value of one of your variables which stores a number
## Why does the 'id' of the variable change?
# some values are treated as immutable in python, and have specific preset IDs,
# this includes integers
a = 999998
print(id(a))
a = 999999
print(id(a))
a = 999998
print(id(a))

# Assign one variable to another
x = 10
y = x
print(id(x))
print(id(y))
## Explain why the id of x and y are the same
# y and x are both 10, so they have the same ID
## What happens if after assigning x = y, I give x a different value? Does the id of y change also?
# No. Y takes the value (10) of x, but is not a reference to x.

## Ask the user for some input and print the input to the screen, etc
print("hi")
name = input("gimme yer name: ")
age = input("gimme yer age: ")
dob = input("gimme yer DoB: ")

## What is the difference between an operator and operand?
# an operator is a function that does something with data, an operand is
# something that holds data. e.g. '=' and '<=' are operators, "x" and "7" are
# operands. get_rotation(some_object) can be an operator and an operand
x = 5
y = 1

print(x + y)
print(x - y)
print(x * y)
print(y / x)
print(x % 2)
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

# bad_string = 'I said 'Wow!''
# print(bad_string)
## Why does this fail?
# ' ' denotes a string literal. The second ' is seen as the end of the string,
# and the rest of the line is evaluated as an expression, which doesn't work

print("I said 'Wow!'")
print('I said "Wow!"')
print('I said \'Wow!\'')

## What is best practice when deciding what quotes to use around strings in Python?
# Ultimately consistency is all that matters, but to stay in line with other
# languages I usually use " for strings and ' for single characters

## What is slicing strings?
# Slicing strings is a way of extracting chunks of a string with array indexing

hw = "Hello world!"
print(hw)
## Find out how many characters Hw has
print(len(hw)) # strings are a kind of array pm
## Get the character in the first position in Hw
print(hw[0])
## Get the last character
print(hw[-1])
## Get the 2nd last character
print(hw[-2])
## Write a comment to EXPLAIN what does this do
print(hw[2:]) # skips the first 2 elements in the string
## Write a comment to EXPLAIN what does this do
print(hw[-3:]) # gets the last 3 elements of the string
## Write a comment to EXPLAIN what does this do
print(hw[:5]) # gets the first 5 elements of the strong
## Starts from the second, stops at the fifth (doesn't include it)
print(hw[1:4])


str_with_extra_spaces = " extra spaces at the start and end "
# Write comment to explain what this does
#print(len(str_with_extra_spaces))
## this returns the length of the string, which is 35
# Write comment to explain what this does
## this removes leading and trailing whitespace
print(len(str_with_extra_spaces.strip()))

example_text = "here's some text with some words of text"
# count how many times the substring 'text' occurs within example_text & print
# it to the screen
print(example_text.count("text"))
# convert example_text to lowercase & print it to the screen
print(example_text.lower())
# convert example_text to uppercase & print it to the screen
print(example_text.upper())
# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())
# replace the word 'with' in example_text with a comma (,) instead & print it to
# the screen
print(example_text.replace("with", ","))


x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print( str(x) + str(y) + z)
## The problem is that the + operator attempts numerical addition when the
## operands are numbers, but concatenation when they are strings. Non-string
## values are also not implicitly cast by '+'. To concatenate all values as
## strings you need to explicitly cast x and y to strings

int_string = "6"
# convert int_string to an integer
print(int(int_string))
# after converting, print its data type to the screen
print(type(int(int_string)))
# convert int_string to float
print(float(int_string))
# after converting, print its data type to the screen
print(type(float(int_string)))


name = "Lassie"
years = 7
height_cm = 60.2
# print these variables in an f-string so that it outputs this to the screen:
# "Lassie is 7 years old and 60.2 cm tall."
print(f"{name} is {years} years old and {height_cm} cm tall.")


pi = 3.14159265359
# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.4}")
# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 5 decimal places: {pi:.6}")
score = 16
max_score = 26
score_as_decimal = score/max_score
# Use an f-string to print 'score_as_decimal' e.g. 'You scored
# 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g.
# 'You scored 61.538462%'
print(f"You scored {score_as_decimal:.6%}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded
# to 2 decimal places e.g. 'You scored 61.54%'
print(f"You scored {score_as_decimal:.2%}")
# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded
# to a whole number e.g. 'You scored 62%'
print(f"You scored {score_as_decimal:.0%}")