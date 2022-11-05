# for loops - syntax is a bit tricky vs explicit loop for(int i = 0; i < n; i++)
# Looping from i = 0 to i = 4  ( i goes in the range of 5, so starts at 0 and ends at 4) 
# i is incremented implicitly - dont have to tell loop to increment by one by default
for i in range(5):
  print(i)
# yeilds 0 1 2 3 4

# we go from 2 to 5 so we pass in those values, starting at 2 and going to 6 but not including 6
for i in range(2, 6):
  print(i)

# to go in reverse we pass in a 3rd value of -1 because we going backwards(decrement) or -2 to go by 2
# start at 5 and go down to 1 but not including 1 so stop at 2. -1 is the decrement amount
for i in range(5, 1, -1):
  print(i)

  # other languages have explicit loops, python is easier to type out
  for (int i = 0; i < n; i++)