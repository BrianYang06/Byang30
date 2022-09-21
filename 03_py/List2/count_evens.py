def count_evens(nums):
  a = 0
  for i in nums:
    if i % 2 == 0:
      a+=1
  return a
