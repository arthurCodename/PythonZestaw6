import math
import unittest

class Point:
#     """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(' + str(self.x) +', '+str(self.y)+')'

    def __repr__(self):
        return 'Point('+str(self.x)+', '+str(self.y)+')'

    def __eq__(self, other: object):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object):
        return not self.x == other.x or self.y == other.y

    def __add__(self, other: object):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object):
        return Point(other.x - self.x, other.y - self.y)
    
    def __mul__(self, other: object):
        return self.x * other.x + self.y * other.y

    def __cross__(self, other: object): 
        return abs(self.x * other.y - self.y * other.x)

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __hash__(self): 
        return hash(self.x, self.y)

class TestPoint(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(Point.__str__(Point(1,2)), '(1, 2)')

    def test__repr__(self):
        self.assertEqual(Point.__repr__(Point(1,2)), 'Point(1, 2)')

    def test__eq__(self):
        self.assertEqual(Point.__eq__(Point(1,2), Point(1, 2) ), True)

    def test__ne__(self):
        self.assertEqual(Point.__ne__(Point(1, 2), Point(3, 4)), True)
    
    def test__add__(self):
        self.assertEqual(Point.__add__(Point(1,2), Point(3,4)), Point(4,6))

    def test__sub__(self):
        self.assertEqual(Point.__sub__(Point(1,2), Point(5,6)), Point(4, 4))

    def test__mul__(self):
        self.assertEqual(Point.__mul__(Point(1,2), Point(3,4)), 11)

    def test__cross(self):
        self.assertEqual(Point.__cross__(Point(1, 2), Point(3,4)), 2)

    def test__length(self):
        self.assertEqual(Point.length(Point(1,2)), math.sqrt(5) )

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()

