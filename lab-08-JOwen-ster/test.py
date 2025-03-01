import unittest
from main import Vehicle, Motorcycle

class TestVehicleProgram(unittest.TestCase):
    def test_vehicle_count(self):
        vehicle1 = Vehicle("Toyota", "Camry", 2022)
        vehicle2 = Vehicle("Ford", "F-150", 2022)
        self.assertEqual(Vehicle.vehicle_count, 8)

    def test_motorcycle_vin(self):
        motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 471)
        motorcycle1.set_vin("ABC123")
        self.assertEqual(motorcycle1.get_vin(), "ABC123")

if __name__ == "__main__":
    unittest.main()
