# 1) Duck typing
# 2) Operator Overloading
# 3) Method Overloading
# 4) Method Overriding
# Polymorphism : means one thing behavior like many things

# DUCK Typing
class Program:
    def execute(self):
        print("Compiling")
        print("Running")


class Program2:
    def execute(self):
        print("No error")
        print("Compiling")
        print("Running")


class Main:
    def show(self, ide):
        ide.execute()


p = Program()
main = Main()
main.show(p)

# Operator Overloading

a = 1
b = 2

print(a + b)
print(int.__add__(a, b))

c = "a"
d = "b"

print(c + d)
print(str.__add__(c, d))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = (self.m1 + other.m1) / 2
        m2 = (self.m2 + other.m2) / 2

        obj = Student(m1, m2)
        return obj

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if (r1 > r2):
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)


s1 = Student(70, 90)
s2 = Student(80, 82)

s3 = s1 + s2
print(s3.m1, s3.m2)

if s1 > s2:
    print("s1 got higher marks")
else:
    print("s2 got higher marks")


a = 9
print(a.__str__())

print(s1)

# METHOD Overloading

