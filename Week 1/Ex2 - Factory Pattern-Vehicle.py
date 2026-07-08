from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass


# Car class
class Car(Vehicle):

    def drive(self):
        print("Driving a Car")


# Bike class
class Bike(Vehicle):

    def drive(self):
        print("Driving a Bike")


# Truck class
class Truck(Vehicle):

    def drive(self):
        print("Driving a Truck")


# Factory class
class VehicleFactory:

    def create_vehicle(self, vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()

        elif vehicle_type == "truck":
            return Truck()

        else:
            return None


# Main program
factory = VehicleFactory()

vehicle1 = factory.create_vehicle("car")
vehicle1.drive()

vehicle2 = factory.create_vehicle("bike")
vehicle2.drive()

vehicle3 = factory.create_vehicle("truck")
vehicle3.drive()

"""
Output:
Driving a Car
Driving a Bike
Driving a Truck
"""
