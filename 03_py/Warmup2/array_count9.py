#Using a foor loop to increment 'ans' to count the number of 9s in a list
def array_count9(nums):
  ans = 0
  for x in nums:
    if x == 9:
      ans +=1
  return ans

print('array_count9([1, 2, 9]):',array_count9([1, 2, 9]))
print('array_count9([1, 9, 9]):',array_count9([1, 9, 9]))
print('array_count9([1, 9, 9, 3, 9]):',array_count9([1, 9, 9, 3, 9]))
