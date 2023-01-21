# Almost everything in python is object

# Create class
class User:
    # Constructor               self is like this
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age +=1


# Extend class
class Customer(User):
    # Constructor               
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# initialize user object
adam = User('Adam Carlsen', 'adamcarlsen@gmail.com',38)

# initialize customer object
Zed = Customer('Zed Malik','zed@gmail.com',28)
Zed.set_balance(500)
print(Zed.greeting())

print(adam.name)
adam.has_birthday()
print(adam.greeting())
