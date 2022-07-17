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



# applesSold = 5000
# applePrice = 0.20

# print("We sold ",applesSold," apples at $",
# format(applePrice,',.2f'),\
# " each for a total of $",\
# format((applesSold * applePrice),',.2f'),\
# sep="")

# applesSold = int(input("How many apples did you sell this week? "))
# applePrice = float(input("What the price of each apple sold? "))
# print("You sold ",applesSold," apples at $",applePrice," each for a total of $",(applesSold * applePrice), sep="")

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

# def buy2Get1Free(qnty):
# 	if qnty >= 6:
# 		print("You qualify for multiple the Buy 2 Get 1 Free Discounts")
# 	elif (qnty >= 3) and (qnty < 6):
# 		print("You get one Apple for Free!")
# 	else:
# 		print("You do not quality for the discount")


# applesSold = 6

# buy2Get1Free(applesSold)

# -----------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------
# For Loops
# -----------------------------------------------------------------------------------------------------------------


# EXAMPLE 1

# def countDown():

# 	for currentCount in [5, 4, 3, 2, 1]:
# 		print(currentCount)
			
# 	print("BLAST OFF!")
	

# countDown()

# ----------------------

# EXAMPLE 2

# def welcomeGuests(guestNames):

# 	for guest in guestNames:
# 		print("Welcome",guest)
		

# guests = []
# guests.append(input("Please enter the name of a guest: "))
# guests.append(input("Please enter the name of a guest: "))
# guests.append(input("Please enter the name of a guest: "))

# welcomeGuests(guests)


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

# def count(stop):
# 	for number in range(stop):
# 		print(number)
		
# stoppingNum = int(input("Count to? "))
# count(stoppingNum)




# EXAMPLE 2

# def countDown(start):

# 	for currentCount in range(start,0,-1):
# 		print(currentCount)
			
# 	print("BLAST OFF!")
	

# startingNum = int(input("Enter the countdown starting number: "))
# countDown(startingNum)

# -----------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------
# While Loops 
# ------------------------------------------------------------------------------------------------------------------


# EXAMPLE 1

# def countDown(start):

# 	while start > 0:
# 		print(start)
# 		start -= 1
			
# 	print("BLAST OFF!")
	

# startingNum = int(input("Enter the countdown starting number: "))
# countDown(startingNum)



# EXAMPLE 2

# *************** BOOLEAN VALUE *****************

# def countDown(start):
# 	continueLoop = True
# 	while continueLoop:
# 		print(start)
# 		start -= 1
# 		if (start == 0):
# 			print("BLAST OFF!")
# 			continueLoop = False	
	

# startingNum = int(input("Enter the countdown starting number: "))
# countDown(startingNum)

# EXAMPLE 3

# def countDown(start):
# 	while True:
# 		print(start)
# 		start -= 1
# 		if (start == 0):
# 			print("BLAST OFF!")
# 			break	
	

# startingNum = int(input("Enter the countdown starting number: "))
# countDown(startingNum)

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

# def classMessage():
# 	print("AFS-210", end=" : ")
# 	print("Data Structures and Algorithms")

# print("Welcome to:")
# classMessage()
# print("I hope you enjoy your next eight weeks of class.")


# EXAMPLE 2


# applesSold = 10
# applePrice = 0.20

# def showAppleTax():
# 	taxRate = 0.06
# 	appleTax = (applesSold * applePrice) * taxRate
# 	print("The tax on the sale of",applesSold,"apples is",appleTax)
	
# showAppleTax()	



# EXAMPLE 3


# def showSum(a,b):
# 	print(a+b)
	
# x = 1
# y = 3
# showSum(x,y)	



# EXAMPLE 4


# def sum(a,b):
# 	return a+b
	

# y = sum(1,2)
# print(y)


# EXAMPLE 5


# def add_subtract(a,b):
# 	return a+b , a-b
	

# sum, sub = add_subtract(1,2)
# print(sum)
# print(sub)	



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