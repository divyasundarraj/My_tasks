
#logical operator
'''
and - it will returns only if all the mentioned conditions are true
or - it will returns any one of conditions are true
not - it will returns the reverse of the actual result
'''

num_1 = int(input("Enter the number1: "))
num_2 = int(input("Enter the number2: "))
num_3 = int(input("Enter the number2: "))

#and operator
and_demo = num_1 == num_2 and num_1 > num_3
print("and:",and_demo)

#or operator
or_demo = num_1 == num_2 or num_1 > num_3
print("or:",or_demo)

#not operator
not_demo = not(num_1==num_2)
print("not:",not_demo)
