#Using a for loop to loop over string to check how many times the last 2 index substring appears in the string
def last2(str):
  x = str[len(str) - 2: len(str)]
  count = 0
  for i in range(len(str) - 2):
    if str[i: i+2] == x:
      count += 1
  return count

print("last2('hixxhi'):",last2('hixxhi'))
print("last2('xaxxaxaxx'):",last2('xaxxaxaxx'))
print("last2('axxxaaxx'):",last2('axxxaaxx'))
