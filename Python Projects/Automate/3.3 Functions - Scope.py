# in python variables inside and outside of a function can have the same name as outside
# Global scope = any given line of your source code outside of a function block
# Local scope  = variable defined in the function block
eggs = 0 
test = 42 # global scope
def funct1():
    test = 41 # local scope because there is an assignment function

# global scope are destroyed when the function terminates
# local scope are destryoed when a function is returned, thus these are 'temporaray' in your code

# 1 Code in global scope CAN NOT access local variables
# 2 Code in local scope CAN access global variables
# 3 one functions local scope cannot used variables in a local scope
# 4 you can use the same name in a variable in different scopes


# https://pythontutor.com/visualize.html#mode=edit
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    print(spam) # reference in memory to definition?
    print(test) # will print the gliobal 42 from above
spam()

# say you want to change the value of a global variable within the local scope of a function
# use the global statement
print('The original value of GLOBAL eggs is: ' + str(eggs))
def global_key():
    global eggs
    eggs = 'hello'
global_key()
print('The new value of the GLOBAL eggs is:  ' + eggs)

# The benefits of scope
# Scope let's more easily determine where a variable in your code might be going wrong for debugging



