class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self._x, self._y)

    def distance(self, other):
        changex = self._x - other._x
        changey = self._y - other._y
        return (changex ** 2 + changey ** 2) ** (1 / 2)

    def measure(self,other):
        measure1 = self._x**2 + self._y**2
        measure2 = other._x**2 + other._y**2
        return f"measurepoint1: {measure1},measurepoint2: {measure2}"









point1=Point(3,4)
point2=Point(5,6)
a=point1.distance(point2)
b=point1.measure(point2)
print(a)
