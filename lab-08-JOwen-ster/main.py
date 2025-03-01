'''
WRITE YOUR CODE HERE
'''
class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1

    def display_vehicle_count(self):
        print(f"Total vehicles: {Vehicle.vehicle_count}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type : str):
        super().__init__(make, model, year)
        self.fuel_type : str = fuel_type
        

class Motorcycle(Vehicle):
    __vin = None
    _color = None

    def __init__(self, make, model, year, engine_capacity : int):
        super().__init__(make, model, year)
        self.engine_capacity : int = engine_capacity
    
    def set_color(self, color):
        self._color = color
    
    def get_vin(self):
        return self.__vin
    
    def set_vin(self, vin):
        self.__vin = vin

def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

def fibonacci(limit):
    num1 = 0
    num2 = 1
    while num1 <= limit:
        yield num1
        num1, num2 = num2, num1 + num2


'''
DRIVER CODE
'''
# Create instances of Vehicle, Car, and Motorcycle
vehicle1 = Vehicle("Toyota", "Camry", 2022)
car1 = Car("Tesla", "Model 3", 2023, "Electric")
motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 471)

# Demonstrate class variables and inheritance
vehicle1.display_vehicle_count()

# Demonstrate private and protected variables
motorcycle1.__vin = "ABC123"  # Attempt to set private variable (won't work)
motorcycle1.set_color("Red")  # Set protected variable
print(f"Motorcycle color: {motorcycle1._color}")
print(f"Motorcycle VIN: {motorcycle1.get_vin()}")  # Access private variable

# Demonstrate generator functions
print("Counting up to 5:")
for num in count_up_to(5):
    print(num, end=" ")

print("\nFibonacci sequence up to 50:")
for num in fibonacci(50):
    print(num, end=" ")

# Demonstrate class variables
vehicle2 = Vehicle("Ford", "F-150", 2022)
vehicle3 = Vehicle("Honda", "Civic", 2022)
vehicle2.display_vehicle_count()
