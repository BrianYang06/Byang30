#Using an if statement to determine if string is longer or equal to 3 and then using a for loop to duplicate the first few letters
def front3(str):
  if len(str) >= 3:
    str = str[0:3]
    for i in range(2):
      str += str[0:3]
  else:
    x = len(str)
    for i in range(2):
      str += str[0:x]

  return str
