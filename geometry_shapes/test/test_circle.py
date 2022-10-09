from __future__ import annotations
import sys, os
import unittest

os.chdir(os.path.dirname(__file__))
path_to_circle_module = os.path.abspath("../")
sys.path.append(path_to_circle_module)

from circle import Circle
from rectangle import Rectangle

class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.radius = 1, 2, 3

    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, self.radius)

    def test_circle(self):
        ci = self.create_circle()
        self.assertEqual((ci.x, ci.y, ci.radius), (self.x, self.y, self.radius))

    def test_equal_circles(self):
        circle1 = self.create_circle()
        circle2 = Circle(1, 2, 4)
        self.assertEqual(circle1, circle2)


if __name__ == "__main__":
    unittest.main()
