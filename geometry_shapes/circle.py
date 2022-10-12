from __future__ import annotations
from math import pi
from shape import Shape
from matplotlib import pyplot as plt, patches


class Circle(Shape):
    """A child class from shape representing a round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the centre).

    ```
    Attributes
    -----------
    radius: float or int representing the radius of the circle
    """

    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        """
        Parameters
        ----------
        radius: represents the distance from the center of the Circle to the circumference or the bounding surface of the Circle
        """
        self.radius = radius

        """The Circle inherits the points x and y from the parent class Shape"""
        super().__init__(x, y)

    @property
    def radius(self) -> int | float:
        """A getter to retrieve the radius attribute of the Circle"""
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        """A setter to set the radius of the Circle"""
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"radius must be an int or float and not {type(value).__name__}"
            )
        self._radius = value

    @property
    def area(self):
        """A getter to retrieve the area of the Circle. It is a property without a getter so that its value cant be change"""
        return pi * self.radius**2

    @property
    def circumference(self):
        """A getter to retrieve the circumference of the Circle. It is a property without a getter so that its value cant be change"""
        return 2 * pi * self.radius

    def is_unit_circle(self) -> bool:
        """A function that checks if a Circle is a unit Circle i.e if the Circle has a radius of 1"""
        return self.radius == 1

    def is_inside(self, a, b) -> bool:
        """A function that checks if my circle is inside another"""
        check = (a - self.x) ** 2 + (b - self.y) ** 2 < self.radius**2
        return check

    def plot(self, ax):
        """A plot function to plot an intance of a Circle created"""
        circle1 = patches.Circle((self.x, self.y), self.radius, color="red", fill=False)
        ax.add_patch(circle1)

    def __repr__(self) -> str:
        """__repr__ overrides the parent Shape classe's __repr__ to return the object representation in a string of a Circle"""
        return f"Circle(Area={self.area}, circumference={self.circumference})"

    def __str__(self) -> str:
        """__str__ overrides the parent's __str__ to return a string representation of Circle"""
        if self.translate:
            return f"Translated {self.__class__.__name__} = ({self.x}, {self.y}, {self.radius})"
        return f"Circle with area: {self.area}, circumference: {self.circumference}"
