#Using if statements to check if a is equal to b resulting in multiplying the number by 4 and if not then return the sum of the variables
def sum_double(a, b):
  if a == b:
    return 4*a
  else:
    return a + b

print('sum_double(1, 2):',sum_double(1, 2))
print('sum_double(3, 2):',sum_double(3, 2))
print('sum_double(2, 2):',sum_double(2, 2))
print('sum_double(-1, 0):',sum_double(-1, 0))
print('sum_double(3, 3):',sum_double(3, 3))
