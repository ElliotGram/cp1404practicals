"""
CP1404/CP5632 Practical
silver service taxi
"""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi for Silver Service."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the Silver Service taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a formatted string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
