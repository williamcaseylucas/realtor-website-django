# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"


# Customer extends User
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}"


# Init user object
brad = User("Brad Traversy", "brad@gmail.com", 37)
janet = User("Janet Williams", "jabent@gmail.com", 27)

# Edit property
brad.age = 38

print(brad.name, brad.age)
# Call method
print(brad.greeting())

# Init customer
john = Customer("john doe", "john@gmail.com", 40)

john.set_balance(500)
print(john.name)

print(john.greeting())
