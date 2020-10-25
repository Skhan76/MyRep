# laregest item in a list
'''
myl = [10, 3, 17, 8, 1]
num = 0

for x in myl:
    if x > num:
        num = x
print(num) 
'''

# 2D list

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# items are access on row and item number basis
# 1 will be row 0, item 0 and so on...
# we can modify a matrix value using same reference
'''
print(mat[0][0]) # Thia prints 1
print(mat[2][2]) # This prints 9
'''
# To print a whole list
'''
for row in mat:
    for x in row:
        print(x)
'''

# List Methods/ List functions
'''
.append
.insert(index, value)
.remove(value)
.clear # removes all items from the list
.pop # removes last item
.index(value) # returns index of an item in the list
.count(value) # returns number of times an item existis in the list
.sort()
.reverse() # reverses the list
.copy() # copies a list
'''
# remove duplicats in a list

ls = [1, 5, 3, 8, 5, 6, 7]

'''
#### Bad logic
numc = 0
for x in ls:
    num = ls.count(x)
    if num > 1:
        for i in num:
            ls.remove(num) 
'''

# Good logic

uniques =[]

for x in ls:
    if x not in uniques:
        uniques.append(x)
print(uniques)

