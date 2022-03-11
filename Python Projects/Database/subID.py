import random
import mainID
import person

# Need to actually instantiate all of the data into the Person class.
# So we have a list to store the objects
# and we have a count variable to move through said lists.
personStorage = []
count = 0
for count in range(0,(len(mainID.first))):
	x = person.Person(count)
	count = count + 1
	personStorage.append(x)

###########################################################################

# Going to have to have hard-code in the employees for the most part.
# Will make the first 7 people employees. The rest of the list can
# be customers. 
employeeStorage = []
e0 = person.Employee(0,'000','12/3/2015','Chief Executive Officer')
employeeStorage.append(e0)

e1 = person.Employee(1,'001','12/3/2015','Chief Financial Officer')
employeeStorage.append(e1)

e2 = person.Employee(2,'002','12/8/2015','Chief Accountant')
employeeStorage.append(e2)

e3 = person.Employee(3,'003','1/16/2016','Sales Associate')
employeeStorage.append(e3)

e4 = person.Employee(4,'004','2/21/2016','Sales Associate')
employeeStorage.append(e4)

e5 = person.Employee(5,'005','4/30/2016','Accounts Receivable/Payable')
employeeStorage.append(e5)

e6 = person.Employee(6,'006','7/6/2016','Clerk')
employeeStorage.append(e6)

#############################################################################

# Customer Creation List for the final 13 identities with their unique
# attributes.
rewardsStatus 	= ['True','False']
custID 			= int(0o000)
#Now have a list of Objects Customers
customerStorage = []

for count in range(7,len(mainID.first)):
	x = person.Customer(count, custID, random.choice(rewardsStatus))
	customerStorage.append(x)
	count 	= count + 1
	custID 	= custID + 1

#Can operate on that list with member functions.
#for x in range(0,len(customerStorage)):
#	customerStorage[x].getInfo()
#	x = x + 1
###############################################################################

testReturn = e6.returnInfo()
print(testReturn)