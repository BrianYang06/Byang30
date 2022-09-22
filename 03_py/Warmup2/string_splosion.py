#Using a for loop to create a "string splosion"
def string_splosion(str):
  x = ""
  for i in range(len(str) + 1):
    x += str[:i]
  return x

print("string_splosion('Code'):",string_splosion('Code'))
print("string_splosion('ab'):",string_splosion('ab'))
print("string_splosion('abc'):",string_splosion('abc'))
