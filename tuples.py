# Tuples are like list but can't be modified like lists (immutable)
# defined using () e.g num = (1, 2, 3)
# only supported actions are count and index
'''
num = (1, 2, 10)
print(num[1])
'''

# Unpacking - Automatically stores values from tuples or lists in variables
'''
coordinates = (1, 2, 3)
x, y, z = coordinates

print(x, y, z)
'''
# Dictionaries - store Key vale pairs. Each key should be unique

custome = {
    "name": "John Smith",
    "age": 30,
    "is_verify": True
}

# each value is accessed by key
'''
print(custome["name"]) # updates a key

custome["next"] = "Jack Smith" # updates the name to Jack Smith
print(custome.get("bday", "Jan 1 1980")) # if key doesn't exist it will print default
'''

pn = input("Phone: ")

output_str = ""
phn = {
    "1": "One",
    "2": "Two"
}

for x in pn:
    output_str += phn.get(x, "!") + " "
print(output_str)       