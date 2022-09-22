#Comapare boolean values to determine if both monkeys are smiling
def monkey_trouble(a_smile, b_smile):
  return a_smile==b_smile

print('monkey_trouble(True, True):',monkey_trouble(True, True))
print('monkey_trouble(False, False):',monkey_trouble(False, False))
print('monkey_trouble(True, False):',monkey_trouble(True, False))
print('monkey_trouble(False, True):',monkey_trouble(False, True))
