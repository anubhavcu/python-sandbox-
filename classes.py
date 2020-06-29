class User:

    # class variable
    age_less_than_30 = True

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return 'my name is {name} and i am {age} years old '.format(name=self.name, age=self.age)

    def hasBirthday(self):
        self.age += 1

# to access values inside methods within the class use self(similar with this)


# initializing the User object
john = User('john wick', 'john@google.com', 25)
print(john)
print(john.name)
print(john.greeting())
john.hasBirthday()

print('after birthday', john.greeting())

# customer class extending User class


class Customer(User):

    # age_less_than_30 = False

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

# if we haven't redifined this function here then User's greeting function would have called
    def greeting(self):
        return 'my name is {name} and i am {age} years old and my balance is {balance}'.format(name=self.name, age=self.age, balance=self.balance)


# initializing customer object
sara = Customer('Sara', 'sara@yahoo', 23)
balance = int(input('Enter balance : '))
sara.set_balance(balance)


# customer can access parent class methods
print(sara.greeting())
print(john.age_less_than_30)
# Customer class's object can also access parent classe's methods and variables
print(sara.age_less_than_30)
# but if we again define a function/variable with same name in customer then first customer's method would be called
