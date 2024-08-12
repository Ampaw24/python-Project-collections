def addition(number1,number2):
    print(number1 + number2)

def bmCalculator(height,weight):
    bmi = weight / (height/100) ** 2
    return bmi

myBmi = bmCalculator(30,50)
print(myBmi)


addition(10,4)
addition(12,4)