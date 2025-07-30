"""
CP1404 Practical 09 - Taxi class
Specialised version of Car that includes fare costs.
"""

from car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable shared by all taxis

    def __init__(self, name, fuel):
        """Initialise a Taxi with fuel and fare attributes."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return string like Car but with current fare distance and price."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip, rounded to nearest 10c."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Reset the fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but track fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
