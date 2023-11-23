number1 = int(input("Enter A number \n"))
number2 = int(input("Enter another number \n"))

def getMax(x,y):
    if x > y:
        print("Value ", x ,"is Greater")
    else:
        print("Value ", y , " is greater")

getMax(number1,number2)