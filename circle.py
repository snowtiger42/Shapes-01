import math

from shape import Shape


class Circle(Shape):

    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius

    # def set_name(self, name):
    #     self.__name = name

    def get_name(self):
        if self.__name is not "Circle":
            raise Exception("Wrong Name or data type")
        return self.__name

    def perimeter(self):
        if self.__name is not "Circle":
            raise Exception("Wrong Name or data type")
        return 2 * (math.pi * self.__radius)

    def area(self):
        if self.__name is not "Circle":
            raise Exception("Wrong Name or data type")
        return math.pi * self.__radius ** 2

    def draw(self):
        result = ""
        if self.__name is not "Circle":
            raise Exception("Wrong Name or data type")
        for shape in self.Shape:
            result = result + shape.__str__() + "\n"

        # result = ""
        # if self.__name is not "Circle":
        #     raise Exception("Wrong Name or data type")
        # for shape in self.Shape:
        #     return shape.draw() + "\n"


def testPerimeter():
    c1 = Circle("Circle", 2.5)
    print(c1.perimeter())


def testArea():
    c2 = Circle("Circle", 2.5)
    print(c2.area())

def testDraw():
    c3 = Circle("Circle", 2.5)
    print(c3.draw())


testPerimeter()
testArea()
testDraw()
