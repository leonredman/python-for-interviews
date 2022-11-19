 #HashMap ( aka dict )
# Hashmaps are the single most common data structure we will use
# like hashsets we cant have duplicate keys inside the hashmap
# to insert we take a value example a string and assign it to another value 88 which is the key
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77

# printing is simple
print(myMap)
# yeild {'alice' : 88, 'bob' : 77}

# getting the length
print(len(myMap))
# yeild 2

# we can modify the value thats mapped to a key
myMap["alice"] = 80
print(myMap["alice"])
#yeild 80

# can also search if a key exists ih a hashmap in constant time
print("alice" in myMap)
# yeild True

# we can also remove that key which will remove the value
myMap.pop("alice")
print("alice" in myMap)
# yeild  False

# to initialize we can add pairs inside of the curly braces
myMap = { "alice" : 90, "bob" : 70 }
print(myMap)

# can also use Dict comprehension with a loop
# we are looping i in the range of 3, we are gonna have 2 values. i is the key and the colon
# we are mapping i so its 2 times i  (used mostly with graph problems and adjacency lists)
myMap = { i: 2*i for i in range(3) }
print(myMap)
# yeild {0: 0, 1: 2, 2: 4}

# Looping through maps
# default method loop through every key and then print that key and every value that key  maps to
myMap = { "alice": 90, "bob" : 70}
for key in myMap:
  print(key, myMap[key])
# yeilds alice 90  bob 70

# we can also iterate directly thru the list of values and then print the value if we dont need the key
  for val in myMap.values():
    print(val)
  # yeilds 90 70

# we can use unpacking we can go thru the items of the map
# which will give us the key and the value
for key, val in myMap.items():
  print(key, val)
# yeilds alice 90 bob 70