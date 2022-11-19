# HashSet - these are useful as we can search them in constant time
# and we can insert values in constant time

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
# yeild {1, 2}  unlike a list there cannot be any duplicates in a hashset

# we can get the length to know how many items have been inserted
print(len(mySet))
# yeild 2

# we can search the hashset with out a function using the 'in' operator
print(1 in mySet)  # to see if 1 exists
# yeilds True
print(2 in mySet)
# yeilds True
print(3 in mySet)
# yeilds False

# we can remove values in constant time
mySet.remove(2)
print(2 in mySet)
# yeild False

# to initialize a hashset we can pass in a list
# list to set
print(set([1, 2, 3]))
# yeild {1, 2, 3}

# Set comprehension - we can manually initialize with a loop inside of the hashset
# we set the value of i and iterate thru the value of i and set to the hashset
mySet = { i for i in range(5) }
print(mySet)
# yeild {0, 1, 2, 3, 4}

