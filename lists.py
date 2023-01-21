# A list is a collection which is ordered & changeable.
# Allows duplicate members
# they are like arrays

# Create list
numbers = [1,2,3,4,5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use constructor
numbers2 = list((6,7,8,9))

print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangoes')
print(fruits)

# Delete from list
fruits.remove('Grapes')
print(fruits)

# Insert at a particular index
fruits.insert(2,'Strawberries')
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse
fruits.reverse()
print(fruits)

# Sort a list
fruits.sort()
print(fruits)

# Sort in reverse order
fruits.sort(reverse=True)
print(fruits)

# Change value
fruits[0]='Blueberries'
print(fruits)

fruits[0]='Apples'
print(fruits)