#Using a for loop we count the number of times a length 2 substring appears in the two strings
def string_match(a, b):
  ans = 0
  x = min(len(a), len(b))
  for i in range(x - 1):
    if b[i:i+2] == a[i:i+2]:
      ans += 1
  return ans

print("string_match('xxcaazz', 'xxbaaz'):",string_match('xxcaazz', 'xxbaaz'))
print("string_match('abc', 'axc'):",string_match('abc', 'axc'))
print("string_match('abc', 'abc'):",string_match('abc', 'abc'))
