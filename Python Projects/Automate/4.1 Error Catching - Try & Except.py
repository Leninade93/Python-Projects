def divide42by(num):
    # When code in the try clause causes a ZeroDivisionError
    # code execution moves to the except clause
    # a simple unspecified exception clause will catch all types of errors
    try:
        return 42/num
    except ZeroDivisionError:
        print('Error you tried to divide by zero!')


print(divide42by(2))
print(divide42by(3.5))
print(divide42by(0))
print(divide42by(1))