#Types of constructor
#default constructor - default constructor if no constructor is defined.
#zero constructor - constructor without any parameter
#parameterized constructor - constructor with parameter

class constructor:
    def __init__(self,name,rno): #parameterized constructor
        self.name =  name
        self.rno = rno
    
    def display(self):
        print(f"Name:{self.name},Rno:{self.rno}")

obj = constructor("Bava",18)
obj.display()
obj = constructor("Dhivya",15)
obj.display()


#zero constructor
class contructor:
    def __init__(self): #constructor
        print("constructor")   #zero constructor




    