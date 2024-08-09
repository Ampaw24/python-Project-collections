height  = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in kg"))
bmi = weight / height  * height

if bmi < 18.5:
    print("Your BMI is", bmi, "- You are underweight")
else:
    print(bmi)

