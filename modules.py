# it is just another python file with code by using import function to reference the file
# in this case module will be referenced with prepending filename and then module name
# import func

# we can either import whole file or just specific module. if importing just module/class/function use:
# from <filename without extension> import <function/module name>
# We can reference module directly i.e. without file name


# serch for "python 3 module index" in google
'''
from func import semoj

message = input(">")
print(semoj(message))
'''

# using Random module

import random

'''
x = random.randint(1, 20)
y = random.randint(1, 20)

print(f"({x}, {y})")
'''

# better approach

class Dice:
    def roll(self):
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        return x, y


dice1 = Dice()
print(dice1.roll())        


