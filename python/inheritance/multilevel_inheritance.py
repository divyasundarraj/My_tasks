
class grandpa:
    def field(self):
        print("field")
    
class dad(grandpa):
    def flat(self):
        print("flat")

    def bike(self):
        print("bike")
class son(dad):
    def mobile(self):
        print("mobile")

obj = son()
obj.mobile()
obj.field()
obj.bike()
obj.flat()



    
