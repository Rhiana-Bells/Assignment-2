class Vehicle:
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels

    def start(self):
        """Base implementation — describes starting a generic vehicle."""
        return f"The {self.make} {self.model} is starting its engine."

    def describe(self):
        """Base implementation — prints basic vehicle info."""
        return f"{self.make} {self.model} with {self.wheels} wheels"


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model, wheels=4)
        self.doors = doors

    def start(self):
        """Override — cars start by turning a key/pressing a button."""
        return f"The {self.make} {self.model} engine roars to life. All {self.doors} doors are locked."


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, wheels=2)

    def start(self):
        """Override — bikes don't have an engine, so starting is different."""
        return f"The {self.make} {self.model} bicycle is ready — just pedal!"


# example
vehicles = [
    Vehicle("Generic", "Utility Van", 4),
    Car("Toyota", "Auris", 4),
    Bike("Giant", "Escape 3"),
]

for v in vehicles:
    print(v.describe())
    print(v.start())
    print("-" * 40)