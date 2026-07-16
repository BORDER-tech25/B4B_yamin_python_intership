class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(5, 10)
p2 = Point(5, 10)
p3 = Point(2, 8)

print(p1)
print("p1 == p2 :", p1 == p2)
print("p1 == p3 :", p1 == p3)
