from __future__ import annotations
from circle import Circle
import math

class Sphere(Circle):
    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        super().__init__(x, y, radius)

    @property
    def sphere_volume(self):
        return (4/3) * math.pi * self.radius**3

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()
sph1 = Sphere(2,2, 1)
print(sph1.sphere_volume)