x = 50
y = 50

# if-else:  <, >, ==

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is smaller than {y}')

if x > y:
    print(f'{x} is greater than {y}')
elif x < y:
    print(f'{x} is smaller than {y}')
else:
    print("Both numbers are equal")

# logical operators - and, or, not
x = 5

if x > 2 and x < 10:
    print(f'{x} is greater than 2 and less than 10')

if x > 2 or x <= 10:

    print(f'{x} is greater than 2 or less than 10')

if not(x == y):

    print(f'{x} is not equal to {y}')


# membership operators -not , not in
numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers)

if y not in numbers:
    print(y not in numbers)


# identity operators - is, is not

if x is y:
    print(x is y)

if x is not y:
    print('x is not y', x is not y)

if type(x) is int:
    print('x is int type')

l1 = []
l2 = []
l3 = l1
l4 = l3 + l1

print('l1 == l2', l1 == l2)     # true
print('l1 is l2', l1 is l2)     # false
print('l1 == l3', l1 == l3)     # true
print('l1 is l3', l1 is l3)     # true
print('l4 is l3', l4 is l3)     # false

# == and is are slightly different -
# == checks if values of both variables are same
# is checks whether variable point to the same object
# l1 is l2 returns false as two empty lists are at different memory locations , hence l1 and l2 refer to different objects - we can check that by id(l1) and id(l2)
# l4 is l3 return false as concatenation of two lists always produce a new list

a = 1
f = a
print('a', a, id(a))
print('f', f, id(f))
print(f is a)
a = 2
print('a', a, id(a))
print('f', f, id(f))
print(f is a)
# note when doing f = a, f now refers to the value a is referring to (not a), so when we change value of a,say to 2, then a will refer to 2 but f is referring to 1.
