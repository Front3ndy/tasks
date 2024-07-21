from math import pi
from math import sqrt


class Figure:

    def __init__(self, color='red'):
        self.color = color

    def change_color(self, new):
        self.color = new
        return new


class Circle(Figure):

    def __init__(self, radius:(float, int)):
        self.radius = radius

    def calculate_area(self):
        return round(pi, 2) * self.radius ** 2

    def calculate_area_with_pi(self):
        return f'{self.radius**2}pi'


class Triangle(Figure):

    def __init__(self, a:(float, int), b:(float, int), c:(float, int)):
        if all(i == True for i in [a+b>c, a+c>b, b+c>a]) and all(i > 0 for i in [a, b, c]):
            self.a = a
            self.b = b
            self.c = c
            self.flag = True
        else:
            self.flag = False

    def calculate_area(self):
        if self.flag:
            p = (self.a + self.b + self.c) / 2
            return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 3)
        else:
            return 'Does not exist'

    @property
    def is_right(self):
        if self.flag:
            bigger = max(self.a, self.b, self.c)
            small = min(self.a, self.b, self.c)
            mid = self.a + self.b + self.c - bigger - small
            return bigger**2 == mid**2 + small**2
        else:
            return 'Does not exist'



if __name__ == '__main__':
    circle = Circle(3)
    print(circle.calculate_area())
    print(circle.calculate_area_with_pi())

    print('*' * 30)

    tr = Triangle(7, 24, 25)
    print(tr.calculate_area())
    print(tr.is_right)
