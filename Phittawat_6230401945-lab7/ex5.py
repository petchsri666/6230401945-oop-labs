import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = math.pi * (math.pow(self.radius, 2))
        return f"The circle with radius {self.radius} has the area as {self.area:.2f}"

    def perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return f"  and the perimeter as {self.perimeter:.2f}"


if __name__ == '__main__':
    print(Circle(3).area())
    print(Circle(3).perimeter())
    print(Circle(4).area())
    print(Circle(4).perimeter())