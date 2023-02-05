# Strings in python are surrounded by either single or double quotation marks. 
# strings immutable i.e existing string cannot be changed

name = 'Zed'
age = 28
sample = 'hy there! wassup?'

# to print entire string
print(sample[:])

# to print acc to index
print(name[0])

# to print last character
print(sample[-1])

# to print second last character
print(sample[-2])

# to print a range of characters
print(sample[2:8])
print(sample[2:])
print(sample[:8])
print(sample[-2:])
print(sample[2:8] + sample[10:])

# Concatenate
print('Hello, my name is '+ name)

# repetition
print(5 * 'fck')

#print('Hello, my name is '+ name + 'and I am ' + age + ' years old.') // will give an error
print('Hello, my name is '+ name + 'and I am ' + str(age) + ' years old.')

# Arguments by position
print ('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings 
print(f'Helloooo, my name is {name} and I am {age}')

# String Methods

s = 'helloo World'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# To check for upper case
print(s.upper().isupper())

# To check for lower case
print(s.islower())

# Swap Case
print(s.swapcase())

# Get length
print(len(s))

# Get character at index
print(s[5])

# Get index of character
print(s.index('h'))

# Replace
print(s.replace('World', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list (array)
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# print quotation marks
print("Abc\"xyz")
 
# "in" is a boolean operator that takes two strings
# return True is first appears as a substring in second
word = "banana"
print("a" in "banana")
print("a" in word)
print("f" in "banana")