from __future__ import annotations
from rectangle import Rectangle

class Cube(Rectangle):
    def __init__(self, x: float | int, y: float | int, side1: float | int, side2: float | int) -> None:
        super().__init__(x, y, side1, side2)

    def validate_cube(self):
        if self.side1 != self.side2:
            raise ValueError(f"A cube has all its sides equal to each other")

    def validate_other(self, other: Cube):
        if self.side1 != self.side2 and self.area != other.area and self.perimeter:
            raise ValueError(f"A cube has all its sides equal to each other")

    @property
    def area(self) -> int | float:
        if self.validate_cube:
            return 6 * self.side1**2

    @property 
    def perimeter(self) -> int | float:
        if self.validate_cube:
            return 12 * self.side1

    def __lt__(self, other: Cube) -> bool:
        if other.validate_cube():
            return self.perimeter < other.perimeter
    
    def __eq__(self, other: Cube) -> bool:
        if other.validate_cube:
            return other.perimeter == self.perimeter
    def __gt__(self, other: Cube) -> bool:
            if other.validate_cube():
                return self.perimeter > other.perimeter

    def __le__(self, other: Cube) -> bool:
        if other.validate_cube():
            return self.perimeter <= other.perimeter

    def __ge__(self, other: Cube) -> bool:
        if other.validate_cube():
            return self.perimeter >= other.perimeter

    def __repr__(self) -> str:
        return f"Cube(Area='{self.are}', Perimeter='{self.perimeter}')"
    
    def __str__(self) -> str:
        return f"Cube with an area of {self.area} and a perimeter of {self.perimeter}"

cube = Cube(1,2, 3,2)
cube1 = Cube(1,1,3,3)
print(cube.area)
print(cube1.perimeter)
print(cube == cube1)