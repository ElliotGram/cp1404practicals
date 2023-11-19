"""
CP1404/CP5632 Practical
unreliable car
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car with reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but with a reliability check."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven