"""
CP1404/CP5632 Practical
unreliable car test
"""
from prac_09.unreliable_car import UnreliableCar

# Create a new UnreliableCar object, my_car, with name "Unreliable", 100 units of fuel, and reliability of 50%
my_car = UnreliableCar("Unreliable", 100, 50)

# Drive the car 40 km (it may or may not drive, depending on reliability)
distance_driven = my_car.drive(40)

# Print the car's details and the distance driven
print(f"{my_car} - Distance driven: {distance_driven} km")
