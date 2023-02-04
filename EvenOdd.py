# a = int(input("Enter the number:\n"))
# if ((a % 2 == 0)):
#     print("Even")
# else:
#     print("Odd")



ce=0
co=0
for i in range(5):
    a = int(input('Enter a number: '))
    if a%2==0:
        ce=ce+1
    else:
        co=co+1

print(f'even: {ce}')
print(f'odd: {co}')
