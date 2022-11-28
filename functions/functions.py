# Functions in python are straightforward we use the def keyword
# we name the function and pass in some parameters and then use a colon after the declaration
# the body of the function  comes after the colon and is indented
def myFunc(n, m):
  return n * m

print(myFunc(3, 4))
# yeild 12

# One functinality used alot in interviews is nested functions
# Nested functions have access to the outer  variables
# this is really helpful in recursive problems
# if you have an outer function that takes in some parameters and you also declare some values in that outer function
# the inner function will have access to all of those variables by default
# so if we call the inner function we dont have to pass in a b and c
# (see graphs)

def outer(a, b):
  c = "c"

  def inner():
    return a + b + c
  return inner()

print(outer("a", "b"))
#yeilds abc

# One gotcha is you can modify objects but not reassign values
# unless using nonlocal keyword
def double(arr, val):
  def helper():
    #modifying array works
    for i, n in enumerate(arr):
      arr[i] *= 2

    # will only modify val in the helper scope
    # val *= 2

    # this will modify val outside the helper scope
    nonlocal val
    val *= 2
  helper()
  print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)
# we see that each variable was doubled
# yeilds [2, 4] 6