#Using if functions to determine if n is less than 21 and using that if statement to determine the return value
def diff21(n):
  if n < 21:
    return abs((n-21))
  else:
    return abs(2*(n-21))
