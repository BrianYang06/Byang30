def rotate_left3(nums):
  i = 1
  list = []
  last = nums[0]
  while i < len(nums):
    if i == len(nums) - 1:
      list.append(nums[i])
    elif i != 0:
      list.append(nums[i])

    i += 1
  list.append(last)
  return list


#A while loop is used to add 1 index ahead of values in nums. The first index will be added at the very end
#rotate_left3([3,4,2]) -----> [4,2,3]
#rotate_left3([35,6,2]) -----> [6,2,35]
