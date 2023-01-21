# A loop is used for iterating over a sequence
# eg list, tuple, dictionary, set, string

people = ['Zed','Hardin','Adam','Landon']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')

# Break 
for person in people:
    if person == 'Adam':
        break
    print(f'Current Person: {person}')


# continue
for person in people:
    if person == 'Adam':
        continue
    print(f'Current Person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):   #will print from 0-10
    print(f'Number: {i}')

# WHILE loop
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1