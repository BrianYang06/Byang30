#Returns the string with its first letter swapped with its last letter as long as the length is greater than 1
def front_back(str):
  if len(str) > 1:
   return str[len(str)-1] + str[1:len(str) -1] + str[0]
  else:
    return str

print("front_back('code'):",front_back('code'))
print("front_back('a'):",front_back('a'))
print("front_back('ab'):",front_back('ab'))
print("front_back('abc'):",front_back('abc'))
print("front_back(''):",front_back(''))
