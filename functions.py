# A function is a block of code which only runs when it is called
# No curly brackets but indentation with tabs or spaces

# Create a function
# def sayHello(name = 'trevor'):
def sayHello(name):
    print(f'Hello {name}')

sayHello('Jeremy')

# return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3, 4))

num = getSum(4,5)
print(num)

def max_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max_num(5,8,1))

# A LAMBDA function is a small anonymous function
# can only take any number of arguments
# but can have only one expression

getSum = lambda num1, num2 : num1 + num2
print(getSum(10,3))