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

print('sum67([1, 2, 2]):',sum67([1, 2, 2]))
print('sum67([1, 2, 2, 6, 99, 99, 7]):',sum67([1, 2, 2, 6, 99, 99, 7]))
print('sum67([1, 1, 6, 7, 2]:',sum67([1, 1, 6, 7, 2]))
print('sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]):',sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
print('sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]):',sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
print('sum67([2, 7, 6, 2, 6, 7, 2, 7]):',sum67([2, 7, 6, 2, 6, 7, 2, 7]))
print('sum67([2, 7, 6, 2, 6, 2, 7]):',sum67([2, 7, 6, 2, 6, 2, 7]))
print('sum67([1, 6, 7, 7]):',sum67([1, 6, 7, 7]))
print('sum67([6, 7, 1, 6, 7, 7]):',sum67([6, 7, 1, 6, 7, 7]))
print('sum67([6, 8, 1, 6, 7]):',sum67([6, 8, 1, 6, 7]))
print('sum67([]):',sum67([]))
print('sum67([6, 7, 11]):',sum67([6, 7, 11]))
print('sum67([11, 6, 7, 11]):',sum67([11, 6, 7, 11]))
print('sum67([2, 2, 6, 7, 7]):',sum67([2, 2, 6, 7, 7]))
