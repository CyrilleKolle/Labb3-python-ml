from __future__ import annotations
from circle import Circle
import math


class Sphere(Circle):
    """A child class from Circle representing a 3D round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the centre).

    ```
    Attributes
    -----------
    radius: float or int representing the radius of the circle
    """

    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        """
        __init__ function is called everytime an instance of the class is created. It  lets the class initialize the object's attributes and serves no other purpose

        Parameters
        -----------
        The Sphere inherits the points x,y and radius from its parent class Circle with the super() function
        """
        super().__init__(x, y, radius)

    @property
    def area(self):
        """A getter to retrieve the area of the Sphere. It is a property without a getter function so that its value cant be change"""
        return 4 * math.pi * self.radius**2

    @property
    def volume(self):
        """A getter to retrieve the volume of the Sphere. It is a property without a getter so that its value cant be change"""
        return (4 / 3) * math.pi * self.radius**3

    def __repr__(self) -> str:
        """__repr__ overrides the parent Circle classe's __repr__ to return the object representation in a string of a Sphere"""

        return f"Sphere(Area = {self.area}, circumference = {self.circumference})"

    def __str__(self) -> str:
        """__str__ overrides the parent's __str__ to return a string representation of a Sphere"""
        if self.translate:
            return f"Sphere with x = {self.x}, y = {self.y}, radius = {self.radius}, volume = {self.volume}, area ={self.area} and circumfere = {self.circumference})"
        return f"Sphere with area: {self.area}, circumference: {self.circumference}"
