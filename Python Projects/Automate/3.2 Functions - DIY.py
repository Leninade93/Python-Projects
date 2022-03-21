# arguments are assigned to parameters
# def func(paramater1)
# func(argument1)

# function calls can be called as arguments in functions with appropiate return value
def plusOne(number):
    return number + 1
new_number = plusOne(5)
print(new_number)


# EVERY FUNCTION HAS A RETURN TYPE
# the return type None
# the data type where there is a lack of a value. in the interative shell this
# won't show up. such as when you make a call to the print()
spam = print()
print(spam) # here we the return value of the function print()
print(None)

# Keyword arguments, often used as optional arguments
# changing the print keyword argument end and sep
print('Hello', end = ' ')
print('World')

print('cat', 'dog', 'bear', 'fox', sep = ' ______ ')