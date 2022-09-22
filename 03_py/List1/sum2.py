def sum2(nums):
  if len(nums) < 2:
    if len(nums) == 0:
      return 0
    else:
      return nums[0]
  else:
    return nums[0] + nums[1]



#The first 2 if statements will check if there are two values in nums. If it passes those if statements, then it will return the sum of first two values.
#sum2([5]) ----> 5
#sum2([5,7,8]) -----> 12
#sum2([]) ------> 0
