# a tuple is a collection which is ordered and unchangeable. Allows duplicate members
# tuples behave a lot like lists - apart from their immutability

# create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
print(fruits)
print(type(fruits))

# tuples can be heterogenous- can have different types within them
o = (0, 1, 2, 3, 4, 'cat')
print(o, type(o))

list1 = ['apples']
# single valued tuples need a trailing comma, otherwise it will be a str type
tuple1 = ('apples',)
print(type(list1))
print(type(tuple1))

# get a value
print(fruits[1])

# can't change a value
# fruits[1] = 'Banana'      # will throw an error
# print(fruits)


# deleting a tuple
del tuple1

# len of tuple
print(len(fruits))

tuple2 = (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(tuple2)

tuple2 = tuple2 * 2     # works fine
print(tuple2)

# concatenate tuples
tuple3 = (10, 11, 12)
tuple4 = tuple2 + tuple3
print(tuple2 + tuple3)
print(tuple4)

# same as with lists
print(tuple3.index(11))     # return index of first occurence
tuple3 = tuple3 * 2
print(tuple3.count(10))     # returns number of occurences

# unpacking - same as lists
new_tuple = (1, 2, 3)
a, b, c = new_tuple
print('unpacking', a, b, c)

# unpacking and embedding -same as lists
x = (1, 2, 3, 4)
y = (10, 20, x, 30)
z = (10, 20, *x, 30)

print('x', x)
print('y', y)
print('z', z)


# slicing of tuples - same as with lists and strings
new_tuple = new_tuple * 5
print('new tuple', new_tuple)
print(new_tuple[:5])
print(new_tuple[::-1])
tp = (1, 2, 3, 4)
tp = tp[::-1]
print('reversed tuple', tp)

# check for membership
print(5 in new_tuple)
print(1 in new_tuple)

# swapping of tuples
t1, t2 = (1, 2, 3, 4), (5, 6, 7, 8)
print(t1, t2)
t1, t2 = t2, t1
print(t1, t2)

# set is a collection which is unordered and unindexed , no duplicate members

# create set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}
# fruits_set1 = set((1, 2, 3, 4, 5))
# print('using constructor', fruits_set1, type(fruits_set1))

# check if in set
print('Apples' in fruits_set)

# heterogenous sets
s1 = {1, 2, 3, 4, 'cat'}
print(s1, type(s1))

print(fruits_set)
fruits_set.add('grapes')
# fruits_set.insert(1, 'lichi')     # error
# fruits.append('lichi')            # error
fruits_set.add('lichi')
fruits_set.add('aa')
fruits_set.add(4)
print(fruits_set)

# remove
fruits_set.remove('aa')
print('before popping', fruits_set)
fruits_set.pop()
print('popped', fruits_set)
# note - sets are unordered, so we don't know which item gets removed


# clear set
fruits_set.clear()
print(fruits_set)    # empty set

# delete set
# del fruits_set
# print(fruits_set)     # will throw an error fruits_set is not defined

new_fruits_set = {'Apples', 'oranges', "banana"}
print('new_fruits_set', new_fruits_set)
new_fruits_set.add('apple')
new_fruits_set.add('Apples')
# not added this element as it was present previously, duplicates are not allowed
print('new_fruits_set', new_fruits_set)


# len of sets
print(len(new_fruits_set))
# since sets are unordered, we don't know which item gets removed
x = new_fruits_set.pop()
print(x)
x = new_fruits_set.pop()
print(x)


# joining of sets
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6}
# s3 = s1 + s2    # get an error as unsupported operand
s3 = s1.union(s2)
# won't show repititive elements -as no duplicate values are allowed in sets
print('s3', s3)

s1.update(s2)
# print(s1.update(s2))    # wrong method
print('new s1', s1)
