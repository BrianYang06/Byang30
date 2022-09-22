#Returns the boolean value of if a or b equals to 10 or if sum of both is equal to 10
def makes10(a, b):
  return a == 10 or b == 10 or (a + b) == 10

print("makes10(9, 10):",makes10(9, 10))
print("makes10(9, 9):",makes10(9, 9))
print("makes10(1, 9):",makes10(1, 9))
print("makes10(10, 1):",makes10(10, 1))
print("makes10(10, 10):",makes10(10, 10))
