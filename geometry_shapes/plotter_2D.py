from circle import Circle
from rectangle import Rectangle
from matplotlib import pyplot as plt


rect1 = Rectangle(0.5,0.2,0.5,0.3)
cir = Circle(0.5,0.5,100)
ax = plt.axes()

for func in (rect1, cir):
    func.plot(ax)
ax.autoscale()
ax.set_aspect(1)
plt.show()






