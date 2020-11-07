'''
test = [2, 3, 4]

x, y, z = [2, 3, 4]
print(x)
print(y)
print(z)
'''

# class definition

'''
class TestClass:
    def pr(self):
        print("Test message")

    def pr2(self):
        print("Hello")

obj1 = TestClass()
obj1.pr()
obj1.pr2()

# variable definition
obj1.x = 10
print(obj1.x)
'''

# Constructs/constructor
# it is used to initialize variables within an obj at definition time
'''
class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pr(self):
        print("Test message")

    def pr2(self):
        print("Hello")

obj1 = TestClass(10, 20)
print(obj1.x)

obj1.x = 11
print(obj1.x)
'''

# practice
'''
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"I am talking {self.name}")

m1 = "How are you"
per1 = Person("Sajid")

per1.talk()
'''

# Inheritance

class Mammal():
    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):  # Dog class is inherating Mammal class
    pass            # pass is used if there is no method definition in this class i.e. it is referencing
                    # another class but doesn't have methods of its own

Dog1 = Dog()
# Dog1.walk()

class Cat(Mammal):
    def meow(self):     # here we didn't use pass as cat has its own method defined and it i not empty
        print("Meow Meow")

cat1 = Cat()
cat1.walk()
cat1.meow()

# 