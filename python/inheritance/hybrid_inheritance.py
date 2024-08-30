
#Hybrid Inheritance
#Its a combination of all types of Inheritance

class A:
    def a(self):
        print("a")

class B(A):
    def b(self):
        print("b")

class C(A):
    def c(self):
        print("c")

class D(C):
    def d(self):
        print("d")

class E(C):
    def e(self):
        print("e")

class F(D,E):
    def f(self):
        print("f")


obj = B()
obj.a()

obj1 = C()
obj.a()

obj2 = D()
obj2.c()

obj3 = E()
obj3.c()


obj4 = F()
obj4.d()
obj4.e()
