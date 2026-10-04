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




#operators
 #arithmetic operators
print(5 + 3) #addition answer is 8
print(5 - 3) #subtraction answer is 2
print(5 * 3) #multiplication answer is 15

print(5 / 3) #division, it retuuns float value answer is 1.666666666666666 
print(5 // 3) #floor division, it returns integer value answer is 1
print(-5 // 3) #floor division, it returns integer value answer is -2

print(5 % 3) #modulus, it returns remainder answer is 2
print(10 % 2) # answer is 0

print(5 ** 3) #exponentiation, it returns power answer is 125
print(5 ** 0.5) # exponentiation, it returns square root answer is 2.23606797749979
print(5 ** (1/3)) # exponentiation, it returns cube root answer is 1.7099759466766968




#relational operators
print(10==10) #equal to, answer is True
print(10!=10) #not equal to, answer is False
print(10!=5) #not equal to, answer is True
print(10>5) #greater than, answer is True
print(10<5) #less than, answer is False

print(10>=10) #greater than or equal to, answer is True
print(10<=10) #less than or equal to, answer is True

#chaining of relational operators
x=10
print(5<x<15) # answer is True
print(5<=x<=15) # answer is True
print(10<x<15) # answer is False

#string comparison
print("python"=="python") # unicode is same,answer is True
print("apple">"banana") # unicode of apple is less than banana, answer is False

#boolen comparison
print(1==True) # answer is True
print(0==False) # answer is True
print(1=="1") # answer is False, because int and string are different data types

#Assignment operators
score = 50 
score += 10 # score = score + 10, answer is 60
score -= 10 # score = score - 10, answer is 50
score *= 2 # score = score * 2, answer is 100
score /= 2 # score = score / 2, answer is 50.0
print(score) # answer is 50.0


#multiple assignmnet- assigning multiple values to multiple variables in a single line
a, b, c = 10  
print(a,b,c) # answer is 10

a, b, c = 10, 20, 30
print(a,b,c) # answer is 10 20 30

#swapping of two numbers
x = 10
y = 20
x, y = y, x #swapping of two numbers
print(x,y) # answer is 20 10

#logical operators
#and operator- both conditions should be satisfied
age = 25
id = True
print(age>18 and id==True) # answer is True both conditions satisfied

#or atleat one condition should be satisfied
is_student = True
is_teacher = False
print(is_student or is_teacher) # answer is True, one condition satisfied

#not operator- it reverses the boolean value
print(not True) # answer is False
print(not False) # answer is True

# Short-circuit with 'and' — right side skipped if left is False
print(False and 1/0) #output false
print(True or 1/0) #output true


# Combining logical operators with comparison operator
marks = 72
print(marks >= 40 and marks <= 100) # → True (valid score range)
print(marks < 40 or marks > 100) # → False (not out of range)




#bitwise operators
print(bin(5)) # output is 0b101, binary representation of 5
print(5 & 3) # bitwise AND, output is 1 (0b001)
print(5 | 3) # bitwise OR, output is 7 (0b111)
print(5 ^ 3) # bitwise XOR, output is 6 (0b110)
print(~5) # bitwise NOT, output is -6 (inverts bits)
print(5 << 1) # left shift, output is 10 (0b1010)
print(5 >> 1) # right shift, output is 2 (0b10)     


#membership operators
print('py' in 'python') # output is True, 'py' is a substring of 'python'
print('java' not in 'python') # output is True, 'java' is not
print('java' in 'python') # output is False, 'java' is not a substring of 'python'

#identity operators
x = [1, 2, 3]
y = [1, 2, 3]  
z = x     
print(x is y) # output is False, x and y are different objects
print(x is not y) # output is True, x and y are different objects
print(x is z) # output is True, x and z refer to the same object




#precedence of operators
# * before + (same as BODMAS)
print(2 + 3 * 4) # → 14 (* before +)
print((2 + 3) * 4) # → 20 (parentheses first)
# ** is right to left
print(2 ** 3 ** 2) # → 512 (2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2) # → 64 (different result with brackets!)
# Comparison before logical operators
print(5 > 3 and 2 < 4) # → True (comparisons first, then and)
print(not True or True) # → True (not binds tighter than or)
# When unsure — always use parentheses for clarity
result = (5 + 3) * (10 - 4)
print(result) # → 48 (clear and unambiguous)



