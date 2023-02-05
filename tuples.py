# A Tuple is a collection which is ordered and unchangeable
# Allows duplicate memebers
# Tuple is a type of data structure
 

# Create tuple
fruits=('Apples', 'Oranges','Grapes')

# by using a constuctor
fruits2=tuple(('Apples', 'Oranges','Grapes'))

print(fruits,fruits2)
print(fruits[1])

fruits3=('Mangoes')
print(fruits3,type(fruits3))

# Single value needs a trailling comma
fruits4=('Mangoes',)
print(fruits4,type(fruits4))

# get a value
print(fruits[1])
print(fruits[1:])
print(fruits[::-1])
print(fruits[1:3])

# cannot chnage the value
# fruits[0]='pears'

# Delete a tuple
del fruits2
# print(fruits2)

# To get length
print(len(fruits))

list1 = [1,6,7,8,0]
# converting list into tuple
print(tuple(list1))

