#USing if statements to check the hour and if the bird is talking to check if he's in trouble (true) or not (false)
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
  return False

print('parrot_trouble(True, 6):',parrot_trouble(True, 6))
print('parrot_trouble(True, 7):',parrot_trouble(True, 7))
print('parrot_trouble(False, 6):',parrot_trouble(False, 6))
print('parrot_trouble(True, 21):',parrot_trouble(True, 21))
print('parrot_trouble(False, 21):',parrot_trouble(False, 21))
