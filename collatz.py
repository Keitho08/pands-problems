# Keith Brazill(G00387845)
# 6th February 2020

# Write a program that asks the user to input any positive integer and outputs the successive 
# values of the following calculation. At each step calculate the next value by taking the 
# current value and, if it is even, divide it by two, but if it is odd, multiply it by three 
# and add one. Have the program end if the current value is one.

n = int(input("Input positive number: "))      # Number = input integer in the string

def collatz(n):                                # defines the function "collatz(number is the parameter)"
    if n % 2 == 0:                             # if remainder of number divided by 2 is 0 it is even
        return n//2                            # returns result to the function
    else:                                      # or else if number divided by 2 is not = 0
        return 3*n + 1                         # return result to sequence

if n > 0:   	                                # Checks number is greater than 0
    while n != 1:                               # keep running while n is not equal to 1
        print(n)                                # print n (prints number each time until n = 1)
        n = collatz(n)                          # the collatz function is applied to n (number inputted)
else:                                           # Or else if the "if" statement fails the except catches the value error to prevent program crashing
    print("Please enter a positive number!")    # If value error the message is displayed.

# References
# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# https://automatetheboringstuff.com/chapter3/
# https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
