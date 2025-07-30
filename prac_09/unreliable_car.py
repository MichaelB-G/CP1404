"""
CP1404 Practical 09 - UnreliableCar class
A specialised version of Car that sometimes does not drive.
"""

import random
from car import Car

class UnreliableCar(Car):
    """Represent an UnreliableCar that may not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with added reliability attribute."""
        super().__init__(name, fuel)
        self.reliability = reliability  # percentage chance to drive

    def drive(self, distance):
        """Attempt to drive the car. Drive only if random chance is within reliability."""
        if random.uniform(0, 100) < self.reliability:
            # Car drives successfully
            return super().drive(distance)
        else:
            # Car fails to drive
            print(f"{self.name} failed to start!")
            return 0
