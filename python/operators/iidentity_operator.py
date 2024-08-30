
#identity operator

#is - returns True if both the variables referring to the same object
#is not - returns True if both the variables are not referring to the same object

no_1 = int(input("Enter the number1: "))
no_2 = int(input("Enter the number2: "))
#is
is_demo = no_1 is no_2
print("Is demo:",is_demo)

#is_not
is_not_demo = no_1 is not no_2
print("Is not demo:",is_not_demo)
