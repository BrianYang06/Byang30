def make_ends(nums):
  list = []
  list.append(nums[0])
  list.append(nums[len(nums) - 1])
  return list


#I created an empty list and I appended the first and then the last index values to it.
# nums([3,26,4,3,2]) ----> [3,2]
# nums([6,7,8,0,4]) ----> [6,4]
