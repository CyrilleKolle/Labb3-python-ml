from __future__ import annotations
from rectangle import Rectangle

class Cube(Rectangle):
    def __init__(self, x: float | int, y: float | int, side1: float | int, side2: float | int) -> None:
        super().__init__(x, y, side1, side2)

    def validate_cube(self):
        if self.side1 != self.side2:
            raise ValueError(f"A cube has all its sides equal to each other")

    @property
    def cube_area(self) -> int | float:
        if self.validate_cube:
            return 6 * self.side1**2

    @property 
    def cube_perimeter(self) -> int | float:
        if self.validate_cube:
            return 12 * self.side1

    def __lt__(self, other: Cube) -> bool:
        return self.perimeter < other.perimeter


    def __repr__(self) -> str:
        return super().__repr__()
    
    def __str__(self) -> str:
        return super().__str__()

cube = Cube(1,1, 2,2)
print(cube.cube_area)
print(cube.perimeter)