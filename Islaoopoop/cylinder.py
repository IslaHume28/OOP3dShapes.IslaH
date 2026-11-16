
from shape3d import Shape3D
import pyvista as pv
import math


class Cylinder(Shape3D):

    def __init__(self, colour, radius, height):
        super().__init__("Cylinder", colour)
        self.__radius = radius
        self.__height = height

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def volume(self):
        return math.pi * (self.__radius**2) * self.__height

    def surface_area(self):
        return 2 * math.pi * self.__radius * (self.__radius + self.__height)

    def draw(self):
        plotter = pv.Plotter()
        cylinder = pv.Cylinder(
            radius=self.__radius,
            height=self.__height
        )
        plotter.add_mesh(cylinder, color=self.get_colour(), show_edges=True)
        plotter.add_axes()
        plotter.show_grid()
        plotter.show()


if __name__ == "__main__":
    cylinder1 = Cylinder("Green", 1, 2)
    cylinder1.draw()

