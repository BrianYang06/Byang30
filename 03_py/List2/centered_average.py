def centered_average(nums):
  nums.remove(min(nums))
  total =0
  nums.remove(max(nums))
  for i in nums:
    total += i
  return total/(len(nums))
