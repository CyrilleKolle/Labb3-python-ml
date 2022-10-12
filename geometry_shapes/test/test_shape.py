from __future__ import annotations
import sys, os
import unittest
import math

os.chdir(os.path.dirname(__file__))
path_to_shapes = os.path.abspath("../")
sys.path.append(path_to_shapes)

from rectangle import Rectangle
from circle import Circle
from cuboid import Cuboid
from sphere import Sphere


class TestShape(unittest.TestCase):
    def setUp(self):
        """Function used used to set up variables to be used during testing. Ensures consistency."""
        self.x = 1
        self.y = 2
        self.side1 = 1
        self.side2 = 2
        self.side3 = 2
        self.radius = 1

    # create all test shapes

    def create_circle(self) -> Circle:
        """create test circle shape"""
        return Circle(self.x, self.y, self.radius)

    def create_rectangle(self) -> Rectangle:
        """create test rectangle shape"""
        return Rectangle(self.x, self.y, self.side1, self.side2)

    def create_cuboid(self) -> Cuboid:
        """create test cuboid shape"""
        return Cuboid(self.x, self.y, self.side1, self.side2, self.side3)

    def create_sphere(self) -> Sphere:
        """create test sphere shape"""
        return Sphere(self.x, self.y, self.radius)

    # test areas of shapes
    def test_circle_area(self):
        """test area of circle.
        ----------
        AssertEqual will check if circle's area locally calculated will return same value as circle's area property
        """
        cir = self.create_circle()
        area = math.pi * self.radius**2
        self.assertEqual(cir.area, area)

    def test_rectangle_area(self):
        """test area of rectangle.
        ----------
        AssertEqual will check if rectangle's area locally calculated will return same value as rectangle's area property
        """
        rect = self.create_rectangle()
        area = self.side1 * self.side2
        self.assertEqual(rect.area, area)

    def test_cuboid_area(self):
        """test area of cuboid.
        ----------
        AssertEqual will check if cuboid's area locally calculated will return same value as cuboid's area property
        """
        cube = self.create_cuboid()
        area = 2 * (
            (self.side3 * self.side2)
            + (self.side2 * self.side1)
            + (self.side1 * self.side3)
        )

        self.assertEqual(cube.area, area)

    def test_sphere_area(self):
        """test area of sphere.
        ----------
        AssertEqual will check if sphere's area locally calculated will return same value as sphere's area property
        """
        sphere = self.create_sphere()
        area = 4 * math.pi * self.radius**2
        self.assertTrue(sphere.area, area)

    # test if new shape is inside current shape
    def test_inside_circle(self):
        """Test if given points are inside Circle. The asserts both false and true possibilities"""

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
        """Test if circle is a unit circle by returning assertTrue if point is inisde and assertFalse if point is outside"""
        c1 = self.create_circle()
        # test that its true for a unit circle
        self.assertTrue(c1.is_unit_circle())

        c2 = Circle(1, 1, 2)
        # test that its false for a non unit circle
        self.assertFalse(c2.is_unit_circle())

    def test_equal_circle(self):
        """Test if current circle is equal to another circle"""
        c1 = self.create_circle()
        c2 = Circle(1, 2, 1)
        self.assertEqual(c1, c2)

    def test_not_equal_circle(self):
        """Test if current is not equal to another circle"""
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertNotEqual(c1, c2)

    def test_circle_translate(self):
        """Test if circle will translate (move) by given points"""
        c1 = self.create_circle()
        c1.translate(1, 1)
        c3 = Circle(2, 3, 1)
        self.assertEqual(c1.midPoint, c3.midPoint)

    def test_less_than_or_equal_circle(self):
        """Test if current circle is less than or equal to another circle"""
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertLessEqual(c1, c2)

    def test_less_than_circle(self):
        """Test if current is less than another circle"""
        c1 = self.create_circle()
        c2 = Circle(3, 2, 2)
        self.assertLess(c1, c2)

    def test_greater_than_circle(self):
        """Test if current circle is greater than another circle"""
        c1 = self.create_circle()
        c2 = Circle(3, 2, 0.2)
        self.assertGreater(c1, c2)

    def test_greater_or_equal_than_circle(self):
        """ "Test if current circle is greater than or equal to another circle"""
        c1 = self.create_circle()
        c2 = Circle(3, 2, 0.2)
        self.assertGreater(c1, c2)

    # test circle against other shapes
    def test_circle_with_rectangle(self):
        """Test circle against a rectangle"""
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(cir, rect)

    def test_circle_with_cuboid(self):
        """Test circle against a cuboid"""
        cir = self.create_circle()
        cube = self.create_cuboid()
        self.assertNotEqual(cir, cube)

    def test_circle_with_sphere(self):
        """Test circle against a sphere"""
        cir = self.create_circle()
        sphere = self.create_sphere()
        self.assertNotEqual(cir, sphere)

    # test rectangle
    def test_equal_rectangle(self):
        """Test if two same rectangle instances are same"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 2)
        self.assertEqual(r1, r2)

    def test_not_equal_rectangle(self):
        """Test if two rectangle instances are not thesame"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 3)
        self.assertNotEqual(r1, r2)

    def test_less_than_or_equal_rectangle(self):
        """Test if rectangle is less than or equal to another rectangle"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 4)
        self.assertLessEqual(r1, r2)

    def test_less_than_rectangle(self):
        """Test if rectangle is less than another rectangle"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 4)
        self.assertLess(r1, r2)

    def test_greater_than_rectangle(self):
        """Test if rectangle is greater than another rectangle"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 1.2)
        self.assertGreater(r1, r2)

    def test_greater_or_equal_than_rectangle(self):
        """Test if rectangle is greater than or equal to another rectangle"""
        r1 = self.create_rectangle()
        r2 = Rectangle(1, 2, 1, 1.3)
        self.assertGreater(r1, r2)

    def test_if_shape_is_rectangle_or_square(self):
        """Test that a rectangle is not a square"""
        r1 = self.create_rectangle()
        self.assertFalse(r1.is_square())

        """Test that rectangle created should have been a square"""
        r2 = Rectangle(0, 0, 2, 2)
        self.assertTrue(r2.is_square())

    def test_if_rectangle_created(self):
        """Test that its a rectangle created"""
        r1 = self.create_rectangle()
        self.assertTrue(r1.validate_rectangle())

    def test_area_rectangle(self):
        """Test area of rectangle"""
        r1 = self.create_rectangle()
        area = self.side1 * self.side2
        self.assertEqual(r1.area, area)

    def test_circumference_rectangle(self):
        """Test circumference of rectangle"""
        r1 = self.create_rectangle()
        circumference = (self.side1 * 2) + (self.side2 * 2)
        self.assertEqual(r1.circumference, circumference)

    def test_inside_rectangle(self):
        """Test if points are inside rectamngle"""
        r1 = self.create_rectangle()
        self.assertTrue(r1.is_inside(0.5, 1.5))
        self.assertTrue(r1.is_inside(1.8, 2.1))

        # assert false if point is outside
        """Test that points are not inside rectangle"""
        self.assertFalse(r1.is_inside(1, 4))

    def test_rectangle_translate(self):
        """Test if rectangle can translate/move by some given x,y points"""
        r1 = self.create_rectangle()
        r1.translate(1, 1)
        r3 = Rectangle(2, 3, 1, 2)
        self.assertTrue(r1.midPoint, r3.midPoint)

    # test rectangle against other shapes
    def test_rectangle_with_circle(self):
        """Test rectangle against circle"""
        cir = self.create_circle()
        rect = self.create_rectangle()
        self.assertNotEqual(rect, cir)

    def test_rectangle_with_cuboid(self):
        """Test rectangle against cuboid"""
        rect = self.create_rectangle()
        cube = self.create_cuboid()
        self.assertNotEqual(rect, cube)

    def test_rectangle_with_sphere(self):
        """Test rectangle against sphere"""
        rect = self.create_rectangle()
        sphere = self.create_sphere()
        self.assertNotEqual(rect, sphere)

    # test cuboid
    def test_cuboid_circumference(self):
        """Test circumference of a cuboid"""
        c1 = self.create_cuboid()
        circumference = 4 * (self.side1 + self.side2 + self.side3)
        self.assertEqual(c1.circumference, circumference)

    def test_cuboid_volume(self):
        """Test volume of a cuboid"""
        c1 = self.create_cuboid()
        volume = self.side1 * self.side2 * self.side3
        self.assertEqual(c1.volume, volume)

    def test_cuboid_translate(self):
        """Test if cuboid can translate/move by some given x,y points"""
        c1 = self.create_cuboid()
        c1.translate(1, 1)
        c3 = Cuboid(2, 3, 1, 2, 3)
        self.assertTrue(c1.midPoint, c3.midPoint)

    def test_equal_cuboid(self):
        """Test if two cuboids are equal"""
        c1 = self.create_cuboid()
        c2 = Cuboid(2, 2, 1, 2, 2)
        self.assertEqual(c1, c2)

    def test_not_equal_cuboid(self):
        """Test that two cuboids are not equal"""
        c1 = self.create_cuboid()
        c2 = Cuboid(2, 3, 2, 1, 5)
        self.assertNotEqual(c1, c2)

    def test_less_than_or_equal_cuboid(self):
        """Test that cuboid is less than or equal to another cuboid"""
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 4, 1)
        self.assertLessEqual(c1, c2)

    def test_less_than_cuboid(self):
        """Test that cuboid is less than another cuboid"""
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 4, 2)
        self.assertLess(c1, c2)

    def test_greater_than_cuboid(self):
        """Test that cuboid is greater than another cuboid"""
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 1.5, 1)
        self.assertGreater(c1, c2)

    def test_greater_or_equal_than_cuboid(self):
        """Test that cuboid is greater than or equal to another cuboid"""
        c1 = self.create_cuboid()
        c2 = Cuboid(1, 2, 1, 1.9, 1)
        self.assertGreater(c1, c2)

    # test cuboid against other shapes
    def test_cuboid_with_rectangle(self):
        """Test cuboid against a rectangle"""
        cube = self.create_cuboid()
        rect = self.create_rectangle()
        self.assertNotEqual(cube, rect)

    def test_cuboid_with_circle(self):
        """Test cuboid against circle"""
        cir = self.create_circle()
        cube = self.create_cuboid()
        self.assertNotEqual(cube, cir)

    def test_cuboid_with_sphere(self):
        """Test cuboid with sphere"""
        cube = self.create_cuboid()
        sphere = self.create_sphere()
        self.assertNotEqual(cube, sphere)

    # Test sphere
    def test_equal_sphere(self):
        """Test if two spheres are equal"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 1)
        self.assertEqual(s1, s2)

    def test_not_equal_sphere(self):
        """Test if two spheres are not equal"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertNotEqual(s1, s2)

    def test_sphere_translate(self):
        """Test if sphere can translate/move by given points"""
        s1 = self.create_sphere()
        s1.translate(1, 1)
        s2 = Sphere(2, 3, 1)
        self.assertEqual(s1.midPoint, s2.midPoint)

    def test_less_than_or_equal_sphere(self):
        """Test if sphere is less than or equal to another sphere"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertLessEqual(s1, s2)

    def test_less_than_sphere(self):
        """Test if sphere is less than another sphere"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 2)
        self.assertLess(s1, s2)

    def test_greater_than_sphere(self):
        """Test if sphere is greater than another sphere"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 0.2)
        self.assertGreater(s1, s2)

    def test_greater_or_equal_than_sphere(self):
        """Test if sphere is greater than or equal to another sphere"""
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 0.2)
        self.assertGreater(s1, s2)

    # test sphere volume
    def test_sphere_volume(self):
        """Test if volume is rightly computed"""
        s1 = self.create_sphere()
        volume = (4 / 3) * math.pi * self.radius**3
        self.assertEqual(s1.volume, volume)


if __name__ == "__main__":
    unittest.main()
