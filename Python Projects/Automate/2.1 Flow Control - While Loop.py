# In a simple series of if/elif/else statement after a satisfied conditional code block is executed
# the control of the program will exit out of the clause

# Flow control for code execution in a while loop will remain in the loop
# after interating through the loop each time until the conditional value 
# is not satisfied.
# Basic interating while loop
def example_1():
    spam = 0

    while spam < 5:
        print('Hello world')
        spam = spam + 1

def example__2():
    name = ''
    while name != 'your name':
        print('Please enter your name')
        name = input()
    print('Thank you!')

# Infinite Loops can be pesky
def infinite_loop():
    while True:
        print('hello')
#infinite_loop()

# Break Statements
# Here we're actually utilized a infinite loop and a break statement to avoid
# getting locked
def revised_example_2():
    name = ''
    while True:
        print('Please enter your name: ')
        name = input()
        if name == 'your name':
            break
    print('Thank you!')

# Continue statements will cause the while loop to return to the beginning of execution
def while_continue():
    spam = 0

    while spam < 5:
        spam = spam + 1
        if spam == 3:
            print('CONTINUE CLAUSE EXECUTING HERE')
            continue
            # in this we see the program skips the next print statement and returns to interating
            # spam increase from 3 to 4. If we had used a break statement our output would have simply ended
        print('Spam is ' + str(spam))       
    print('Exiting loop')
while_continue()