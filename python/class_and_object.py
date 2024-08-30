#oops - object oriented programming language

#class &object
#class - an outline for creating a new object(is the blueprint(planning))
#object - it is the instance of the class

#method
     #are the function which are define inside the class
     #every function defined inside the class must have the self keyword as a parameter

#self
    #keyword
    #it represents object of the class

#instance variable
#are those variable which are define inside the methods/contructor
#it is created by using self keyword as prefix ex:self.<variable_name>
#scope:throughout the class

#syntax:
"""class <class_name>:
    class_body"""

class building:  #class is created

    def bricks(self,no_of_bricks=9000): #self ==>keyword
        print(f"{no_of_bricks}bricks!")

    def door(self):
        self.no_of_doors= 10 #instance variable
        return f"{10} doors"
    
    def window(self):
        print(self.no_of_doors)
        print("40 windows")

obj = building() #object is created #syntax:<class_name() #It is default constructor
obj.bricks()
data=obj.bricks()
data=obj.door()
print(data)



