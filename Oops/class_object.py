class Computer:
    def __init__(self):  # __init__ is a constructor
        print("hello")

    def ram(self, name):
        print("It has 8 gb ram"+name)


comp1 = Computer()
comp1.ram(" Animesh")
Computer.ram(comp1, " Lohar")
print("i love you")

# ----------------------------


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        print("my height is : " + height + " and my weight is: " + weight)

    def update(self, update_weight):
        self.weight = update_weight

    def get_height(self):  # getters or get method
        return self.height

    def set_weight(self, value):
        self.weight = value
        return self.weight


person1 = Person("7cm", "50kg")
person1
person1.update(60)
print("Updated weight is: " + str(person1.weight))

# ----------------------------


class Car:
    name_of_shop = "sexy"  # class variable or it's called static variable

    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color
        # instance variable or it's called object variable
        self.name_of_owner = "Animesh Lohar"

    def test(self):
        print("This car's brand is: " + self.brand_name +
              " and color is : " + self.color)

    @classmethod
    def changeShopName(cls):
        return cls.name_of_shop

    @staticmethod
    def pleaseUse():
        print("FUCK YOU !!!")


car1 = Car("XUV", "Red")
car1.test()
print("Name of shop is: " + car1.name_of_shop)
print("Name of owner is: " + car1.name_of_owner)
print(car1.changeShopName())

# all objects keep in heap memory

# Pointers : all objects are kept in heap memory
print(id(comp1))
print(id(person1))
print(id(car1))
