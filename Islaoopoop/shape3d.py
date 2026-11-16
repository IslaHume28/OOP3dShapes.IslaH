
class Shape3D:

    def __init__(self, type, colour):
        self.__type = type
        self.__colour = colour

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def volume(self):
        return None

    def surface_area(self):
        return None
