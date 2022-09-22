#Using a for loop that increments 2 to create a "string bit"
def string_bits(str):
  x = ""
  for i in range(0,len(str),2):
    x += str[i]
  return x

print("string_bits('Hello'):",string_bits('Hello'))
print("string_bits('Heeololeo'):",string_bits('Heeololeo'))
print("string_bits('Hi'):",string_bits('Hi'))
