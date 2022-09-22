#Using if statements to determin if a or b is negative/postive or if negative is true then if a and b are negative
def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
  elif (a > 0 and b < 0) or (a < 0  and b > 0):
    return True
  return False

print('pos_neg(1, -1, False):',pos_neg(1, -1, False))
print('pos_neg(-1, 1, False):',pos_neg(-1, 1, False))
print('pos_neg(-4, -5, True):',pos_neg(-4, -5, True))
print('pos_neg(-4, -5, False):',pos_neg(-4, -5, False))
print('pos_neg(-4, 5, False):',pos_neg(-4, 5, False))
