#Using if statements to check if the string contains a 'not' at the start and adding a not if the string doesn't contain it
def not_string(str):
  if len(str) > 2 and str[0:3] == 'not':
    return str
  else:
    return 'not ' + str

print("not_string('candy'):",not_string('candy'))
print("not_string('x'):",not_string('x'))
print("not_string('not bad'):",not_string('not bad'))
print("not_string('bad'):",not_string('bad'))
print("not_string('not'):",not_string('not'))
