def concatenate_string(*args):
    string1 = args[0]
    string2 = args[1]
  
    return string1 + string2
  
obj = concatenate_string('Hello, ', 'George')
print('Function call with Parentheses: ')
print(obj)
  
obj = concatenate_string
print('Function call without Parentheses: ')
print(obj)
