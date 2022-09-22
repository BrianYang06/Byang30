#using slices to remove the index of the letter from the string
def missing_char(str, n):
  return str[0:n] + str[n + 1:]

print("missing_char('kitten', 1):",missing_char('kitten', 1))
print("missing_char('kitten', 0):",missing_char('kitten', 0))
print("missing_char('kitten', 4):",missing_char('kitten', 4))
print("missing_char('Hi', 0):",missing_char('Hi', 0))
print("missing_char('Hi', 1):",missing_char('Hi', 1))
