#Using a for loop and boolean to track if it should be added together or not
def sum67(nums):
  count = True
  total = 0
  for i in nums:
    if i == 6:
      count = False
    if count == True:
      total += i
    if i == 7:
      count = True

  return total
