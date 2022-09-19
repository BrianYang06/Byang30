def string_splosion(str):
  x = ""
  for i in range(len(str) + 1):
    x += str[:i]
  return x
