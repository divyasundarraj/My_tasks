"""Python - popular language ,High level programming language
created Guido van Rossum and released in 1991
Uses:
1)Web development
2)software development
3)Mathematical calculation
4)system Scripting
#windows,mac,linux,raspberry
"""
#varibles:
a =10
even = 5
odd =1

#data types:
int,float,str,bool,complex,list,tuple,set,dict,None

#int
a =10
print(type(a))
#immutable,not iterable

#float 
a=50.5
print(type(a))
#immutable,not iterable

#string
name = "divya"
for i in name:
    print(i)
    print(type(name))
#mutable,iterable

#bool
num = True
#immutable,not iterable

#complex
comp = 3+4j
print(type(comp))
#immutable,not iterable

#list  [ ]
list = [1,2,3,4,"bava","divya",3+4j]
list[2] = 5
print(list)
print(type(list))
#mutable,iterable

#tuple  ( )
tuple = (1,2,3,4,"bava","divya")
for i in tuple:
    print(i)
    print(type(tuple))
#immutable,iterable

#set { }
set = {3,4,4.5,3+4j,"string"}
for i in set:
    print(i)
    print(type(set))
#mutable,iterable

#dict {key : value}
dict = {1:'one',2:'two',3:'three'}
for i in dict:
    print(i)
    print(type(dict))
#mutable,iterable

#none
language = None


#intendation - space