# A dectionary is a collection which is unordered, changeable & indexed
# No duplicate members

# Create
person ={
    'first_name':'Hardin',
    'last_name':'Scott',
    'age':28
}
print(person,type(person))

# by using a constructor
person2 = dict(first_name='Adam',last_name='Carlsen')
print(person2,type)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key value
person['phone'] = '987654321'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person3 = person.copy()
person3['city'] = 'India'
print(person3)

# Remove an item
del(person['age'])
print(person)
print(person3)

person.pop('phone')
print(person)

# Clear dict
person.clear()
print(person)

# Get len
print(len(person3))

# list of dict
people = [
    {'name': 'Zed', 'age': 28},
    {'name': 'Landon','age':29}
]
print(people)
print(people[1]['name'])