# Keith Brazill
# Check if a number is prime
# The primes are 2, 3, 5, 6, 11, 13, ...

p = 221
m = 2
isprime = True

while m < p:
    if p % m == 0:
      #  print(m,"divides", p, "and therefore", p, "is not prime")
      isprime = False
      break 
    m = m + 1

if isprime:
    print(p, "is a prime number.")
else:
    print(p, "is not prime.")