import abc


class Shape(metaclass=abc.ABCMeta):

    def __init__(self, name: str) -> None:
        self._name = name

    @abc.abstractmethod
    def area(self):
        """
       Calculate the area of the shape.

       Returns:
       (float): the area of the shape.
       """
        # raise NotImplementedError
        pass

    @abc.abstractmethod
    def perimeter(self):
        """
       Calculate the perimeter of the shape.

       Returns:
       (float): the perimeter of the shape.
       """
        # raise NotImplementedError
        pass

    @abc.abstractmethod
    def draw(self):
        pass
        # return "I am a " + self._name + "my area is: " + Shape.area() + " and my perimeter is " + Shape.perimeter()
