from __future__ import annotations
from math import pi
from shape import Shape
from matplotlib import pyplot as plt, patches


class Circle(Shape):
    """class representing a round plane figure whose boundary (the circumference) consists of points equidistant from a fixed point (the centre)."""

    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        self.radius = radius
        super().__init__(x, y)

    @property
    def radius(self) -> int | float:
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"radius must be an int or float and not {type(value).__name__}"
            )
        self._radius = value

    @property
    def area(self):
        return pi * self.radius**2

    @property
    def circumference(self):
        return 2 * pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def translate_circle(self, a,b):
        value = [a,b]
        for i in range(len(value)):
            if not isinstance(value[i], (float, int)):
                raise TypeError(
                    f"translate numbers have to be ints or float and not {type(value[i]).__name__}"
                )

        circle_coord = (self.x, self.y)
        translated = tuple(a + b for a, b in zip(circle_coord, value))
        circle = Circle(translated[0], translated[1], self.radius)
        return circle

    def plot(self, ax):

        circle1 = patches.Circle((self.x, self.y), self.radius, color="red", fill=False)
        ax.add_patch(circle1)
        



    def __repr__(self) -> str:
        return f"Circle(Area={self.area}, circumference={self.circumference})"

    def __str__(self) -> str:
        if self.translate_circle:
            return f"{self.__class__.__name__} = ({self.x}, {self.y}, {self.radius})"
        return f"Circle with area: {self.area}, circumference: {self.circumference}"


