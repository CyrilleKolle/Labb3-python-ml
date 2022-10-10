from curses.textpad import rectangle
from turtle import circle
from circle import Circle
from rectangle import Rectangle
import matplotlib.pyplot as plt


class Plotter_2D:


    def plotting(self):
        circle1 = Circle(1,2,1)
        rectangle1 = Rectangle(1,1, 2,3)
        fig = plt.figure(2)
        axes = []
        for item in (circle1, rectangle1):
            axes.append(item.plot())
        fig.axes.append(axes)

        plt.show()



plotter1 = Plotter_2D()
plotter1.plotting()