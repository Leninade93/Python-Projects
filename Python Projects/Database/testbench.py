import person
import mainID
import subID

def fucntion1():
	#Importing at function scope
	import mainID	
	import random
	import subID
	random.seed(12)
	#Creating a seed so I get the same values for each random

	pNumbers = []

	for name in mainID.first:
		#random.randrange sets cut off points
		#random.randint is inclusive of the arguments
		#random.randchoice() can return string, range, list, or tuple
		choiceList = ['469','972','214']
		phoneNumbers = '{}-{}-{}'.format(
		(random.choice(choiceList)),
		 random.randint(100,999),
		 random.randint(1000,9999))
		pNumbers.append(phoneNumbers)
	print(pNumbers)

def function2():
	import outputGen
	outputGen.option1()

## Pass by Value/Reference/Assignment
def main():
	arg = 4
	arg = square(arg)
	print(arg)

def square(n):
	n *= n
	# without returning the actual value
	# the variable remains unchanged
	return(n)


# String formatting Goals:
# Removing out extraneous characters.
infoTuple = subID.personStorage[0].returnInfo()	
infoString = str(infoTuple)
infoString = infoString.replace('(', '')
infoString = infoString.replace(')', '')
infoString =infoString.replace("'", '')
print(infoString)

def stringFormat(x):
	#use the above logic on passed values

	#return the parsed and new string
	pass