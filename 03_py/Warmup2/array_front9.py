#Using a for loop to loop through the first 4 elements and an if statement to check if one is a 9
def array_front9(nums):
  for i in range(4):
    if  i < len(nums) and nums[i] == 9:
      return True
  return False

print('array_front9([1, 2, 9, 3, 4]):',array_front9([1, 2, 9, 3, 4]))
print('array_front9([1, 2, 3, 4, 9]):',array_front9([1, 2, 3, 4, 9]))
print('array_front9([1, 2, 3, 4, 5]):',array_front9([1, 2, 3, 4, 5]))
