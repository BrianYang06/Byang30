#Using if statements to check if the string contains a 'not' at the start and adding a not if the string doesn't contain it
def not_string(str):
  if len(str) > 2 and str[0:3] == 'not':
    return str
  else:
    return 'not ' + str
