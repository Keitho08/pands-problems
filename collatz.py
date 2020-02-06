# Keith Brazill
# Computer and Programming Task 4 06.02.2020

# Write a program that asks the user to input any positive integer and outputs the successive 
# values of the following calculation. At each step calculate the next value by taking the 
# current value and, if it is even, divide it by two, but if it is odd, multiply it by three 
# and add one. Have the program end if the current value is one.

def collatz(number):                                # defines the function "collatz(number is the parameter)"
    if number % 2 == 0:                             # if remainder of number divided by 2 is 0 it is even
        return number//2                            # returns result to the function
    else:                                           # or else if number divided by 2 is not = 0
        return 3*number + 1                         # return result to sequence
try:                                                # try below code
    n = int(input("Input positive number: "))       # Number = input integer in the string
    while n != 1:                                   # keep running while n is not equal to 1
        n = collatz(n)                              # the collatz function is applied to n (number inputted)
        print(n)                                    # print n (prints number each time until n = 1)

except ValueError:                                  # If the try block of code fails the except catches the value error to prevent program crashing
    print("Please enter a positive number!")        # If value error the message is displayed.