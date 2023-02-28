#String Data Type
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

#Concatenation
firstString = "water"
secondString = "Fall"
thirdString = firstString + secondString
print(thirdString)

#input() function
name = input("What is your name? ")
print(name)

#Formatting output
colour = input("What is your favorite colour? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,colour,animal))