# Keith Brazill
# Check if one number divides another.
# if (p % m) != 0:  (this means is not equal to 0) alternative
# to else.

p = 8 
m = 2

if (p % m) == 0:
    print(p, "divided by", m, "leaves a remainder of zero.")
    print("I'll be run too if the condition is True.")
else:
    print(p, "divided by", m, "does not leave a remainder of zero.")
    print("I'll be run too if the condition is False.")

print("I'll run no matter what.")