#This program calculates BMI
#based on user weight and height input

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_cm_to_m = height/100

BMI = weight / (height_cm_to_m **2)
print('BMI is: {:.2f}'.format(BMI))