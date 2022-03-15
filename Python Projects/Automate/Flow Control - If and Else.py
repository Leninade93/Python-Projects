# Only one elif statement will run before the functions breaks out of the if clause. One and only one of the blocks will be executed
def function1():
    name = "tim"
    if name == 'Debug':
        print('Your name is ' + name)
    elif name == 'debug':
        print('Your name is ' + name)
    elif name != False:
        print('You entered a name. The string was: ' + name)
    elif name == False:
        print('Please enter a name')
        name = input()
    else:
        print('This should not execute')

# Here we see two elif statements that conditionals with be satisfied. The first and only the first code block hit will be
# executed and the remaining will be skipped.
def function2():
    name2 = 'bob'
    age = 3000

    if name2 == 'alice':
        print('Hi, Aice')
    elif age < 12:
        print('You are not Alice, Kiddo')
    elif age > 300:
        print('You are not alice, Grannie')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire')
    else:
        print('All previous conditional statements are false')

# Truthy values
def function3():
    name = input()
    if name:
        print('Thank you for entering a name')
    else:
        print('You did not enter a name')

def function4():
    print(bool(0)) # Falsey integer
    print(bool('')) # False
    print(bool(' ')) # True

#function4()
