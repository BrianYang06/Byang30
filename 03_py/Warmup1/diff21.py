#Using if functions to determine if n is less than 21 and using that if statement to determine the return value
def diff21(n):
  if n < 21:
    return abs((n-21))
  else:
    return abs(2*(n-21))

print('diff21(19):',diff21(19))
print('diff21(10):',diff21(10))
print('diff21(21):',diff21(21))
print('diff21(22):',diff21(22))
print('diff21(25):',diff21(25))
