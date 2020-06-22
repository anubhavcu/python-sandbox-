# dictionary is a collection which is unordered, changeable,and indexed  and no duplicate members allowed

# create dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 24
}

# using constructor - slightly different syntax
# person1 = dict(first_name='john', last_name='doe')

print(person, type(person))


# get a value
print(person['first_name'])
print(person.get('last_name'))


# add key-value
person['phone'] = '312312312'
print(person)

# get keys
print(person.keys())

# get items
print(person.items())


# copy dict
person2 = person.copy()
person2['city'] = 'new delhi'
print(person2)
print('ln 37 checking member', 'city' in person2)


# remove item
del(person['age'])
print(person)

person.pop('phone')
print(person)

# clear
person.clear()
print(person)


# length
print(len(person2))
print('person', person2)
person2['company'] = 'Google'
print(person2)
# person2.pop()     # pop with dictionaries require 1 argument
person2.pop('company')
print('after popping elements ', person2)

# list of dictionaries
people = [
    {'name': 'john', 'age': 30},
    {'name': 'sara', 'age': 23},
    {'company': 'Google', 'phone': 2132131321}
]
print('dictionary literal(list of dictionaries)', people)
print(people[0])
print(people[0]['name'])
print('checking member', 'company' in people[2])


d1 = {'name': 'john'}
print(d1, type(d1))
d2 = {'age': 21, 'name': 'sarah'}
print(d2, type(d2))
d1.update(d2)
print('new d1', d1)
