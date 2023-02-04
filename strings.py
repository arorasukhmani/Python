# Strings in python are surrounded by either single or double quotation marks. 
 
name = 'Zed'
age = 28

# Concatenate
print('Hello, my name is '+ name)

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
 