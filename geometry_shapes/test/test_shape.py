from __future__ import annotations
import sys, os
import unittest
import math
from unittest.case import _AssertRaisesContext

os.chdir(os.path.dirname(__file__))
path_to_shapes = os.path.abspath("../")
sys.path.append(path_to_shapes)

from rectangle import Rectangle
from circle import Circle
from cuboid import Cuboid
from sphere import Sphere


class TestShape(unittest.TestCase):
    def setUp(self):
        self.x = 1
        self.y = 2
        self.side1 = 1
        self.side2 = 2
        self.side3 = 2
        self.radius = 1

    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, self.radius)

    def create_rectangle(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.side1, self.side2)

    def create_cuboid(self) -> Cuboid:
        return Cuboid(self.x, self.y, self.side1, self.side2, self.side3)

    def create_sphere(self) -> Sphere:
        return Sphere(self.x, self.y, self.radius)

    # Test empty shapes
    def create_empty_circle(self):
        with self.assertRaises(ValueError):
            cir = Circle()

    def create_empty_rectangle(self):
        with self.assertRaises(ValueError):
            rect = Rectangle()

    def create_empty_cuboid(self):
        with self.assertRaises(ValueError):
            cu = Cuboid()

    def create_empty_sphere(self):
        sp = Circle
        with self.assertRaises(ValueError):
            sp

    # test areas of shapes
    def test_circle_area(self):
        cir = self.create_circle()
        area = math.pi * self.radius**2
        self.assertAlmostEqual(cir.area, area)

    def test_rectangle_area(self):
        rect = self.create_rectangle()
        area = self.side1 * self.side2
        self.assertEqual(rect.area, area)

    def test_cuboid_area(self):
        cube = self.create_cuboid()
        area = 2 * (
            (self.side3 * self.side2)
            + (self.side2 * self.side1)
            + (self.side1 * self.side3)
        )

        self.assertEqual(cube.area, area)

    def test_sphere_area(self):
        sphere = self.create_sphere()
        area = 4 * math.pi * self.radius**2
        self.assertTrue(sphere.area, area)

    # test if new shape is inside current shape
    def test_inside_circle(self):
        cir = self.create_circle()
        points = [[1.2, 2.4], [1, 2.2], [1.5, 1.5]]
        for point in points:
            self.assertTrue(cir.is_inside(point[0], point[1]))
        self.assertTrue(cir.is_inside(1.2, 2.4))

        points_ = [[0.1, 0.1], [0.5, 0.5], [0, 0]]
        for point in points_:
            self.assertFalse(cir.is_inside(point[0], point[1]))

    # Test circle
    def test_unit_circle(self):
        c1 = self.create_circle()
        # test that its true for a unit circle
        self.assertTrue(c1.is_unit_circle())

        c2 = Circle(1, 1, 2)
        # test that its false for a non unit circle
        self.assertFalse(c2.is_unit_circle())

    def test_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(1, 2, 1)
        self.assertEqual(c1, c2)

    def test_not_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertNotEqual(c1, c2)

    def test_circle_translate(self):
        c1 = self.create_circle()
        c1.translate(1, 1)
        c3 = Circle(2, 3, 1)
        self.assertEqual(c1.midPoint, c3.midPoint)

    def test_less_than_or_equal_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertLessEqual(c1, c2)

    def test_less_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertLess(c1, c2)

    def test_greater_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3, 2, 0.2)
        self.assertGreater(c1, c2)

    def test_greater_or_equal_than_circle(self):
        c1 = self.create_circle()
        c2 = Circle(3, 2, 0.2)
        self.assertGreater(c1, c2)

    # test circle against other shapes
    def test_circle_with_rectangle(self):
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(cir, rect)

    def test_circle_with_cube(self):
        cir = self.create_circle()
        cube = self.create_cuboid()
        self.assertNotEqual(cir, cube)

    def test_circle_with_sphere(self):
        cir = self.create_circle()
        sphere = self.create_sphere()
        self.assertNotEqual(cir, sphere)

    # test rectangle
    def test_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 2)
        self.assertEqual(r1, r2)

    def test_not_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 3)
        self.assertNotEqual(r1, r2)

    def test_less_than_or_equal_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 4)
        self.assertLessEqual(r1, r2)

    def test_less_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 4)
        self.assertLess(r1, r2)

    def test_greater_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 1.2)
        self.assertGreater(r1, r2)

    def test_greater_or_equal_than_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 1.3)
        self.assertGreater(r1, r2)

    def test_if_shape_is_rectangle_or_square(self):
        r1 = self.create_rectangle()
        self.assertFalse(r1.is_square())

        r2 = Rectangle(0, 0, 2, 2)
        self.assertTrue(r2.is_square())

    def test_if_rectangle_created(self):
        r1 = self.create_rectangle()
        self.assertTrue(r1.validate_rectangle())

    def test_area_rectangle(self):
        r1 = self.create_rectangle()
        area = self.side1 * self.side2
        self.assertEqual(r1.area, area)

    def test_circumference_rectangle(self):
        r1 = self.create_rectangle()
        circumference = (self.side1 * 2) + (self.side2 * 2)
        self.assertEqual(r1.circumference, circumference)

    def test_inside_rectangle(self):
        r1 = self.create_rectangle()
        self.assertTrue(r1.is_inside(1.5, 2))

        # assert false if point is outside
        self.assertFalse(r1.is_inside(1, 4))

    # test rectangle against other shapes
    def test_rectangle_with_circle(self):
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(rect, cir)

    def test_rectangle_with_cube(self):
        rect = self.create_rectangle()
        cube = self.create_cuboid()
        self.assertNotEqual(rect, cube)

    def test_rectangle_with_sphere(self):
        rect = self.create_rectangle()
        sphere = self.create_sphere()
        self.assertNotEqual(rect, sphere)

    # test cuboid

    def test_equal_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(2, 2, 1, 2, 2)
        self.assertEqual(c1, c2)

    def test_not_equal_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(2, 3, 2, 1, 5)
        self.assertNotEqual(c1, c2)

    def test_less_than_or_equal_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 4, 1)
        self.assertLessEqual(c1, c2)

    def test_less_than_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 4,2)
        self.assertLess(c1, c2)

    def test_greater_than_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 1.5,1)
        self.assertGreater(c1, c2)

    def test_greater_or_equal_than_cuboid(self):
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 1.9, 1)
        self.assertGreater(c1, c2)

    # test cube against other shapes
    def test_cube_with_rectangle(self):
        cube = self.create_cuboid()
        rect = self.create_rectangle()
        self.assertNotEqual(cube, rect)

    def test_cube_with_circle(self):
        cir = self.create_circle()
        cube = self.create_cuboid()
        self.assertNotEqual(cube, cir)

    def test_cube_with_sphere(self):
        cube = self.create_cuboid()
        sphere = self.create_sphere()
        self.assertNotEqual(cube, sphere)

    # Test sphere
    def test_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 1)
        self.assertEqual(s1, s2)

    def test_not_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertNotEqual(s1, s2)

    def test_sphere_translate(self):
        s1 = self.create_sphere()
        s1.translate(1, 1)
        s2 = Sphere(2, 3, 1)
        self.assertEqual(s1.midPoint, s2.midPoint)

    def test_less_than_or_equal_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertLessEqual(s1, s2)

    def test_less_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertLess(s1, s2)

    def test_greater_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 0.2)
        self.assertGreater(s1, s2)

    def test_greater_or_equal_than_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 0.2)
        self.assertGreater(s1, s2)

    # test sphere volume
    def test_sphere_volume(self):
        s1 = self.create_sphere()
        volume = (4 / 3) * math.pi * self.radius**3
        self.assertEqual(s1.volume, volume)


if __name__ == "__main__":
    unittest.main()
