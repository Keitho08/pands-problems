# Keith Brazill (G00387845)
# 17th of February 2020

# Write a program that outputs whether or not today is a weekday.

import datetime #Imports "datetime". This a module for manipulating dates and times. 

weekday = datetime.datetime.today().weekday() 
#Class type. .today() returns the current local datetime. .weekday returns current
#day of the weeks as an integer. Monday = 0, Sunday = 6.

if weekday<5: #If the above code returns an integer <5 i.e. Monday(0) to Saturday (5), then it is a weekday.
    print("Yes, unfortunately today is a weekday.") # Prints string if weekday (0,1,2,3,4)
else:
    print("It is the weekend, yay!") #Prints string if weekend day (5,6)  

# References
# https://pythontic.com/datetime/date/weekday
# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# https://docs.python.org/3/library/datetime.html
