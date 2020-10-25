
def dwnld(url):
    print("Connecting to " +  url)


url1 = input("Enter download URL: ") 
 
dwnld(url1)


'''
name = str(input("Enter your name: "))
if len(name) < 3:
    print("name too short")
elif len(name) > 10:
    print("Name too long")
else:
    print("Name looks good!")
'''
# convert kilos to Lbs and vice versa
'''
wt = int(input("Enter your weight: "))
tp = input("L or K")

if tp.upper() == "L":
    conv = wt * 0.45
    print(f"Weight is {conv} Kilos")
else:
    conv = wt / 0.45
    print(f"Weight is {conv} Lbs")
'''

# while loop

'''
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")
'''

# Guessing game
'''
Guess = 7
i = 1

while i <= 3:
    gn = int(input("Enter the number to guess: "))
    if gn == Guess:
        print("You guessed right!!!")
        break
    else:
        print("Try again...")
        i += 1

# guessing game with while else
Guess = 7
i = 1

while i <= 3:
    gn = int(input("Enter the number to guess: "))
    i += 1
    if gn == Guess:
        print("You guessed right!!!")
        break
else:
    print("Sorry, you failed...")


# car game with while loop

act = ""
st = False
so = False

while True:
    act = input(">").lower()
    if act == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif act == "start":
        if st:
            print("Car is already started")
        else:
            st = True
            print("car started...")
    elif act == "stop":
        if not st:
            print("Car is already stopped")
        else:
            st = False
            print("car stopped...")    
    elif act == "quit":
        break
else:
    print("I don't understand")
 '''               

