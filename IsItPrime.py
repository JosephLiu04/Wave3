def prime(x):
  prime_numbers=[]
  for y in range(2,x):
    if x % y == 0:
      prime_numbers.append(y)
  if len(prime_numbers) > 1:
    return False
  else:
    return True


