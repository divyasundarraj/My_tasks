

#Hirarichical Inheritance
#single parend and multiple child classes

class Country:
    def region(self):
        print("region")

class India(Country):
    def language(self):
        print("Hindi")

class USA(Country):
    def language(self):
        print("language")

obj = India()
obj.region()
obj.language()

obj = USA()
obj.region()
obj.language()