# class User:

#     # class variable
#     age_less_than_30 = True

#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def greeting(self):
#         return 'my name is {name} and i am {age} years old '.format(name=self.name, age=self.age)

#     def hasBirthday(self):
#         self.age += 1

# # to access values inside methods within the class use self(similar with this)


# # initializing the User object
# john = User('john wick', 'john@google.com', 25)
# print(john)
# print(john.name)
# print(john.greeting())
# john.hasBirthday()

# print('after birthday', john.greeting())

# # customer class extending User class


# class Customer(User):

#     # age_less_than_30 = False

#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.balance = 0

#     def set_balance(self, balance):
#         self.balance = balance

# # if we haven't redifined this function here then User's greeting function would have called
#     def greeting(self):
#         return 'my name is {name} and i am {age} years old and my balance is {balance}'.format(name=self.name, age=self.age, balance=self.balance)


# # initializing customer object
# sara = Customer('Sara', 'sara@yahoo', 23)
# balance = int(input('Enter balance : '))
# sara.set_balance(balance)


# # customer can access parent class methods
# print(sara.greeting())
# print(john.age_less_than_30)
# # Customer class's object can also access parent classe's methods and variables
# print(sara.age_less_than_30)
# # but if we again define a function/variable with same name in customer then first customer's method would be called


# we can use pass if we don't want any body for class methods for the time being , for eg
# class Abc:
#     def sayHello():
#         pass


# more ex:
class User:
    def __init__(self, firstName, lastName, age, company):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.company = company

    def greeting(self):
        return 'hello world this is {firstName} {lastName} and i am {age} years old working at {company}'.format(firstName=self.firstName, lastName=self.lastName, age=self.age, company=self.company)

    def sayHello():
        print('hello world - static method without @static method decorator')

    @staticmethod
    def sayHelloAgain():
        print('hello world - static method with @static method decorator')


john = User('john', 'doe', 25, 'Google')
print(john)
print(john.greeting())
User.sayHello()
john.sayHelloAgain()

# Notes
# 1. In python we define class with 'class(base)', if base class is omitted then object is assumed
# 2. instance methods takes an explicit 'self' first parameter which references the instance(object created)
#     so for eg if john is the object(instance) of class User then we call
#     -john.sayHello()
#     internally which gets converted into - User.sayHello(john)
# *3- to declare an instance method we can omit the 'self' argument and use a staticmethod decorator. the latter prevents the instance being passed as a parameter when we call the method from that instance.
# In above eg sayhello function can be called with class name only, if we call the sayHello function with the instance(object) of the User class i.e john.sayHello() - we would be getting an error as python will try to pass an instance as a parameter which is missing also there is no @staticmethod decorator .
# but for @staticmethod decorator , functions can be called by either class or objects
