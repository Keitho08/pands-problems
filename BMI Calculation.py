#This program calculates BMI
#based on user weight and height input

weight = float(input("enter weight in kg: "))
height = float(input("enter height in cm: "))

BMI = (weight/((height/100)**2))

print("Your BMI is", BMI)