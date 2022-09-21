#Using a while loop to add all the numbers up except when theres a 13
def sum13(nums):
  i = 0
  total = 0
  while i < len(nums):
    if nums[i] == 13:
      i+= 2
    else:
      total += nums[i]
      i+=1
  return total

print('sum13([1, 2, 2, 1]):',sum13([1, 2, 2, 1]))
print('sum13([1, 1]):',sum13([1, 1]))
print('sum13([1, 2, 2, 1, 13]):',sum13([1, 2, 2, 1, 13]))
print('sum13([1, 2, 13, 2, 1, 13]):',sum13([1, 2, 13, 2, 1, 13]))
print('sum13([13, 1, 2, 13, 2, 1, 13]):',sum13([13, 1, 2, 13, 2, 1, 13]))
print('sum13([]):',sum13([]))
print('sum13([13]):',sum13([13]))
print('sum13([13, 13]):',sum13([13, 13]))
print('sum13([13, 0, 13]):',sum13([13, 0, 13]))
print('sum13([13, 1, 13]):',sum13([13, 1, 13]))
print('sum13([5, 7, 2]):',sum13([5, 7, 2]))
print('sum13([5, 13, 2]):',sum13([5, 13, 2]))
print('sum13([0]):',sum13([0]))
print('sum13([13, 0]):',sum13([13, 0]))
