#using remove() to remove the largest and smallest function and then find the average of the rest
def centered_average(nums):
  nums.remove(min(nums))
  total =0
  nums.remove(max(nums))
  for i in nums:
    total += i
  return total/(len(nums))
