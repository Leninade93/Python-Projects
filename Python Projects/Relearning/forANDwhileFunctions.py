import sys
#Global variables
names = ['Tom', 'Nick', 'Igor', 'Johnny', 'Betty', 'Elizabeth']
a = 0

def funct1():
	#Using global we can prevent the function from trying to create a
	#local scope version of a
	global a 
	# Don't forget to seperate print statements with commas
	while a < 5	
		print(names[a], "with a length of: ", len(names[a]))
		a = a+1
		#ctrl + c will break loop

def funct2():
	global names
	#global a
	#For loops go through lists or strings and can't really how long to iterate.
	#Don't need a variable to iterate through. Can just use the string or list declared. 
	for currName in names:
		print(currName, "with a length of : ", len(currName))

#If the user seeks to rerun the program
def repeatProgram():
	prompt2 = input("Would you like to run the program again? (yes/no):")
	if prompt2 == "yes":
		print("\n")
		userInput()
	elif prompt2 == "no":
		print("Program exiting.")
	else:
		print("Invalid input.\n")
		repeatProgram()

#input allows console command.
def userInput():
	prompt = (input("Please choose which function to execute '1' or '2':"))
	if prompt == '1':
		funct1()
		repeatProgram()
	elif prompt == '2':
		funct2()
		repeatProgram()
	else:
		print("Incorrect value entered please re-run the program.\n")
		userInput()
userInput()

