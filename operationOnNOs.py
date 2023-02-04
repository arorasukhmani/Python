from math import*

print(5+(2*5))

num = 5
print(num)
print("My number is " + str(num))

x=-5
print(abs(x))

print(pow(7,3))
print(max(7,3))
print(min(7,3))
print(round(7.7))
print(floor(7.7)) 
print(ceil(7.7))  
print(sqrt(49))

# exponent number
print(2**3)   #2^3

def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(3,4))