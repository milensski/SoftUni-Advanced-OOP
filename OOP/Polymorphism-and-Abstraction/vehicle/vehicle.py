from abc import ABC,abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITION_INCREASE = 0.9

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.AIR_CONDITION_INCREASE) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.AIR_CONDITION_INCREASE)
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity




class Truck(Vehicle):
    AIR_CONDITION_INCREASE = 1.6

    def drive(self, distance):
        if distance * (self.fuel_consumption + self.AIR_CONDITION_INCREASE) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AIR_CONDITION_INCREASE)
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel - (fuel * 0.05)
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
