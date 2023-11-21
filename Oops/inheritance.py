class A:
    def __init__(self):
        print("tum 1")

    def show(self):
        print("I Love You")


class B(A):  # child class
    def __init__(self):
        print("tum 2")

    def show(self):
        print("I Love You 2")


class C:
    def __init__(self):
        print("tum 3")

    def show3(self):
        print("I LOVE YOU 3")


class D(A, C):  # Multiple inheritance
    def __init__(self):
        print("tum 4")

    def show4(self):
        print("I Love You 4")


a = A()
b = B()
# b.show()
d = D()
d.show()
