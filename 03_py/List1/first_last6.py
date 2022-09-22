def first_last6(nums):
  return nums[0] == 6 or nums[len(nums) - 1] == 6

  #You don't need to use an if statement since you are just checking the first and last value.
  #The single return statement is sufficient in checking whether either the first of the last index is equal to 6

  #Test cases:
  #first_last6([5,3,2,6]) -----> True
  #first_last6([6,6]) -----> True
  #first_last6([5,5,6,7]) -----> False
