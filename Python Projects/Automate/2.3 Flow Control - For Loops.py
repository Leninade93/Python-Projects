# For loops will iterate a specific number of times
print('My name is')
for i in range(5):
    print('Jimmy 5 times ' + str(i))
    # notice here that i autoiterates, you don't need to do i = i + 1. also that i starts automatically at zero
print('')

# find the sum of 0-100
total = 0
for num in range(101):
    total = total + num
print(total)
print('')
i = 0
while i < 5:
    print('Jimmy 5 times ' + str(i))
    i = i + 1
print('')


# range data type
for i in range(5,16):
    print('Jimmy X times ' + str(i))
    # notice here that i autoiterates, you don't need to do i = i + 1. also that i starts automatically at zero
print('')

#range agruments (start, stop, step)
for i in range(10,200, 3):
    print('Jimmy X times ' + str(i))
    # notice here that i autoiterates, you don't need to do i = i + 1. also that i starts automatically at zero
print('')

#break and continue statements will still work in for loops
for num in range(0, 1000, 1):
    if num == 507:
        print(str(num) + ' : the magic number has been achieved. Please continue.')
        #continue
        break
    elif num == 999:
        print('We have reached the end of our loop at : ' + str(num))