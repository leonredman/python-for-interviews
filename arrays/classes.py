# Class
class MyClass:
  # Constructor is basically keywords  "def, double underscore, init, double underscore"
  # "self" is passed into every method of a class, its basically like the this keyword in other languages
  # in this case our constructor is maybe taking in a list of numbers "nums"
  def __init__(self, nums):
    # To Create member variables we also use the self keyword
    self.nums = nums   # we create a member variable called nums and assign it the nums that were passed in from constructor 
    self.size = len(nums) # we can also create a member variable for the size of nums and assign it the lenght of the parameter
       
    # We can create a method for this class "getLength" we dont want to pass in params but we have to pass in the self keyword
    #  self key word required as param always
    # gives us access to our member variable keyword so we can return self.size
  def getLength(self):
    return self.size

# to call a member function we can do that with the self keyword
  def getDoubleLength(self):
    return 2 * self.getLength()
