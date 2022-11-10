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

# Custom sort (by length of string) an use a lambda
arr.sort(key=lambda x: len(x))