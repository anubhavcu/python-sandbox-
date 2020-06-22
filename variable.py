''' variable names are case sensitive
start with x letter or underscore
can have numbers but cannot start with
'''

x = 1
y = 2.5
name = 'john'
is_cool = True
co_ordinate = complex(3, 5)
z = None

print(x, y, name, is_cool, co_ordinate, z)

# types
print(type(x))  # int
print(type(y))  # float
print(type(name))   # string
print(type(is_cool))    # boolean
print(type(co_ordinate))  # complex
print(type(z))  # NoneType

# multiple assignments
x, y = 5, 8

print(x, y)


# basic math
print(x+y)
print(x-y)
print(x*y)
print(24/5)     # floor division
print(24//5)    # returns quotient
print(24 % 5)   # returns remainder
print(2**3)     # power - same as math.pow
print('pow funtion', pow(4, 5))

# casting
a = 3
a = str(a)  # type str
b = 6.5
b = int(b)  # type int
print(type(a))
print(type(b), b)
c = float(b)

print(c, type(c))


# built- in functions
z = -5.5
print(abs(z))   # returns positive
print(min(5, 2))
print(max(5, 2))
print(divmod(24, 9))  # returns quotient-remainder pair
# round takes expression and number of decimal places to round to
print(round(100/3, 4))
# round will return 2 in 2.x if x<= 2.5 else it will return 3 if x > 2.5
print(round(2.5))   # 2
print(round(2.6))   # 3

# boolean values - anything other than 0 is True
print(int(True))  # 1
print(int(False))   # 0
print(True > False)     # True
print(bool(-2))     # True
print(bool(0))  # False
