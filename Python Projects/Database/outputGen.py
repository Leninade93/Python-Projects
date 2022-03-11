#Generate Output
import subID

# String formating : removing extraneous characters
def stringFormating(x):
	formatedString = x
	formatedString = formatedString.replace('(', '')
	formatedString = formatedString.replace(')', '')
	formatedString =formatedString.replace("'", '')
	return(formatedString)
	

#Experimenting with outputting information to generic text files.
def getPersons():
	# Text File
	f = open('Persons.txt', 'w')
	f.write("Persons list ->" + '\n')
	f.write('PID, ' + 'First Name, ' + 'Last Name, ' + 'Phone Number, ' + 'Birthday, '+ 
			'Address, ' + 'Email, ' + '\n')
	for count in range(0,(len(subID.personStorage))):
			# Type casting int to str
			f.write(str(count) + ': ')
			personString = str(subID.personStorage[count].returnInfo())
			personString = stringFormating(personString)
			f.write(personString + '\n')
			count = count + 1
	f.close()

	# CSV File
	f = open('Persons.csv', 'w')
	f.write("Persons list ->" + '\n')
	f.write('PID,' + 'First Name, ' + 'Last Name,' + 'Phone Number,' + 'Birthday,'+ 
			'Address,' + 'Email,')
	f.write( '\n')
	for count in range(0,(len(subID.personStorage))):
			f.write(str(count)+ ',')
			personString = str(subID.personStorage[count].returnInfo())
			personString = stringFormating(personString)
			f.write(personString + '\n')
			count = count + 1
	f.close()
###############################################################

def getEmployees():
	f = open('Employees.txt', 'w')
	f.write("Employee list ->" + '\n')
	f.write('EID, ' + 'First Name, ' + 'Last Name, ' + 'Phone Number, ' + 'Birthday, '+ 
			'Address, ' + 'Email, ' + 'Employee ID, ' + 'Hiring Date, ' + 'Job Title ' + '\n')
	for count in range(0,(len(subID.employeeStorage))):
			f.write(str(count) + ': ')
			employeeString = str(subID.employeeStorage[count].returnInfo())
			employeeString = stringFormating(employeeString)
			f.write(employeeString + '\n')
			count = count + 1
	f.close()

	f = open('Employee.csv', 'w')
	f.write('Employee Lists:')
	f.write('\n')
	f.write('EID, ' + 'First Name, ' + 'Last Name, ' + 'Phone Number, ' + 'Birthday, '+ 
			'Address, ' + 'Email, ' + 'Employee ID, ' + 'Hiring Date, ' + 'Job Title ' + '\n')
	for count in range(0,(len(subID.employeeStorage))):
			f.write(str(count)+ ',')
			employeeString = str(subID.employeeStorage[count].returnInfo())
			employeeString = stringFormating(employeeString)
			f.write(employeeString + '\n')
			count = count + 1
	f.close()

###############################################################

def getCustomers():
	f = open('Customers.txt', 'w')
	f.write("Customers list ->" + '\n')
	f.write('CID, ' + 'First Name, ' + 'Last Name, ' + 'Phone Number, ' + 'Birthday, '+ 
			'Address, ' + 'Email, ' + 'Customer ID, ' + 'Rewards Membership, ' + '\n')
	for count in range(0,(len(subID.customerStorage))):
			f.write(str(count) + ': ')
			customerString = str(subID.customerStorage[count].returnInfo())
			customerString = stringFormating(customerString)
			f.write(customerString + '\n')
			count = count + 1
	f.close()

	f = open('Customers.csv', 'w')
	f.write('Customers Lists:')
	f.write('\n')
	f.write('CID, ' + 'First Name, ' + 'Last Name, ' + 'Phone Number, ' + 'Birthday, '+ 
			'Address, ' + 'Email, ' + 'Customer ID, ' + 'Rewards Membership, ' + '\n')
	for count in range(0,(len(subID.customerStorage))):
			f.write(str(count)+ ',')
			customerString = str(subID.customerStorage[count].returnInfo())
			customerString = stringFormating(customerString)
			f.write(customerString + '\n')
			count = count + 1
	f.close()
	
###############################################################
getPersons()
getEmployees()
getCustomers()