import math
# More math helpers
print(math.floor(3 /2))  # explicitly rounds down
print(math.ceil(3 /2))   # explicitly rounds up
print(math.sqrt(2))      # square root
print(math.pow(2,3))     #  power or variable raised up ... 2 to power of 3

# Max / Min Int
float("inf")  # maximum integer
float("-inf") # minimum integer

# Python numbers are infinite so they never overflow
# Example
import math
print(math.pow(2, 200)) 

# very large number but still less than infinity
print(math.pow(2, 200) < float("inf")) # yeilds TRUE

