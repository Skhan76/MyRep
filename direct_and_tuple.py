'''
# Dictionary example
sal = {"jane":15, "John":20}
print(sal)

# append to dictionary
sal["andy"] = 25
print(sal)

# looping dictionary on keys
for item in sal.keys():
    print(item)

# looping dictionary on value
for item in sal.values():
    print(item)

# looping dictionary and printing both key & value
print("looping dictionary and printing both key & value")
for key, val in sal.items():
    print(key, val)
'''

# playing with Sets
'''
print("\n playing with sets")
s = {1, 2, 3}
print(s)
'''

# Dictionary game to convert digits to numbers
'''
no = input(">")

mapword = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}

output = ""
for x in no:
    output += mapword.get(x, "!") + " "

print(output) 
'''

# Dictionary game to convert message to emoji

no = input(">")
msg = no.split(" ")

mapword = {
    "Sad": ":(",
    "Happy": ":)",
    "Quiet": "x)"
}

output = ""
for x in msg:
    output += mapword.get(x, x) + " "
    
print(output) 