#Using a while loop that loops one number in the list short to check if the current value is 2 and if the next value is also true
def has22(nums):
  i = 0
  while i < len(nums) - 1:
    if nums[i] == 2 and nums[i+1] == 2:
      return True
    i += 1
  return False

print('has22([1, 2, 2]):',has22([1, 2, 2]))
print('has22([1, 2, 1, 2]):',has22([1, 2, 1, 2]))
print('has22([2, 1, 2]):',has22([2, 1, 2]))
print('has22([2, 2, 1, 2]):',has22([2, 2, 1, 2]))
print('has22([1, 3, 2]):',has22([1, 3, 2]))
print('has22([1, 3, 2, 2]):',has22([1, 3, 2, 2]))
print('has22([2, 3, 2, 2]):',has22([2, 3, 2, 2]))
print('has22([4, 2, 4, 2, 2, 5]):',has22([4, 2, 4, 2, 2, 5]))
print('has22([1, 2]):',has22([1, 2]))
print('has22([2, 2]):',has22([2, 2]))
print('has22([2]):',has22([2]))
print('has22([]):',has22([]))
print('has22([3, 3, 2, 2]):',has22([3, 3, 2, 2]))
print('has22([5, 2, 5, 2]):',has22([5, 2, 5, 2]))
