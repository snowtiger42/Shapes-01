from shape import Shape


class Rectangle(Shape):

    def __init__(self, name, width, height):
        self.__name = name
        self.__width = width
        self.__height = height

    # def set_name(self, name):
    #     self.__name = name

    def get_name(self):
        if self.__name is not "Rectangle":
            raise Exception ("Wrong Name or data type")
        return self.__name

    def perimeter(self):
        if self.__name is not "Rectangle":
            raise Exception ("Wrong Name or data type")
        return 2 * (self.__width + self.__height)

    def area(self):
        if self.__name is not "Rectangle":
            raise Exception ("Wrong Name or data type")
        return self.__width * self.__height

    def draw(self):
            result = ""
            if self.__name is not "Rectangle":
                raise Exception("Wrong Name or data type")
            for shape in self.Shape:
                result = result + shape.__str__() + "\n"


def testPerimeter():
    r1 = Rectangle("Rectangle", 2.5, 5)
    print(r1.perimeter())


def testArea():
    r2 = Rectangle("Rectangle", 2.5, 5)
    print(r2.area())


testPerimeter()
testArea()

