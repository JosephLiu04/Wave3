def prime(x):
  prime_numbers=[]
  for y in range(2,x):
    if x % y == 0:
      prime_numbers.append(y)
  if len(prime_numbers) > 1:
    return False
  else:
    return True

def main():
  number = int(input("What is your number?"))
  if prime(number) == True:
    print("Your number is prime")
  else:
    print("Your number is composite")
