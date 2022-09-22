#Using a for loop to add str to a string n times
def string_times(str, n):
  x = ""
  for i in range(n):
    x += str
  return x

print("string_times('Hi', 2):",string_times('Hi', 2))
print("string_times('Hi', 3):",string_times('Hi', 3))
print("string_times('Hi', 1):",string_times('Hi', 1))
