"""
CP1404/CP5632 Practical
silver service taxi
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a new SilverServiceTaxi object, my_taxi, with name "Hummer", 200 units of fuel, and fanciness of 4
my_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive the taxi 18 km
my_taxi.drive(18)

# Print the taxi's details and the current fare
print(my_taxi)