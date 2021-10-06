# Author: Ryan (AMDG) 10/6/21
# weight in kg height in m

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = weight / (height ** 2)
if bmi < 19:
    print("you are underweight")
elif bmi < 25:
    print("you are healthy")
elif bmi < 30:
    print("you are overweight")
elif bmi < 40:
    print("you are obese")
elif bmi >= 40:
    print("you are extremely obese")
