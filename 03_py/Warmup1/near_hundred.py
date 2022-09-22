#Using absolute value function and an if statement to determine if n is close to 100 or 200
def near_hundred(n):
  if abs(100 - n) < 11 or abs(200-n) < 11:
    return True
  else:
    return False

print('near_hundred(93):',near_hundred(93))
print('near_hundred(90):',near_hundred(90))
print('near_hundred(89):',near_hundred(89))
print('near_hundred(110):',near_hundred(110))
print('near_hundred(111):',near_hundred(111))
