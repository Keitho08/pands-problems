# Keith Brazill
# Check if a number is prime
# The primes are 2, 3, 5, 6, 11, 13, ...

p = 347 
m = 2

while m < p:
    if p % m == 0:
        print(m,"divides", p, "and therefore", p, "is not prime")
    m = m + 1
    