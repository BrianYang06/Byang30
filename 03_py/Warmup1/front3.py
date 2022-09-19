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
