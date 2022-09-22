#Takes the string a slices it and then using a for loop to concat to a string the first 3 letters n times
def front_times(str, n):
  str = str[0:3]
  x = ""
  for i in range(n):
    x += str
  return x

print("front_times('Chocolate', 2):",front_times('Chocolate', 2))
print("front_times('Chocolate', 3):",front_times('Chocolate', 3))
print("front_times('Abc', 3):",front_times('Abc', 3))
