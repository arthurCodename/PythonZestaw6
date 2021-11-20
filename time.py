class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)
 
    def __str__(self):
        h = self // 3600
        sec = self - h*3600
        m = sec // 60
        sec = sec - m*60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        return "Time({0})".format(self)

    def __add__(self, other:object):
        return Time(self.s + other.s)

    def __cmp__(self, other: object):
        if self.s > other.s:
            return 1
        elif self.s == other.s:
            return 0
        else: 
            return -1

    def __eq__(self, other: object):
        return self.s == other.s

    def __ne__(self, other:object):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    def __gt__(self, other):
       return self.s > other.s

    def __ge__(self, other):
       return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return int(self.s)


import unittest

class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):     # test str() i repr()
        self.assertEqual(Time.__str__(5693), '01:34:53')
        self.assertEqual(Time.__repr__(5), 'Time(5)')

    def test_cmp(self):
        # Trzeba sprawdzać ==, !=, >, >=, <, <=.
        self.assertTrue(Time.__eq__(Time(2), Time(2)))
        self.assertFalse(Time.__eq__(Time(3), Time(2)))
        self.assertTrue(Time.__ne__(Time(3), Time(4)))
        self.assertFalse(Time.__ne__(Time(3), Time(3)))
        self.assertTrue(Time.__le__(Time(2), Time(3)))
        self.assertFalse(Time.__le__(Time(4), Time(3)))
        self.assertTrue(Time.__gt__(Time(4), Time(3)))
        self.assertFalse(Time.__gt__(Time(2), Time(3)))
        self.assertTrue(Time.__ge__(Time(4), Time(3)))
        self.assertFalse(Time.__ge__(Time(2), Time(3)))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Time.__add__(Time(1),Time(2)), Time(3))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main() 
    