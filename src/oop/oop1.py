# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    print("Vehicle")
    pass


class GroundVehicle(Vehicle):
    print("GroundVehicle child of Vehicle")
    pass


class Car(GroundVehicle):
    print("Car child of GroundVehicle")
    pass


class Motorcycle(GroundVehicle):
    print("Motorcycle child of GroundVehicle")
    pass


class FlightVehicle(Vehicle):
    print("FlightVehicle child of Vehicle")
    pass


class Airplane(FlightVehicle):
    print("Airplane child of FlightVehicle")
    pass


class Starship(FlightVehicle):
    print("Starship child of FlightVehicle")
    pass
