#if statements to determine if we're sleeping in by looking at if its a weekday or we're on vacation
def sleep_in(weekday, vacation):
  if not weekday:
    return True
  else:
    return vacation

print('sleep_in(False, False):',sleep_in(False, False))
print('sleep_in(True, False):',sleep_in(True, False))
print('sleep_in(False, True):',sleep_in(False, True))
print('sleep_in(True, True):',sleep_in(True, True))
