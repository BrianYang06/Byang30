#USing if statements to check the hour and if the bird is talking to check if he's in trouble (true) or not (false)
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
  return False
