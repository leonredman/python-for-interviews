# Arrays (called lists in python)  most common DS next to hashmaps
arr = [1, 2, 3]
print(arr)
# yeild [1,2,3]

# can be used as a stack
arr.append(4)  # can push to end of an array
arr.append(5)
print(arr)
# yeild [1,2,3,4,5]

arr.pop()  # can pop from the end of array ( last value)
print(arr)
# yeild [1,2,3,4]

# Because this is an array we can insert into the middle as it is not technically a stack
# insert at index of 1, value of 7  is BIG-O of O(n) time operation
arr.insert(1, 7)
print(arr)
# yeild [1, 7, 2, 3, 4]

# Reading and Reassigning
# To index an array is not a O(n) time operation - these are O(1) constant time operations
arr[0] = 0
arr[3] = 0
print(arr)

# To initialize and array (arr) of variable size (n) with default value or 1
# arr of size 5 with all values of 1
n = 5
arr = [1] * n  # weird using multiplication sign her but its syntax is correct
print(arr)
print(len(arr))
#yeild [1, 1, 1, 1, 1]
#yeild 5

# Careful when indexing array: -1 is not out of bounds,
# python will read the last value on the right
arr = [1, 2, 3]
print(arr[-1])
# yeild 3

# Indexing -2 is the second to last value etc.
print(arr[-2])
# yeild 2

# Getting sublists is one of the most useful features of python (aka SLICING)
arr = [1, 2, 3, 4]
print(arr[1:3]) # taking values from array from index 1 to index 3 but not including index 3
# yeild [2, 3]

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0, 4])
# yeild [1, 2, 3, 4]

# Unpacking - taking all the elements of an array and assigning them to variables
# helpful when going thru a list of pairs
a, b, c = [1, 2, 3]
print(a, b, c)
# yeild 1 2 3

# be careful the number or variables must match the num or elements from the array
a, b = [1, 2, 3]   # NO!

# Loop thru arrays
nums = [1, 2, 3]

# we can do it using index using length and iterate that many times and print vals
for i in range(len(nums)):
  print(nums[i])
#yeild 1 2 3

# We can do it without index (simpler) go thru ever value in nums and print that value
for n in nums:
  print(n)
#yeild 1 2 3

# if you needed both  index and value, you can use the enumerate
for i, n in enumerate(nums):
  print(i, n)
#yeild 0 1  1 2  2 3

# To Loop through Multiple arrays simultaneously with Unpacking
# We can use a helper function called zip
# This will combine them into an array of pairs and then we can unpack those values
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
  print (n1, n2)
# yeild 1 2  3 4  5 6

 # Reversing and Array we call the reverse method
nums = [1, 2, 3]
nums.reverse()
print(nums)
# yeild [3, 2, 1]
