#function with return type and without return type


#without return type
def addition():
    no1=int(input("Enter the number1: "))
    no2=int(input("Enter the number2: " ))
    add = no1+no2
    print("Addition:",add)

#with return type
def Multiplication():
    no1=int(input("Enter the number1: "))
    no2=int(input("Enter the number2: " ))
    mul = no1*no2
    return mul #return keyword used
data1 = Multiplication() #object
print(data1)
