# Exception handling
# Exit code 0 means success. Anything but 0 means crash

# This will print "Invalid vale" if code generates a vale error 
# ZeroDivionError

try:
    age = int(input("Age: "))
    print(age)

    a = 40/age
except ZeroDivisionError:
    print("Age can't be 0")
except ValueError:
    print('Invalid value')

