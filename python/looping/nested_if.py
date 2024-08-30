#Nested_if - (one if function inside of another)

m1 = 100
m2 = 200
m3 = 300
if(m1>m2):
    if(m1>m3):
        print("m1 is greater")
    else:
        print("m3 is greater")
else:
    if(m2<m3):
        print("m2 is greater")
    else:
        print("m3 is greater")