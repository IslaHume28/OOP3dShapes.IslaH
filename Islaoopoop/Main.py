
from sphere import Sphere
from cylinder import Cylinder

# Ma sphere
sphere1 = Sphere("Pink", 5)

# ma cylinder
cylinder1 = Cylinder("Green", 1, 2)

#List for shapes yuhyuh
shapes = [sphere1, cylinder1]

for shape in shapes:

    print("\n========================")
    print("Shape:", shape.get_type())
    print("Colour:", shape.get_colour())

    print("Volume:", round(shape.volume(), 2))
    print("Surface Area:", round(shape.surface_area(), 2))

    print("\nDrawing:")
    shape.draw()

print("\nAll shapes tested YURRRRRR")
