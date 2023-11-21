class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")


class D(A):
    def __init__(self):
        super().__init__()
        print("D")


class E(D):
    def __init__(self):
        super().__init__()
        print("E")


c = C()
print("-------")
e = E()
e
