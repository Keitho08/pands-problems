# Keith Brazill (G00387845)
# 17th February 2020

# Write a program that takes asks a user to input a string 
# and outputs every second letter in reverse order.

#This program takes a user input string (s) and
#outputs every second letter in reverse order.

s = input("Please enter a sentence: ")
# input: The quick brown fox jumps over the lazy dog.
print(s[::-2])
# output: .o zletrv pu o wr cu h

# Syntax: stringname[stringlength::-1]
# The string name is "s", we do not specify the string length
# as we want the full lenght we leave as follows [:]. :-2 specifies
# that we print from the end using only every second letter.
# In understanding this formula, the code was tested on these:
# print(s[:])
# print(s[::-1])
# to understand how these impacted the results. 

# References
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# https://docs.python.org/2/library/string.html
