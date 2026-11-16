
from shape3d import Shape3D
import pyvista as pv
import math

# my sphere, ma sphere, here yaaaa go
class Sphere(Shape3D):

    def __init__(self, colour, radius):
        super().__init__("Sphere", colour)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def volume(self):
        return (4/3) * math.pi * (self.__radius**3)

    def surface_area(self):
        return 4 * math.pi * (self.__radius**2)

    def draw(self):
        plotter = pv.Plotter()
        sphere = pv.Sphere(radius=self.__radius)
        plotter.add_mesh(sphere, color=self.get_colour(), show_edges=True)
        plotter.add_axes()
        plotter.show_grid()
        plotter.show()


if __name__ == "__main__":
    sphere1 = Sphere("Pink", 5)

    print("Shape:", sphere1.get_type())
    print("Colour:", sphere1.get_colour())
    print("Volume:", round(sphere1.volume(), 2))
    print("Surface Area:", round(sphere1.surface_area(), 2))

    sphere1.draw()
