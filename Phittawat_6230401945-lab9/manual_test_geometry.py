from geometry import area
from geometry import shape

circle1 = shape.Circle("blue", 3)
print(f"Circle with radius {circle1.radius} has area as "
      f"{round(area.get_circle_area(circle1.radius), 2)}")

rect1 = shape.Rectangle("green", 3, 4)
print(f"Rectangle with width {rect1.width} and height {rect1.height} "
      f"has area as {round(area.get_rectangle_area(rect1.width, rect1.height), 2)}")
