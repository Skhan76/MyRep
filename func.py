# functions

'''
def fun1():
    print("Hello mama!!!")


print("Hello!!!")
fun1()
'''
# Function with parameters
'''
def fun2(x, y):
    print(x)
    print(y)

fun2("Sajid", "Khan")    
'''

# keyword Arguments
# specifies position of an argument. Rarely used but improves readibility
# use keyword argument after positional argument

'''
def fun2(x, y):
    print(x)
    print(y)

fun2(y="Sajid", x="Khan")   
'''

# function that return values
# by default a function return "None"
'''
def divr(no):
    return(no/4)

print(divr(2)) 
'''

# Creating a reusable function

def semoj(msg):
    words = msg.split(" ")
    emojis ={
        ":)": "Smile",
        ":(": "Sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(semoj(message))

