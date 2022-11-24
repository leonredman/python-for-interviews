# tuples are like arrays but immutable
# similar to arrays but to initialize we use parenthesis instead of  brackets
# we can index them, but we cant modify them
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify
tup[0] = 0  # wont work

#Mainly use tuples as keys for hash map/set
myMap = { (1,2): 3 }  # mapping a pair of values "1,2" to 3
print(myMap[(1,2)])
# this tuple is our hashable key
# we can do the same thing for hash sets
mySet = set()
mySet.add((1, 2))
print((1,2) in mySet)

# we can then use that tuple to search the hash set
# we do this because lists are not hashable and cant be keys for hash sets or maps
myMap[[3, 4]] = 5   # will not work