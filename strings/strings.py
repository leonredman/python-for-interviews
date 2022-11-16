#strings are similar to arrays
# can use single or double quotes
s = "abc"
print(s[0:2]) # can slice them the same way we do with arrays
#yeild ab

# Remeber this key point Strings are immutable - cannot modify/ cant reassign s at index zero
s[0] = "A"  # no good

# we can update though, which creates a new string  / its considered N-time operation
s += "def"
# yeild abcdef

# strings can be converted into integoers  and added
print(int("123") + int("123"))
# yeild 246

# And numbers can be converted to strings
print(str(123) + str(123))
#yeild 123123

# In the rare case you need ASCII values
# of a character
print(ord("a"))
# yeild 97
print(ord("b"))
# yeild 98

#combine a list of strings with a empty string delimitor
strings = ["ab", "cd", "ef"]
# empty string delimitor
print("".join(strings))
# yeild abcdef

