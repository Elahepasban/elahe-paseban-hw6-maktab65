class Square:
    def __init__(self, side):
        self.side = side
        self.s = 0
        self.a = 0

    def surrounding(self):
        self.s = self.side * 4
        return self.s

    def area(self):
        self.a = self.side * self.side
        return self.a

    def __repr__(self):
        return f" Square surrounding: {self.s} , Square area: {self.a}"


class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        self.s = 0
        self.a = 0

    def surrounding(self):
        self.s = (self.width + self.lenght) * 2
        return self.s

    def area(self):
        self.a = self.width * self.lenght
        return self.a

    def __repr__(self):
        return f" Rectangle surrounding: {self.s} , Rectangle area: {self.a}"


class Righttriangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height
        self.s = 0
        self.a = 0
        self.hypotenuse = 0

    def surrounding(self):
        self.hypotenuse = (self.side ** 2 + self.height ** 2) ** (1 / 2)
        self.s = self.side + self.height + self.hypotenuse
        return self.s

    def area(self):
        self.a = self.side * self.height / 2
        return self.a

    def __repr__(self):
        return f" Righttriangle surrounding: {self.s} , Righttriangle area: {self.a}"


s1 = Square(4)
s1.area()
s1.surrounding()
print(s1.__repr__())

s2 = Rectangle(5,4)
s2.area()
s2.surrounding()
print(s2.__repr__())

s3 = Righttriangle(3,6)
s3.area()
s3.surrounding()
print(s3.__repr__())