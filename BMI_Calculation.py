# Keith Brazill (G00387845)
# 22nd January 2020

# Write a program that calculates somebody's Body Mass Index (BMI). 
# The inputs are the person's height in centimetres and weight in kilog
# The output is their weight divided by their height in metres squared.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
height_cm_to_m = height/100
BMI = weight / (height_cm_to_m **2)
print('BMI is {:.2f}.'.format(BMI)) 
#Syntax: {[argument_index_or_keyword]:[width][.precision][type]}

#User is prompted to enter height and weight as a float 
# (real number i.e. 1.0) number. The users weight is divided
# by the height in metres to the power of 2. The output
# is printed to the screen. The code "{:.2f}'.format(BMI)" 
# specifies the format of the string. "2f" represents a floating
# point number to a precision of 2 decimal places. ".format BMI" 
# specifies the output is from the BMI function.

# References
# https://thepythonguru.com/python-string-formatting/
# https://docs.python.org/2/library/string.html
# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
# https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
# https://bmicalculatorireland.com/
