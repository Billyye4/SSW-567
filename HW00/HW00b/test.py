import unittest
from triangle import defineTriangle

class TestTriangle(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(defineTriangle(3, 3, 3), "Equilateral")

    def testIsosceles(self):
        self.assertEqual(defineTriangle(3, 3, 5), "Isosceles")

    def testScalene(self):
        self.assertEqual(defineTriangle(3, 4, 6), "Scalene")

    def testRightTriangle(self):
        self.assertEqual(defineTriangle(3, 4, 5), "Right Triangle")

    def testNotTriangle(self):
        self.assertEqual(defineTriangle(3, 0, 5), "Not a triangle")

if __name__ == '__main__':
    unittest.main()