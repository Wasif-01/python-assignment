#create a class shape with variable radius . initialize the variable with constructor. create a class circle which is the child of shape class.   define a method cal_area() to calculate the area of circle using math packege.  create a class sphere which is a child of shape slass. define cal_volume() to calculate the volume of the sphere...
import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def cal_area(self):
        area = math.pi * self.radius * self.radius
        print("Area of Circle =", area)


class Sphere(Shape):
    def cal_volume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        print("Volume of Sphere =", volume)
7
r = float(input("Enter radius: "))

c = Circle(r)
c.cal_area()

s = Sphere(r)
s.cal_volume()