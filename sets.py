# A SET is a collection which is unordered and unindexed
# No duplicate members

# Create a Set
fruits_set = {'Apples','Oranges','Mangoe'}
print(fruits_set)

# to calculate length
print(len(fruits_set))

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Will not add duplicates
fruits_set.add('Apples')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Remove from set when you aren't sure if it is in the set or not
fruits_set.discard('kiwi')
print(fruits_set)

# to add multiple elts
fruits_set.update(['Grape','kiwi'])
print(fruits_set)

# to pop a random elt
print(fruits_set.pop())

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete a set
del fruits_set
#print(fruits_set)

# UNION of sets can be done by two ways: pipeline, concatenation
a = {2,4,7,'fk'}
b = {1,5,2,9,'u'}
c = {4,1,10}

print(a|b)   #pipeline
print(a.union(b))   #concatenation
print(a|b|c)
print(a.union(b,c))


# INTERSECTION of sets can be done by two ways: "&"  intersection()
print(a&b)
print(c.intersection(b))

#DIFFERENCE 
print(a-b)
print(b.difference(c))

# FROZEN set: set whose value cannot be changed
d = frozenset(a)
print(d)
#print(d.add(1))