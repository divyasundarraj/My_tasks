#single Inheritance:
#Single Parent Class and Single Child class


class Dad:                    #parent class
    def flat(self):         
        print("flat")

    def car(self):
        print("car")

    def bike(self):
        print("bike")
class Son(Dad):              #child class
    def bike(self):
        super().bike()    #immediate parent class
        print("Son's Bike")

    def mobile(self):
        print("mobile")

son = Son()
son.bike()
son.mobile()
son.car()
son.flat()