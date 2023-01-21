
x = 13
y = 15

# if else statement
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif    else-if
if x > y:
    print(f'{x} is greater than {y}')
elif y > x:
    print(f'{y} is greater than {x}')
else:
    print(f'{y} and {x} are equal')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operator

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 5 or x <= 10:
    print(f'{x} is greater than 5 and less than or equal to 10')

# not
if not(x== y):
     print(f'{y} and {x} are not equal')


# Membership Operators (not, not in)
# are used to test if sequence is presented in an object

numbers = [10,15,20,25,30]

# in
if x in numbers:
    print( x in numbers)

# not in 
if x not in numbers:
    print( x not in numbers)


# Identity Operators (is, is not)
# Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)