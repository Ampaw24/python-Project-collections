height = float(input("what is your height? (in meters)"))

weight = float(input("what is your weight? (in kg)"))

bmi = (weight / (height * height))

bmirounded = round(bmi,2)

if bmirounded < 18.5:
    print("you are underweight")
elif bmirounded >= 18.5 and bmirounded <= 24.9:
    print("Hurray you have a normal weight")



