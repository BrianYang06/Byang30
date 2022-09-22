def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False


#I created a for loop that checks if nums contain 2 or 3
# has23([5,3,7,5,9]) ----> True
# has23([7,5,8,4,3,1]) ----> True
# has23([7,6,5,0,0,7,5]) ----> False
