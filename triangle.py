#create a triangle with three variable side_1, side_2,side_3. it also has the variable angle_1,angle_2 and angle_3. initialize the variable with construction. create a class  equi_latteral trangle with cal_area() function. find the tangent of all angles using final_angle() method.
import math


class Triangle:
    def __init__(self, side_1, side_2, side_3, angle_1, angle_2, angle_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.angle_1 = angle_1
        self.angle_2 = angle_2
        self.angle_3 = angle_3


class EquilateralTriangle(Triangle):
    def cal_area(self):
        area = (math.sqrt(3) / 4) * self.side_1 ** 2
        print("Area of Equilateral Triangle =", round(area))

    def final_angle(self):
        print("Tangent of Angle 1 =", math.tan(math.radians(self.angle_1)))
        print("Tangent of Angle 2 =", math.tan(math.radians(self.angle_2)))
        print("Tangent of Angle 3 =", math.tan(math.radians(self.angle_3)))


class Scalene(Triangle):
    def cal_parameter(self):
        parameter = self.side_1 + self.side_2 + self.side_3
        print("Parameter of Triangle =", parameter)

    def cal_area(self):
        s = (self.side_1 + self.side_2 + self.side_3) / 2
        area = math.sqrt(
            s * (s - self.side_1) *
            (s - self.side_2) *
            (s - self.side_3)
        )
        print("Area of Scalene Triangle =", round(area))



e = EquilateralTriangle(6, 6, 6, 60, 60, 60)

e.cal_area()
e.final_angle()



s = Scalene(5, 6, 7, 40, 60, 80)

s.cal_parameter()
s.cal_area()