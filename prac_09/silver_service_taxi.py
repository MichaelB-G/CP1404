"""
CP1404 Practical 09 - SilverServiceTaxi class
A specialised Taxi with fanciness and flagfall.
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes fanciness and flagfall."""
    flagfall = 4.50  # class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi with fanciness multiplier."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness  # scale price/km for this taxi

    def get_fare(self):
        """Return fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string with added flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
