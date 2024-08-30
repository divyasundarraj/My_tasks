
#List---------------------------------------------------------------------------------------------------------

#Append()
name_lst = ["Divya","Priya","Shakthi","Ram"]
name_lst.append("Maha")
print(name_lst)

#insert()
Fruits = ["Apple","Orange","Mango","Banana"]
Fruits.insert(2,"Grapes")
print(Fruits)

#extend()
name_lst1 = ["Divya","Priya","Shakthi","Ram"]
name_lst2 = ["keerthi","Kaviya","Maha"]
name_lst1.extend(name_lst2)
print(name_lst1)

#pop()
name_lst = ["Divya","Priya","Shakthi","Ram"]
name_lst.pop(3)
print(name_lst)

#clear
name_lst = ["Divya","Priya","Shakthi","Ram"]
name_lst.clear()
print(name_lst)

#sort
lst = [9,6,5,7,4,3,1,2,8]
lst.sort()
print(lst)

#copy()
lst1 = [1,2,3,4,5]
lst2 = ['a','b','c','d']
lst1 = lst2.copy()
print(lst1)

#reverse()
lst = ['a','b','c','d']
lst.reverse()
print(lst)

#count()
lst = [1,2,1,4,5,1,8,7,1,5,1]
a = lst.count(1)
print(a)

#index()
name_lst = ["Divya","Priya","Shakthi","Ram"]
a = name_lst.index("Shakthi")
print(a)