from __future__ import annotations
import sys, os
import unittest

os.chdir(os.path.dirname(__file__))
path_to_shapes = os.path.abspath("../")
sys.path.append(path_to_shapes)

from rectangle import Rectangle
from circle import Circle
from cube import Cube
from sphere import Sphere

class TestShape(unittest.TestCase):

    def setUp(self):
        self.x = 1
        self.y = 2
        self.side1 = 1
        self.side2 = 2
        self.radius = 1

    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, self.radius)

    def create_rectangle(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.side1, self.side2)

    def create_cube(self) -> Cube:
        return Cube(self.x, self.y, self.side1, self.side2)

    def create_sphere(self) -> Sphere:
        return Sphere(self.x, self.y, self.radius)


    #Test empty shapes
    def create_empty_circle(self):
        with self.assertRaises(ValueError):
            cir = Circle()
    def create_empty_rectangle(self):
        with self.assertRaises(ValueError):
            rect = Rectangle()
    def create_empty_cube(self):
        with self.assertRaises(ValueError):
            cu = Cube()
    def create_empty_sphere(self):
        sp = Circle
        with self.assertRaises(ValueError):
            sp


    #Test circle
    def test_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,1)
        self.assertEqual(c1,c2)

    def test_not_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,2)
        self.assertNotEqual(c1,c2)

    def test_circle_translate(self):
        c1 = self.create_circle()
        self.assertEqual(c1.translate_circle(1,1), Circle(self.x +1, self.y + 1, self.radius))
        
    def test_less_than_or_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,2)
        self.assertLessEqual(c1,c2)

    def test_less_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,2)
        self.assertLess(c1,c2)

    def test_greater_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,0.2)
        self.assertGreater(c1,c2)
    def test_greater_or_equal_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3,2,0.2)
        self.assertGreater(c1,c2)

    #test circle against other shapes
    def test_circle_with_rectangle(self):
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(cir, rect)

    def test_circle_with_cube(self):
        cir = self.create_circle()
        cube = self.create_cube()
        self.assertNotEqual(cir, cube)

    def test_circle_with_sphere(self):
        cir = self.create_circle()
        sphere = self.create_sphere()
        self.assertNotEqual(cir, sphere)

    
    #test rectangle
    def test_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,2)
        self.assertEqual(r1,r2)

    def test_not_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,3)
        self.assertNotEqual(r1,r2)

    def test_less_than_or_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,4)
        self.assertLessEqual(r1,r2)

    def test_less_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,4)
        self.assertLess(r1,r2)

    def test_greater_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,1.2)
        self.assertGreater(r1,r2)

    def test_greater_or_equal_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1,2,1,1.3)
        self.assertGreater(r1,r2)

    #test rectangle against other shapes
       #test circle against other shapes
    def test_rectangle_with_circle(self):
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(rect, cir)

    def test_rectangle_with_cube(self):
        rect = self.create_rectangle()
        cube = self.create_cube()
        self.assertNotEqual(rect, cube)

    def test_rectangle_with_sphere(self):
        rect = self.create_rectangle()
        sphere = self.create_sphere()
        self.assertNotEqual(rect, sphere)

    #test cube
    def test_equal_cube(self):
        c1 = self.create_cube()
        c2 = Cube(2,2,1,2)
        self.assertEqual(c1,c2)

    def test_not_equal_cube(self):
        c1 = self.create_cube()
        c2 = Cube(2,3,2,1)
        self.assertNotEqual(c1,c2)

    def test_less_than_or_equal_cube(self):
        c1 = self.create_cube()
        c2 = Cube(1,2,1,4)
        self.assertLessEqual(c1,c2)

    def test_less_than_cube(self):
        c1 = self.create_rectangle()
        c2 = Rectangle(1,2,1,4)
        self.assertLess(c1,c2)

    def test_greater_than_cube(self):
        c1 = self.create_rectangle()
        c2 = Rectangle(1,2,1,1.5)
        self.assertGreater(c1,c2)

    def test_greater_or_equal_than_cube(self):
        c1 = self.create_rectangle()
        c2 = Rectangle(1,2,1,1.9)
        self.assertGreater(c1,c2)

    #test cube against other shapes
    def test_cube_with_rectangle(self):
        cube = self.create_cube()
        rect = self.create_rectangle()
        self.assertNotEqual(cube, rect)

    def test_cube_with_circle(self):
        cir = self.create_circle()
        cube = self.create_cube()
        self.assertNotEqual(cube, cir)

    def test_cube_with_sphere(self):
        cube = self.create_cube()
        sphere = self.create_sphere()
        self.assertNotEqual(cube, sphere)

       #Test sphere
    def test_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3,2,1)
        self.assertEqual(s1,s2)

    def test_not_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Circle(3,2,2)
        self.assertNotEqual(s1,s2)

    def test_sphere_translate(self):
        s1 = self.create_sphere()
        self.assertEqual(s1.translate_circle(1,1), Circle(self.x +1, self.y + 1, self.radius))

    def test_less_than_or_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Circle(3,2,2)
        self.assertLessEqual(s1,s2)

    def test_less_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Circle(3,2,2)
        self.assertLess(s1,s2)

    def test_greater_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Circle(3,2,0.2)
        self.assertGreater(s1,s2)

    def test_greater_or_equal_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Circle(3,2,0.2)
        self.assertGreater(s1,s2)


if __name__ == "__main__":
    unittest.main()