class Student:
    def __init__(self, color):
        self.school = "abc high school"
        self.obj = self.Laptop(color)

    def show(self):
        print(self.school, end=" , laptop color: ")
        print(self.obj.color, end=" , laptop brand: ")
        print(self.obj.brand)

    class Laptop:
        def __init__(self, color):
            self.color = color
            self.brand = "HP"


s1 = Student("white")
s1.show()
