# Variables are dynamically typed
# we set n equal to zero and we dont have to declare types

n = 0 
print('n = ', n)

# types are determined at runtime so we can reassign to a string if wanted and will be fine
n = "abc"

# We can do multiple assignments by adding both variables on the left and then both values on the right
# we can have multiple values on a single line
n, m = 0 , "abc"
n, m, z = 0.125, "abc", False

# Incrementing  is different
n = n + 1  # good
n += 1     # good (shorthand)
n++        # bad, cannot do plus plus 

# None is null (absense of a value in python)