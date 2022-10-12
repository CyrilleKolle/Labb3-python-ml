from circle import Circle
from rectangle import Rectangle
from matplotlib import pyplot as plt


rect1 = Rectangle(2, 2, 3, 5)
cir = Circle(0.5, 0.5, 10)
cir.translate(2, 2)
ax = plt.axes()
for func in (rect1, cir):
    func.plot(ax)
ax.autoscale()
ax.set_aspect(1)
ax.spines["top"].set_color("none")
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")

plt.show()
