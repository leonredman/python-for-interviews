# Sorting an array - will sort in ascending order by default
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)
# yeild [3, 4, 5, 7, 8]


arr.sort(reverse=True)


# sorting strings by default will be by alphabetical order
arrString = ["bob", "alice", "jane", "doe"]
arrString.sort()
print(arrString)

#yeild ['alice', 'bob', 'doe' 'jane']

# Custom sort (by length of string) we cam pass in a lambda function
# basically a function without a name the key is equal to lambda. We take every single 
# value from the array call it x then return from that the length of x and this is the key
# that is used to sort the string. Each string is mapped to its length and 
# then we sort those strings based on their length. By default will be in ascending order
# 
arr.sort(key=lambda x: len(x))
# yeild ['alice', 'bob', 'doe', 'jame']

# initiliaze lists - List Comprehension
# to go through every value in range 5 and call that value i and then add that value
# to the array - this is the short hand
arr = [i for i in range(5)]
print (arr)
# yeild [0, 1, 2, 3, 4]

# we can add to i
arr = [i+i for i in range(5)]
print (arr)
# yeild [0,2,4,6,8]

# 2-D Lists
arr = [[0] * 4 for in range(4)]
print (arr)
# yeild an array with all zeros  this will build a grid of all zeros

