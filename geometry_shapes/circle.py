from __future__ import annotations
from math import pi
from typing import Type
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
    def circle_area(self):
        return pi * self.radius**2

    @property
    def circle_circumference(self):
        return 2 * pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def __eq__(self, other: Circle) -> bool:
        return self.circle_circumference == other.circle_circumference

    def __lt__(self, other: Circle) -> bool:
        return self.circle_circumference < other.circle_circumference

    def __gt__(self, other: Circle) -> bool:
        return self.circle_circumference > other.circle_circumference

    def __le__(self, other: Circle) -> bool:
        return self.circle_circumference <= other.circle_circumference

    def __ge__(self, other: Circle) -> bool:
        return self.circle_circumference >= other.circle_circumference

    def translate_circle(self, value: tuple):
        for i in range(len(value)):
            if not isinstance(value[i], (float, int)):
                raise TypeError(
                    f"translate numbers have to be ints or float and not {type(value[i]).__name__}"
                )

        circle_coord = (self.x, self.y)
        translated = tuple(a + b for a, b in zip(circle_coord, value))
        circle = Circle(translated[0], translated[1], self.radius)
        return circle

    def plot_circle(self):
        if self.is_shape_circle():
            plt.rcParams["figure.figsize"] = [7.00, 3.50]
            plt.rcParams["figure.autolayout"] = True
            fig = plt.figure()
            ax = fig.add_subplot()
            circle1 = patches.Circle(
                (self.x, self.y), radius=0.5, color="green", fill=False
            )
            ax.add_patch(circle1)
            ax.axis("equal")

        return plt.show()

    def __repr__(self) -> str:
        return f""

    def __str__(self) -> str:
        return f"hey"


circle1 = Circle(x=1, y=2, radius=2)
circle2 = Circle(4, 2, 2)
co = (2, 2)

# try:
#     # circle3 = circle1.translate_circle(co)
#     # print(f"circle 3 ={circle3}")
#     #circle1.plot_circle()
#     c3 = circle1.translate_circle(co)

# except ValueError as err:
#     print(err)

print(Circle.__name__)

print(Circle.__class__)

# print(circle2.is_unit_circle())
