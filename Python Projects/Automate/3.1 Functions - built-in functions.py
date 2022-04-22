# print(), input(), len(), range() have all been covered.
# additional built-in funcs come from importing modules from the standard library
import random, math, sys, os
print(random.randint(1, 100))

# alternative import statement. Now we won't have to call the random module to use randint
from random import *
print(randint(0, 100))

# terminate a program early
#sys.exit()

# following statement will never execute
print('Goodbye')

# third party modules can be installed through PIP. let's install pyperclip
import pyperclip
pyperclip.copy('hello world')
# print function would not have to be used if running through idle to output the string above
print(pyperclip.paste())
