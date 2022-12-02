from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(75.50, 615.10)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init(self):
        self.assertEqual(75.50, self.car.fuel)
        self.assertEqual(615.10, self.car.horse_power)
        self.assertEqual(75.50, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_kilometers(self):
        self.car.drive(10)
        self.assertEqual(63.0, self.car.fuel)

    def test_drive_to_raise_exception(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_correct_fuel(self):
        self.car.fuel = 15
        self.car.refuel(10)
        self.assertEqual(25,self.car.fuel)

    def test_refuel_with_more_than_capacity_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(200)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_representation(self):
        result = self.car.__str__()
        expected = "The vehicle has 615.1 " \
               "horse power with 75.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(result,expected)


if __name__ == "__main__":
    main()
