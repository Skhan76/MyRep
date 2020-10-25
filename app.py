# This is a comment
ab = [1,2,3,4]
print(ab)
ab.append(5)
print(ab)
#use pop to remove last element
print(ab.pop(4))
x = ab.pop
for x in ab:
    print(x)

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

# playing with Sets
print("\n playing with sets")
s = {1, 2, 3}
print(s)