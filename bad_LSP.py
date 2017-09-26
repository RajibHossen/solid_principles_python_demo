

class Rectangle:

    def __init__(self):
        self.length = None
        self.width = None

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_area(self):
        return self.width*self.length


class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
        self.length = None
        self.width = None

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width


class AreaCalculator():
    def calculate_area(self, rectangle):
        return rectangle.width*rectangle.length


rectangle = Rectangle()
rectangle.set_length(5)
rectangle.set_width(6)
area_calculator = AreaCalculator()
print area_calculator.calculate_area(rectangle)

square = Square()
square.set_length(5)
square.set_width(5)
print area_calculator.calculate_area(square)


