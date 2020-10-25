"""
# if statement
 x = 20
if x < 20:
    print(" X is less than 20")
elif x == 20:
    print(" X is equal to 20")    
else:
    printe("X is greater than 20")    
"""

'''
name = "John"
age = 20
new_patient = True
print (name, age, new_patient)
'''

'''
name = input("what is your name: ")
color = input("what colour do you like: ")
print(name + " likes " + color)
'''

'''
birth_year = input("Enter your birth year: ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(age)
'''

'''
weight = input("Enter your weight: ")
weight_kg = int(weight)/4.5
print(weight_kg)
# print("Your weight is " + int(weight)//4.5 + "Kilos")
'''

# formated string
'''
fname = "John"
lname = "Smith"
msg = f'{fname} [{lname}] is a coder'
print(msg)
'''

# string functions
course = "Python for Begineers"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('o'))
# print(course.replace('Begineers', 'advanced begineers'))
# print('Python' in course) # will return a tru or false

# Arithematic operators
# + - * / // (will roud off),  % modulus, ** (exponent)

# Maths function
# x = -2.9
# print(round(x))
# print(abs(x)) # always returns a positive number
# import maths module for advanced math functions using
# imports math at the start of the file
# math.ceil(2.9) # google search " python 3 math module"

# if statement

''''
price = 1000000
cs = True

if cs:
    dp = price * 0.1
else:
    dp = price * 0.2

print(f"Down payment = ${dp}")
'''

'''
ls = list(range(1, 8))
print(ls)
'''

ad3 = 0
ad5 = 0

for x in range(1, 100):
    if x % 3 == 0:
        ad3 += x
        continue
    elif x % 5 == 0:
        ad5 += x

print(ad3)
print(ad5)