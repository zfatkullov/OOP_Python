class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")
        #super().hello()

class C(A):
    def hello(self):
        print("C")
        super().hello()

class D(C, B):
    def hello(self):
        print("D")
        super().hello()

#   1. class D -> class B -> class C -> class A -> object
#   D().hello() вывод: D B C A
#   2. class D -> class C -> class B -> class A -> object
#   D().hello() вывод D C B A

print(D.__mro__)