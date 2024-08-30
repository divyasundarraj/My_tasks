#global variable
#local variable
#intance variable

#static/class variable:
#-this variable is declared inside the class and outside the method/constructor
#scope throughout the class
#class variable is accessed by the class name
#syntax:<class_name>.<class_variable_name>
#it is used for memory management
#shares the same memory
#class variable can be called class name/object name

class school:
    school_name = "Coder" #class/static variable

    def __init__(self,name,rno):
        self.name=name
        self.rno = rno
        
    def display(self):
        print(f"Hi{self.name} from{school.school_name},your rno is{self.rno}!")

print(school.school_name)
obj = school("bava",25)
obj.display()
print(obj.school_name)

obj1 = school("dhivya",21)
obj1.display()
print(obj1.school_name)
print(obj1.name)