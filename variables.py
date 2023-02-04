# A variable is a container for a value, which can be of various types


# VARIABLE RULES:
#   - Variable names are case sensitive 
#   - Must start with a letter or an underscore
#   - Can have numbers but can not start with one

x = 1               # int by default
y = 6.9             # float
name = 'Adam'       # strings can have '' or ""
is_cool = True      # boolean True False

# Multiple assignment
x, y, name, is_cool= (1,6.9,'Adam',True)

# printing
print('Hellooo')
print(y,name)

# Basic Maths
a = x + y
print(a)

# to print data type
print(type(x))

# type casting 
x = str(x)
z = int(y)
print(type(x),x,type(z),z)
