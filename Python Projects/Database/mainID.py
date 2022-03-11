#identity generation
import random
#Creating a seed so I get the same values for each random
random.seed(12)
#For creating birth dates

#Create a list of first names
first = ['Drake', 'Alice','Ariana','Nash','Tamara','Randall','Mitchell','Zion','Joslyn','Carl'
		,'Savanna','Gordon','Simon','Madeline','Dereon','Raegan','Lola','Whitney','Erik','Jaylen']
#Create a list of last names
last  = ['Oneal','Gilmore','Reynolds','Fletcher','Weber','Mcgee','Hansen','Clayton','Santiago'
		,'Dodson','Shepherd','Archer','Sweeney','Haley','Rich','Gonzales','Montes','Dyer','Newman','Ball' ]

#Create a phone number for each person of str data type
pNumbers = []
for name in first:
	#random.randrange sets cut off points
	#random.randint is inclusive of the arguments
	#random.randchoice() can return string, range, list, or tuple
	choiceList = ['469','972','214']
	phoneNumbers = '{}-{}-{}'.format((random.choice(choiceList)), random.randint(100,999), random.randint(1000,9999))
	pNumbers.append(phoneNumbers)

#Create birthdates for all these people of str datatype
bDates = []
for names in first:
	DOB = (str(random.randint(1,12))) + '/' + (str(random.randint(1,30))) + '/' + (str(random.randint(1965,2000)))
	bDates.append(DOB)	

#Want to add an address list
#houseNumber int, then streetName, then cityName from a small choice with a tied zipcode
houseList = []
for names in first:	
	x = random.randint(1000,9999)
	houseList.append(x)
	
streetName = [  'Main Street', 'Ocean Avenue', 'Rodeo Drive', 'Fifth Avenue', 'Maretplace Way'
				  , 'Abbey Road', 'Third Street', 'Maple Road', 'Crossburn Road', 'Elm Avenue'
				  , 'Lakewood Street', 'Washing Avenue', 'Luther\'s Route', 'Electric Avenue', 'Sabbath Road'
				  , 'Guston Road', 'Dirt Road', 'Farmer\'s Way', 'Taming Road', 'Clifford Street']
	
cityName = ['Dallas ', 'Garland ', 'Mesquite ', 'Richardson ', 'Irving ', 'Plano ', 'Arlington ']
	
zipCode = [75201, 75040, 75150, 75080, 75014, 75023, 76001]

#Link because i'm lazy
cityZip = []
i = 0 
for i in range(0,(len(cityName))):
	x = cityName[i] + str(zipCode[i])
	cityZip.append(x)

#Combined into final address
addressList = []
i = 0
for i in range(0,len(first)):
	x = (streetName[i]  +'' " Texas "  +  random.choice(cityZip))
	addressList.append(x)


#Want to add an email list
emailList = []
i = 0
for i in range(0,len(first)):
	x = first[i] + "_" + last[i] + "@mail.com"
	emailList.append(x)