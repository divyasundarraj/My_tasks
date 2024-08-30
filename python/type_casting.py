
#Typecasting - one dataype can convert into another data type 
"""
int()
float()
str()
bool()
comp()
list()
set()
tuple()#not modify
dict()"""

#====================================INT============================================================
num =10
print("Int to Int:",int(num),"------------>",type(int(num)))
print("Int to float:",float(num),"------------>",type(float(num)))
print("Int to str:",str(num),"------------>",type(str(num)))
print("Int to bool:",bool(num),"------------>",type(bool(num)))
print("Int to comp:",complex(num),"------------>",type(complex(num)))

#====================================FLOAT============================================================
num = 100.8
print("Int to Int:",int(num),"------------>",type(int(num)))
print("float to float:",float(num),"------------>",type(float(num)))
print("float to str:",str(num),"------------>",type(str(num)))
print("float to bool:",bool(num),"------------>",bool(str(num)))
print("float to comp:",complex(num),"------------>",type(complex(num)))

#====================================STRING============================================================
name = "python"
#print("Int to Int:",int(name),"------------>",type(int(name)))
#print("float to float:",float(name),"------------>",type(float(name)))
print("str to str:",str(name),"------------>",type(str(name)))
print("str to bool:",bool(name),"------------>",bool(str(name)))
#print("str to comp:",complex(name),"------------>",type(complex(name)))


#====================================BOOL============================================================
human = True #True = 1, False = 0

print("bool to Int:",int(human),"------------>",type(int(human)))
print("bool to float:",float(human),"------------>",type(float(human)))
print("bool to str:",str(human),"------------>",type(str(human)))
print("bool to bool:",bool(human),"------------>",type(bool(human)))
print("bool to complex:",complex(human),"------------>",type(complex(human)))

#====================================complex============================================================
comp = 10 +5j

#print("comp to Int:",int(comp),"------------>",type(int(comp)))
#print("comp to float:",float(comp),"------------>",type(float(comp)))
print("comp to str:",str(comp),"------------>",type(str(comp)))
print("comp to bool:",bool(comp),"------------>",type(bool(comp)))
print("comp to complex:",complex(comp),"------------>",type(complex(comp)))

lst = [10,2,6,3,1,5,6,7,8,8,6] #6,8
print(lst)

unique = set(lst)
print("---------type",(unique)) #doesnt duplicate value only unique value

list1 = list(unique)
print("----------type",(list1))
