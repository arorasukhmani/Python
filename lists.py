# A list is a collection which is ordered & changeable.
# Allows duplicate members
# they are like arrays

# Create list
numbers = [1,2,3,4,5,4,7,4]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use constructor
numbers2 = list((6,7,8,9))

# To print all the elements
print(numbers, numbers2)
print(fruits[:])

# Get a value
print(fruits[1])

# to get index
print(fruits.index('Grapes'))

# To print all the elements after a specific index
print(fruits[2:])

# To print all the elements in range of index
print(fruits[1:3])

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

# To join 2 lists
numbers.extend(fruits)
print(numbers)

# To get index
print(numbers.index(5))

# To count the occurence
print(numbers.count(4))

# To make copy of a list
fruits2 = fruits.copy()
print(fruits2)

# to remove all the elts of the list
numbers2.clear()
print(numbers2)