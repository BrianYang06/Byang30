def last2(str):
  x = str[len(str) - 2: len(str)]
  count = 0
  for i in range(len(str) - 2):
    if str[i: i+2] == x:
      count += 1
  return count
