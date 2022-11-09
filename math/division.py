# Division is decimal by default, most languages use integer division
print (5 / 2)  # yeild is 2.5, most other languages will round to 0 by default and yeild  2

# If you want integer division in python
# Double slash  that rounds down like this
print(5 // 2)  # yeild is 2

# You must be Careful as most languages round towards 0 by default
# So negative numbers will round 'down' in python using integer division
print(-3 // 2)  # yeild -2 but decimal value would be 1.5 most languages would be -1

# A workaround for rounding towards zero is to 
# use decimal division and then convert to int. It will round towards zero - this yeilds -1 if desired use case
print(int(-3 / 2))