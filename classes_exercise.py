# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""


class Vehicle:
    """Represents a vehicle

    Attributes:
        name: name of the vehicle
        max_speed: maximum speed in km/h
        capacity: how many people it can hold
    """

    def __init__(self):
        self.name = ""
        self.max_speed = 0
        self.capacity = 0

    def vroom(self) -> None:
        """Vehicle goes vroom speed times"""
        print("Vroom" * self.max_speed)


a_vehicle = Vehicle()
a_vehicle.name = "Super Fast Ferrari"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_vehicle.vroom()

