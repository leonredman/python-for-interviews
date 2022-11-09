# Modding is similar to most languages
print(10 % 3) # yeild is 1; {3 x 3 = 9, modulo 1}

# Except for negative values
print(-10 % 3) # yeild is 2; which is different from most languages

# To be consistent with other languages modulo run this
import math
print(math.fmod(-10, 3))  # yeilds -1.0 as expected