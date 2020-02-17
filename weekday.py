# Keith Brazill
# Computer and Programming Task 5 17.02.2020
# Task: Write a program that outputs whether or not today is a weekday.

import datetime #Imports "datetime". This a module for manipulating dates and times. 

weekday = datetime.datetime.today().weekday() 
#Class type. .today() returns the current local datetime. .weekday returns current
#day of the weeks as an integer. Monday = 0, Sunday = 6.

if weekday<5: #If the above code returns an integer <5 i.e. Monday(0) to Saturday (5), then it is a weekday.
    print("Yes, unfortunately today is a weekday.") # Prints string if weekday (0,1,2,3,4)
else:
    print("It is the weekend, yay!") #Prints string if weekend day (5,6)  