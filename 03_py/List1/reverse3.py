def reverse3(nums):
  i = len(nums)
  list = []

  while i > 0:
    list.append(nums[i - 1])
    i -= 1
  return list


#I made a while loop that will add values from nums into a new list. The while loop will start at the last index.
#reverse3([3,5,8]) ----> [8,5,3]
#reverse3([4,3,8,5]) -----> [5,8,3,4]
