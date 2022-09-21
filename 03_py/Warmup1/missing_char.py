#using slices to remove the index of the letter from the string
def missing_char(str, n):
  return str[0:n] + str[n + 1:]
