from __future__ import annotations
from circle import Circle
import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


class Sphere(Circle):
    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        super().__init__(x, y, radius)

    @property
    def area(self):
        return 4 * math.pi * self.radius**2

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.radius**3

    def __repr__(self) -> str:
        return f"Sphere(Area={self.area}, circumference={self.circumference})"

    def __str__(self) -> str:
        if self.translate:
            return f"{self.__class__.__name__} = ({self.x}, {self.y}, {self.radius})"
        return f"Sphere with area: {self.area}, circumference: {self.circumference}"
