# A Tuple is a collection which is ordered and unchangeable
# Allows duplicate memebers
 

# Create tuple
fruits=('Apples', 'Oranges','Grapes')

# by using a constuctor
fruits2=tuple(('Apples', 'Oranges','Grapes'))

print(fruits,fruits2)

fruits3=('Mangoes')
print(fruits3,type(fruits3))

# Single value needs a trailling comma
fruits4=('Mangoes',)
print(fruits4,type(fruits4))

# get a value
print(fruits[1])

# cannot chnage the value
# fruits[0]='pears'

# Delete a tuple
del fruits2
# print(fruits2)

# To get length
print(len(fruits))


# A SET is a collection which is unordered and unindexed
# No duplicate members

# Create a Set
fruits_set = {'Apples','Oranges','Mangoe'}
print(fruits_set)

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Will not add duplicates
fruits_set.add('Apples')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete a set
del fruits_set
print(fruits_set)

