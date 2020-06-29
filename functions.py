def sayHello(name):
    print(f'Hello {name}')
# default arguments


def sayHello1(name='johnDoe'):
    print(f'hello {name}')


sayHello('anubhav')
sayHello1()

# return values


def getSum(num1, num2):
    total = num1 + num2

    return total


# num = getSum(3,4)
print(getSum(3, 4))


# lambda functions is a small anonymous functions
# it can take any number of arguments, but can only have one expression
# - very similar to js arrow functions

# def getSum1(num1, num2): return num1 + num2
# getSum1=lambda num1, num2: return num1 + num2  # commented due to flake8 error E731 (convertin git back to normal function on save)


# print(getSum1(19, 20))
