#multiple Inheritance
#Multiple parent class and single child class

class c_lang:
    def procedural_feature(self):
        print("procedural_feature")

    def language(self):
        print("C language")

class cpp_lang:
    def oops_feature(self):
        print("OOPS feature")

    def language(self):
        print("Cpp language")

class python(cpp_lang,c_lang):
    def both_feature(self):
        print("Both procedural aand OPPS language")

    
    def language(self):
        print("Python language")


obj = python()
obj.procedural_feature()
obj.oops_feature()
obj.both_feature()
obj.language()