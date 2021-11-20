from shape import Shape


class Triangle(Shape):
    def __init__(self, name, base, height, length1, length2, length3):
        self.__name = name
        self.__base = base
        self.__height = height
        self.__length1 = length1
        self.__length2 = length2
        self.__length3 = length3

    # def set_name(self, name):
    #     self.__name = name

    def get_name(self):
        if self.__name is not "Triangle":
            raise Exception("Wrong Name or data type")
        return self.__name

    def perimeter(self):
        if self.__name is not "Triangle":
            raise Exception("Wrong Name or data type")
        return self.__length1 + self.__length2 + self.__length3

    def area(self):
        if self.__name is not "Triangle":
            raise Exception("Wrong Name or data type")
        return (self.__base * self.__height) / 2

    def draw(self):
            result = ""
            if self.__name is not "Triangle":
                raise Exception("Wrong Name or data type")
            for shape in self.Shape:
                result = result + shape.__str__() + "\n"

def testPerimeter():
    t1 = Triangle("Triangle", 5, 4, 3, 5, 2.5)
    print(t1.perimeter())

def testArea():
    t2 = Triangle("Triangle", 5, 4, 3, 5, 2.5)
    print(t2.area())

testPerimeter()
testArea()

