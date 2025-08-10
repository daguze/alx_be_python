import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def __str__(self):
        return f"The area of the Rectangle is : {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius** 2

    def __str__(self):
        return f"The area of the Circle is : {self.area()}"