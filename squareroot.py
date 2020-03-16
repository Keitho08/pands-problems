# Keith Brazill (G00387845)
# 16th March 2020

# Write a program that takes a positive floating-point number as input and 
# outputs an approximation of its square root. 
# You should create a function called sqrt that does this.

#Example:   Please enter a positive number: 14.5
#           The square root of 14.5 is approx. 3.8.

# number of iterations to run (line 10), I found out this needs to be a large no. to get a good approximation. 
# A lower value can result in wrong answer, e.g 1 iteration returns 7.8 as answer for 14.5 which is incorrect. 

def newton_method(number, number_iters = 100000):
    a = float(number) # number to get square root of
    for i in range(number_iters): # number of iterations to run, I found out this needs to be a large no. to get a good approximation. A lower value can result in wrong answer, e.g 1 iteration returns 7.8 as answer for 14.5.
        number = 0.5 * (number + a / number) # formula to run newton method as per references below. 
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number
 
n =  float(input("Enter positve no.: "))        # Number = input integer in the string
if n < 0:                                       # If n is less than 0 print "Please enter a positive number"
    print("Please enter a positive number")     # This prevents user entering negative number
else:
    Sqrt = (newton_method(n))                   # If user enter positive number, the newton method to find square root is applied.
    print(round(Sqrt,1))                        # The answer is rounded to one decimal place as per example provided in lecture. 

#References

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# https://gist.github.com/Akaame/0da597d785e2c210cd951b6e7c9e9193
# https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# https://www.youtube.com/watch?v=1uN8cBGVpfs 
# https://en.wikipedia.org/wiki/Newton%27s_method
# For this task I also referred to my code collatz.py code as re-using and modifying some of the function's
# in the collatz code saved some time and efficiency on this task. 