# if statements dont need parenthese
# of curly braces, we use indentation (tab and a colon that goes after the conditional)
n = 1
if n > 2:
     n -= 1

# 'else if' works a bit differently elif is the keyword
elif n == 2:
  n *= 2    
# keyword for else
else:     
  n += 2

  # parenthesis are needed  for multi line conditions

  # logic
  # the keywords 'and', 'or' are used in python instead of double ampersand and double pipe

  # and = &&
  # or = ||

  # example:
  
  n, m = 1, 2
  if ((n > 2 and 
       n != m) or n == m):
       n += 1
