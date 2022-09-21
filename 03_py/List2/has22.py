#Using a while loop that loops one number in the list short to check if the current value is 2 and if the next value is also true
def has22(nums):
  i = 0
  while i < len(nums) - 1:
    if nums[i] == 2 and nums[i+1] == 2:
      return True
    i += 1
  return False
