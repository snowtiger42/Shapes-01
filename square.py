from shape import Shape


class Square(Shape):
    def __init__(self, name, side_length):
        self.__name = name
        self.__side_length = side_length


    # def set_name(self, name):
    #     self.__name = name

    def get_name(self):
        if self.__name is not "Square":
            raise Exception("Wrong Name or data type")
        return self.__name

    def perimeter(self):
        if self.__name is not "Square":
            raise Exception("Wrong Name or data type")
        return 4 * self.__side_length

    def area(self):
        if self.__name is not "Square":
            raise Exception("Wrong Name or data type")
        return self.__side_length * self.__side_length

    def draw(self):
        if self.__name is not "Square":
            raise Exception("Wrong Name or data type")

        return "I am a " + self.__name + "my area is: " + Square.area(self) + " and my perimeter is " \
               + Square.perimeter(self)

        # result = ""
        # if self.__name is not "Square":
        #     raise Exception("Wrong Name or data type")
        # for shape in self.Shape:
        #     result = result + shape.__str__() + "\n"


def testPerimeter():
    S1 = Square("Square", 2.5)
    print(S1.perimeter())


def testArea():
    S2 = Square("Square", 2.5)
    print(S2.area())

def testDraw():
    s3 = Square("Square", 2.5)
    print(s3.draw())


testPerimeter()
testArea()
testDraw()
