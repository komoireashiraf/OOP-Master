# 1. Planets
class Planet:
    def _init_(self, name, diameter, moons, atmosphere):
        self.name = name
        self.diameter = diameter
        self.moons = moons
        self.atmosphere = atmosphere


planet1 = Planet("Mercury", "4,879 km", 0, "Thin gases")
planet2 = Planet("Venus", "12,104 km", 0, "Carbon dioxide")
planet3 = Planet("Earth", "12,742 km", 1, "Nitrogen and Oxygen")
planet4 = Planet("Jupiter", "139,820 km", 79, "Hydrogen and Helium")
planet5 = Planet("Neptune", "49,244 km", 14, "Methane")
