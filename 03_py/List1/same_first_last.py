def same_first_last(nums):
  if len(nums) >= 1:
    return nums[0] == nums[len(nums) - 1]
  else:
    return False

#There is an if statement to make sure that there is at least two values in the list or else you wouldn't be able to compare it
#same_first_last([0]) -----> False
#same_first_last([0,5]) -----> False
#same_first_last([0,5,6,3,3,0]) -----> True
