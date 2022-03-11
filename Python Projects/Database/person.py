import mainID

## Basic class with some inheritance and overrided methods

class Person:
	# Attributes
	fName = " "
	lName = " " 
	phoneNumb = " "
	bDate = " " 
	address = ' '
	email = ' '

	# Methods
	def __init__(self, a):
		self.fName = mainID.first[a]
		self.lName = mainID.last[a]
		self.phoneNumb = mainID.pNumbers[a]
		self.bDate = mainID.bDates[a]
		self.address = mainID.addressList[a]
		self.email = mainID.emailList[a]

	def getInfo(self):
		print("First Name:   		" + self.fName)
		print("Last Name:   		" + self.lName)
		print("Phone Number:   	" + self.phoneNumb)
		print("Birth Date:   		" + self.bDate)
		print("Address:   			" + self.address)
		print("Email:   			" + self.email)

	def returnInfo(self):
		return(self.fName,self.lName,self.phoneNumb,self.bDate,self.address,self.email)
		
################################################################
class Employee(Person):
	#Unique attributes
	eID = ''
	hiringDate = ''
	jobTitle = ''

	def __init__(self, a, eID, hiringDate, jobTitle):
		Person.__init__(self, a)
		self.eID = eID
		self.hiringDate = hiringDate
		self.jobTitle = jobTitle

	def getInfo(self):
		Person.getInfo(self)
		print("Employee ID:  		" + self.eID)
		print("Date Hired:   		" + self.hiringDate)
		print("Job Title:    		" + self.jobTitle)

	def returnInfo(self):
		return(Person.returnInfo(self), self.eID, self.hiringDate, self.jobTitle)

################################################################	
class Customer(Person):
	#Unique attributes
	cID = int
	#Boolean if they're a rewards member
	rewMem = bool

	def __init__(self, a, cID, rewards):
		Person.__init__(self, a)
		self.cID = cID
		self.rewMem = rewards

	def getInfo(self):
		Person.getInfo(self)
		print('{}{}'.format("Customer ID:	",self.cID))
		print("Rewards Status:	"   + self.rewMem)

	def returnInfo(self):
		return(Person.returnInfo(self), self.cID, self.rewMem)
		
###############################################################
