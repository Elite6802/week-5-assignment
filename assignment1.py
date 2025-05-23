# Base class
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand         # Encapsulated attribute
        self._model = model         # Encapsulated attribute

    def get_info(self):
        return f"{self._brand} {self._model}"

    def move(self):
        print("The vehicle is moving.")  # Generic move method (will be overridden)

# Subclass 1
class Car(Vehicle):
    def move(self):
        print(f"{self.get_info()} is Driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print(f"{self.get_info()} is Flying ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print(f"{self.get_info()} is Sailing 🚤")
