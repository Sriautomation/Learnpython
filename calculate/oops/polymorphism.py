#multiple inheritance
class A:
    def f1(self):
        print("f1 called")
    def f2(self):
        print("f2 called")

class B(A):
    def f3(self):
        print("f3 called")
    def f4(self):
        print("f4 called")

#multilevel inheritance
class C:
    def f4(self):
        print("f4 called")
    def f5(self):
        print("f5 called")

class D:
    def f6(self):
        print("f6 called")
    def f7(self):
        print("f7 called")

class E(C,D):
    def f8(self):
        print("f8 called")

obj1 = A()
obj2 = B()

obj2.f2()

obj3 = E()
obj3.f5()


