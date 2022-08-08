

# --------------------------------------------------------------------------------------------------------------------------
# Ordered Dictionary
# ---------------------------------------------------------------------------------------------------------------------------

from typing import OrderedDict


od1 = OrderedDict()

od1['one']  = 1

od1['two']  = 2

od2 = OrderedDict()

od2['two']  = 2

od2['one']  = 2

od1 == od2 # False

od3 = OrderedDict(sorted(od1.items(), key = lambda t : (4*t[1]) - t[1]**2))

print(od3.values())

#---------------------------------------------------------------------------------------------------------------------------


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