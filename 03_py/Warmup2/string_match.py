def string_match(a, b):
  ans = 0
  x = min(len(a), len(b))
  for i in range(x - 1):
    if b[i:i+2] == a[i:i+2]:
      ans += 1
  return ans
