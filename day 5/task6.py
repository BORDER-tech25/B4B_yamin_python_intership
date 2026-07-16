class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()


rect1 = Rectangle(4, 6)
rect2 = Rectangle(3, 8)

print("Rectangle 1 Area:", rect1.area())
print("Rectangle 2 Area:", rect2.area())
print("Are they equal?", rect1 == rect2)

