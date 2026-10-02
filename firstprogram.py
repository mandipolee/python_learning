#this is for single line comment ctrl + /
""" This is for multiline comment window shift alt a and for mac shift option a """
#assigning variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
print("My name is " +name + " and I am " + str(age)) # this is concate method
print(f"My name is {name} and age is {age}") # this is f string methond

print("My name is %s and age is %dand address is %s" % (name, age, address)) # this is old format method
 
print("My name is {0} and age is {1}".format(name, age)) #this is new format method




print("hello world")
print("i am learning python" )
