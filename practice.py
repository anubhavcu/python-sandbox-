
# lists - ordered and indexed
# allows repitition, changeable
numbers = [1, 2, 3, 4, 5, 'cat']
numbers1 = list((1, 2, 3, 4, 5, 6))

print(numbers, numbers1)

# check members
print('cat' in numbers)
print(200 in numbers)

numbers2 = numbers1 + numbers
print(numbers2)

# adding
numbers.append(4)   # repititive elements allowed
numbers.insert(0, 100)
print(numbers)

# removing
numbers.remove(100)
numbers.pop(1)
numbers.pop()
print(numbers)

# list w/in lists
l1 = [1, 2,  3, 4]
l2 = [10, 20, l1, 30, 40]       # embedding
l3 = [10, 20, *l1, 30, 40]      # unpacking
print(l2, l3)
a, b, c, d = l1
print(a, b, c, d)

# sorting
l3.sort()
print('sorted', l3)
l3.sort(reverse=True)
print('reverse sorted', l3)

l3.sort()
l3.reverse()
print(l3)

# swapping
l1, l2 = [1, 2, 3, 4, 5], [5, 6, 7, 8, 9]
print(l1, l2)
l1, l2 = l2, l1
print(l1, l2, 'swapped lists')

# slicing
print(l3[:4])
print(l3[::-1])
l4 = l3[::-1]
print(l4, 'l4')
# l5 = l4.sort(reverse=True) # we can't use statements like this as rhs doesn't return anything, instead we shoud do-
l4.sort(reverse=True)
l5 = l4
print(l5, ' new list l5')
# we can't assign values like l4= l3.sort() as rhs doesn't return anything, but we can do l4= l3[::-1]

#index and count
print(l5.index(1))      # return first occurence of 1
print(l5.count(4))


# -----------x --------
# tuples - ordered and indexed
# allows repitition and NOT changeable
tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple((4, 6, 7, 7))
print(tuple1, tuple2)

# single valued tuples are treated as strings if not used with a trailing comma
t1 = ('apples')
t2 = ('apples', )

print(type(t1), t1)
print(type(t2), t2)


tuple3 = tuple1 + tuple2
print(tuple3)

# unpacking , embedding, slicing, index, count, swapping
# -- same as like lists
# tuples behaves almost like lists but they are immutable like
# tuple1[4] = 5  will throw an error and also we cannot append ,insert into a tuple


# -------x- -------
#sets- unordered and unindexed
# NO repitition allowed and are mutable

fruits = {'apples', 'oranges', 'banana'}
print(fruits, type(fruits))

s1 = {1, 2, 3, 4, 'cat'}
s2 = set((1, 2, 3, 4, 5, 5, 'cat'))
print(s1, type(s1))
print(s2)   # repititive elements are removed

# membership
print('cat' in s1)
print(5 in s1)


# adding
s1.add('dog')
s1.add(4)
print(s1)   # repititive elements are removed

# removing
s1.remove('dog')
print(s1)
s1.pop()
print(s1)
# since lists are unordered and unindexed we don't know which element gets removed

# joining - union and update
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s1.update(s2)
print(s1)   # note repititive elements are removed
s3 = s1.union(s2)
print(s3)
# s4 = s1.update(s2) -  again we can't assign sets like this as upadte doesn't return anything


# dictionary - unordered but indexed
# NO repitition, changeable
person = {'first_name': 'john', 'last_name': 'Doe', 'age': 21}
print(person, type(person))

print(person['first_name'])

# adding
person['company'] = 'Google'
print(person)

# remove
del person['age']
print(person)

# we can also use pop, it will take key value, - in case of sets we weren't able to pass anything as sets are unordered and unindexed but our dictionaries are indexed
person.pop('company')
print(person)

# check member
print('first_name' in person)
print('company' in person)


# lists of dictionaries
people = [
    {'first_name': 'john', 'last_name': 'doe', 'age': 23},
    {'name': 'sarah williams ', 'company': 'Google'}

]
print(people, type(people))
# check for membership
print('name' in people[0])
print('name' in people[1])

# adding dictionaries
d1 = {'first_name': 'john', 'last_name': 'doe'}
d2 = {'last_name': 'williams', 'age': 24}

d1.update(d2)
print(d1)
# since repititions are not allowed so common parameters are picked up from d2


# -------------------
# functions
def sayHello(name):
    # use this instead of newer f-strings as they are mostly not supported on competitive websites
    print('hello there, this is {name}'.format(name=name))


sayHello("john doe")


# def calculateSum(x, y):
#     return x+y


# x, y = map(int, input('enter two numbers, space seperated ').split())
# print("Sum of numbers {x} and {y} is: ".format(x=x, y=y), calculateSum(x, y))


# lambda functions
# res = lambda x, y : return x+y


# --------------
# membership - in || not in
l1 = [1, 2, 3, 4, 'cat']

if 'cat' in l1:
    print('cat' in l1)

print('dog' in l2)


# ---------------------------------------
# also check 'is' and 'is not' in conditionals.py file


# ----------------
# loops
numbers = [100, 12, 3, 43, 2, 63, 45, 76]

for number in numbers:
    print(number)

# for indices

for x in range(len(numbers)):
    print(x)

# range(start, stop, step), - default step is 1, range function will go upto stop-1

for x in range(1, 11):
    print('hello ', x)

for x in range(5, 101, 5):
    print(x)

# -ve steps

for x in range(10, 2, -2):  # will go upto 4
    print(x)

# reverse order

for x in range(11, 0, -1):      # 11 -> 1
    print(x)

for x in reversed(range(len(numbers))):
    print(numbers[x])

# enumerate -  allows to loop over lists with numbers and index

for i, v in enumerate(numbers):
    print(i, v)             # prints correspoding index and value

# zip -  allows to loop over multiple lists at same time
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

for x, y in zip(l1, l2):
    print(x, y)
