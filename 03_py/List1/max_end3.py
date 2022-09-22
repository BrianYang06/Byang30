def max_end3(nums):
  bigger = nums[0]
  if nums[0] < nums[len(nums) - 1]:
    bigger = nums[len(nums) - 1]



  i = 0

  while i < len(nums):
    nums[i] = bigger
    i += 1



  return nums


#I made an if statement that checks if the first index is bigger than the last. A while loop will replace every value with the bigger of the two values.
#max_end3([2,4,5,73,4]) ----> [4,4,4,4,4]
#max_end3([7,4,3,2,4,6]) -----> [7,7,7,7,7,7]
