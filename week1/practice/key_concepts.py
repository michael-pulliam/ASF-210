# Python offers the following math operator.

# Symbol		Operation			Description
# ----------------------------------------------
# + 			Addition 			Adds two numbers
# _ 			Subtraction 		Subtracts one number from another
# * 			Multiplication 		Multiplies one number by another
# / 			Division 			Divides one number by another and gives the result as a
# 								floating-point number
# // 			Integer division 	Divides one number by another and gives the result as
# 								an integer
# % 			Remainder 			Divides one number by another and gives the remainder
# ** 			Exponent 			Raises a number to a power


# -----------------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------------------
# Input & Output
# --------------------------------------------------------------------------------------------------------------



applesSold = 5000
applePrice = 0.20

print("We sold ",applesSold," apples at $",
format(applePrice,',.2f'),\
" each for a total of $",\
format((applesSold * applePrice),',.2f'),\
sep="")

applesSold = int(input("How many apples did you sell this week? "))
applePrice = float(input("What the price of each apple sold? "))
print("You sold ",applesSold," apples at $",applePrice," each for a total of $",(applesSold * applePrice), sep="")

# ---------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------
# If/Else Statements
# ----------------------------------------------------------------------------------------------------------------

""""
Operator Meaning
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to
"""

def buy2Get1Free(qnty):
	if qnty >= 6:
		print("You qualify for multiple the Buy 2 Get 1 Free Discounts")
	elif (qnty >= 3) and (qnty < 6):
		print("You get one Apple for Free!")
	else:
		print("You do not quality for the discount")


applesSold = 6

buy2Get1Free(applesSold)

# -----------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------
# For Loops
# -----------------------------------------------------------------------------------------------------------------


# EXAMPLE 1

def countDown():

	for currentCount in [5, 4, 3, 2, 1]:
		print(currentCount)
			
	print("BLAST OFF!")
	

countDown()

# ----------------------

# EXAMPLE 2

def welcomeGuests(guestNames):

	for guest in guestNames:
		print("Welcome",guest)
		

guests = []
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))

welcomeGuests(guests)


# ***************************** RANGE *************************************

"""
range(start, stop[, step])

start
The value of the start parameter (or 0 if the parameter was not supplied)

stop
The value of the stop parameter

step
The value of the step parameter (or 1 if the parameter was not supplied)

"""




# EXAMPLE 1

def count(stop):
	for number in range(stop):
		print(number)
		
stoppingNum = int(input("Count to? "))
count(stoppingNum)




# EXAMPLE 2

def countDown(start):

	for currentCount in range(start,0,-1):
		print(currentCount)
			
	print("BLAST OFF!")
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

# -----------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------
# While Loops 
# ------------------------------------------------------------------------------------------------------------------


# EXAMPLE 1

def countDown(start):

	while start > 0:
		print(start)
		start -= 1
			
	print("BLAST OFF!")
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)



# EXAMPLE 2

# *************** BOOLEAN VALUE *****************

def countDown(start):
	continueLoop = True
	while continueLoop:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			continueLoop = False	
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

# EXAMPLE 3

def countDown(start):
	while True:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			break	
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

# ---------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------------------------------------------

"""

A function is a block of code that exist within a program designed to perform a specifc task.

When defining the name of a function, you must follow the same naming rules as those for variables.

There are rules when naming functions / variables and include:
• You cannot use one of Python’s key words as a functions / variable name. 
• A functions / variable name cannot contain spaces.
• The first character must be one of the letters a through z, A through Z, or an underscore character (_).
• After the first character you may use the letters a through z or A through Z, the digits 0 through 9, or underscores.
• Uppercase and lowercase characters are distinct. 

"""

# EXAMPLE 1

def classMessage():
	print("AFS-210", end=" : ")
	print("Data Structures and Algorithms")

print("Welcome to:")
classMessage()
print("I hope you enjoy your next eight weeks of class.")


# EXAMPLE 2


applesSold = 10
applePrice = 0.20

def showAppleTax():
	taxRate = 0.06
	appleTax = (applesSold * applePrice) * taxRate
	print("The tax on the sale of",applesSold,"apples is",appleTax)
	
showAppleTax()	



# EXAMPLE 3


def showSum(a,b):
	print(a+b)
	
x = 1
y = 3
showSum(x,y)	



# EXAMPLE 4


def sum(a,b):
	return a+b
	

y = sum(1,2)
print(y)


# EXAMPLE 5


def add_subtract(a,b):
	return a+b , a-b
	

sum, sub = add_subtract(1,2)
print(sum)
print(sub)	



# -----------------------------------------------------------------------------------------------------------------
# Classes & Methods 
# ------------------------------------------------------------------------------------------------------------------

class dog:

	def __init__(self, name, breed, age, color, size):
		self.name = name
		self.breed = breed
		self.age = age
		self.color = color
		self.size = size
		
	def bark(self):
		print("Woof..Woof")
		
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name
		
	def getAge(self):
		return self.age
		
	def setAge(self,age):
		self.age = age
  
dog1 = dog("Max","German Shepherd",2,"brown","large")
dog2 = dog("Cooper","Labrador",4,"black","large")
dog3 = dog("Bella","Chihuahua",1,"tan","small")

print(dog1.getName())
print(dog1.bark())
print(dog1.setAge(3))
print(dog1.getAge())


# -----------------------------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------------
# List 
# -----------------------------------------------------------------------------------------------------------------




progLang = ["python", "c#", "javascript", "java", "c++"]
moreLang = ["rust", "php", "perl", "ruby", "go"]

myNumbers = [1,2,3,4,5]
myFloats = [1.0, 2.1, 3.2, 4.3]

myMixed = ["Hello", True, 6, ["item1","item2","item3"], 3.14]

print(progLang)

progLang.append("c")
print(progLang)

progLang.extend(moreLang)
print(progLang)

progLang.insert(1, "pascal")
print(progLang)

progLang.remove("pascal")
print(progLang)

progLang.pop()
print(progLang)

progLang.pop(6)
print(progLang)

print(progLang.index("php"))
progLang.append("php")
print(progLang)
print(progLang.count("php"))
progLang.sort(reverse=True)
print(progLang)

print(myMixed[3][2])

# ---------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------
# Tuple
# -----------------------------------------------------------------------------------------------------------------


#Tuple items are ordered, unchangeable, and allow duplicate values.

#Tuple items are indexed with the first item having an index of [0], the second item has an index of [1] etc.

#The Tuple is unmutable (ie: unchangeable), meaning that we can not change, add, and remove items in a tuple after it has been created.

#A Tuple may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects

#Tuples are created by placing a sequence of values separated by a comma inside round brackets ()


progLang = ("python", "c#", "javascript", "java", "c++", "python")

myNumbers = (1,2,3,4,5)
myFloats = (1.0, 2.1, 3.2, 4.3)

myMixed = ("Hello", True, 6, ["item1","item2","item3"], 3.14)

print(progLang.count("python"))
print(progLang.index('javascript'))

print(len(progLang))

print(myMixed)
myMixed[3][0] = "A"
print(myMixed)


# ----------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------------
# Set
# -----------------------------------------------------------------------------------------------------------------------------


#In a Set, items are unordered, unindexed and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.

#This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

#Sets cannot have two items with the same value.

#A Set is created by placing a sequence of values separted by a comma inside curly brackets {}


progLang = {"python", "c#", "javascript", "java", "c++"}
moreLang = {"rust", "php", "perl", "ruby", "go", "java", "python"}

myNumbers = {1,2,3,4,5}

myFloats = {1.0, 2.1, 3.2, 4.3}

progLang.add("HTML") # No Duplicate Error (does not allow duplicate values)
print(progLang)

removedItem = progLang.pop() # Removes Random
print(progLang)
print(removedItem)

progLang.discard("c#")
print(progLang)

# progLang.remove("c#") # Throw Error if Item is not in the Set
print(progLang)

print(progLang.difference(moreLang)) # Values not shared
print(progLang)

print(progLang.intersection(moreLang)) # Values shared


# --------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------
# Dictionary
# ---------------------------------------------------------------------------------------------------------------------------


#Dictionaries are used to store data in key:value pairs where the keys must be unique.

#A dictionary is a collection which is ordered, as of Python version 3.7, changeable (mutable) and does not allow duplicate key values.

#Storing a value using a key that is already in use, results in the old value being replaced with the new value.

#A Dictionary is created by placing a sequence of keys:values pairs, separted by a comma, inside curly brackets {}

#If you are familiar with Javascript, the notation of key:value pairs should be familiar to you as they are similar to JSON data format.



worldCapitals = {
	"Afghanistan" : "Kabul",
	"Bangladesh" : "Dhaka",
	"Canada" : "Ottawa",
	"Cuba" : "Havana",
	"France" : "Paris",
	"Germany" : "Berlin",
	"Philippines" : "Manila",
	"United Kingdom" : "London",
	"United States" : "Washington D.C."
}

print(worldCapitals.get("France")) # Builded in get method using the KEY of the key value pair

print(worldCapitals.values()) # Get all values inside Dictionary

print(worldCapitals.keys()) # Get all keys inside Dictionary

keys = worldCapitals.keys()

for key in keys:
    print('"%s" : "%s"' % (key, worldCapitals.get(key)),end=",")
    
print(worldCapitals.items()) # Return view object tuple of the key: value pairs 

for country, capital in worldCapitals.items():
	print(country + " = " + capital)
 
worldCapitals.pop("Germany") # Remove key value pair from Dictionary (call key)
print(worldCapitals)


worldCapitals.update({"United States" : "New York"}) # Change key: value pair /or add new key: value pair
print(worldCapitals)

print(worldCapitals.get("Canada")) # gets key: value pair

print(worldCapitals.setdefault("Canada")) # combination of .get() and .update()