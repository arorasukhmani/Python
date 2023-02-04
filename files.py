# Open a file
myFile = open('myFile.txt','w')

# To check if the file is readable
print(myFile.readable())

# To read all the contents
# print(myFile.read())
# print(myFile.readline())
# print(myFile.readlines())
# print(myFile.readlines()[1])

# Get some info of the file
print('Name: ',myFile.name)
print('Is Closed : ',myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to a file
myFile.write('This is my first python course')
myFile.close()

# Append to file
myFile = open('myFile.txt','a')
myFile.write(' \n I will learn more')

# Read from file
myFile = open('myFile.txt','r+')
text = myFile.read(100)
print(text)
print(myFile.readline())

