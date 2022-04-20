class Error(Exception):
    pass
class NegativeValue(Error):
    pass
class FloatValue(Error):
    pass

while True:
    print('How many cats do you have?')
    numberCats = input()

    try:
        if float(numberCats)%1 == 0.0:
            if int(numberCats) >= 4:
                print('That is a lot of cats.')
            elif int(numberCats) < 0:
                raise NegativeValue
            else:
                print('That is not a lot of cats')
        else:
            raise FloatValue
    except ValueError:
        print('You did not enter a number.')
    except NegativeValue:
        print('You can\'t have a negative amount of cats silly.')
    except FloatValue:
        print('I\'m not going to ask how you have a fractional amount of cats')