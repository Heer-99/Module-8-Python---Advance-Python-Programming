
# ==========================================
# Task 1: Parking System
# ==========================================

# Create Parent Class
class Vehicle:

    def __init__(self, reg_no, owner, hours, rate):
        self.reg_no = reg_no
        self.owner = owner
        self.hours = hours
        self.rate = rate

    # Calculate parking charge
    def parking_charge(self):
        return self.hours * self.rate


# Create TwoWheeler Child Class
class TwoWheeler(Vehicle):

    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 10)


# Create FourWheeler Child Class
class FourWheeler(Vehicle):

    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 30)


# Create FourWheeler Object
car = FourWheeler("GJ01AB1234", "Akshat", 3)

# Create TwoWheeler Object
bike = TwoWheeler("GJ01CD5678", "Nidhi", 5)


# Display FourWheeler Details
print("===== Four Wheeler Parking =====")
print("Registration No:", car.reg_no)
print("Owner:", car.owner)
print("Parking Hours:", car.hours)
print("Rate Per Hour: ₹", car.rate)
print("Parking Charge: ₹", car.parking_charge())


# Display TwoWheeler Details
print("\n===== Two Wheeler Parking =====")
print("Registration No:", bike.reg_no)
print("Owner:", bike.owner)
print("Parking Hours:", bike.hours)
print("Rate Per Hour: ₹", bike.rate)
print("Parking Charge: ₹", bike.parking_charge())


# ==========================================
# Task 2: Electric Car
# ==========================================

# Create ElectricCar Child Class
class ElectricCar(FourWheeler):

    def __init__(self, reg_no, owner, hours, battery_kwh):
        super().__init__(reg_no, owner, hours)
        self.battery_kwh = battery_kwh

    # Calculate charging cost
    def charging_cost(self, units):
        return units * 12


# Create ElectricCar Object
electric_car = ElectricCar("GJ01EF9012", "Aarav", 2, 60)


# Display ElectricCar Details
print("\n===== Electric Car Details =====")
print("Registration No:", electric_car.reg_no)
print("Owner:", electric_car.owner)
print("Parking Hours:", electric_car.hours)
print("Battery Capacity:", electric_car.battery_kwh, "kWh")
print("Parking Charge: ₹", electric_car.parking_charge())
print("Charging Cost: ₹", electric_car.charging_cost(10))


# ==========================================
# Task 3: Multiple Inheritance - Valet Service
# ==========================================

# Create ValetService Class
class ValetService:

    # Return valet fee
    def valet_fee(self):
        return 50


# Create ValetElectricCar Class
class ValetElectricCar(ElectricCar, ValetService):

    def __init__(self, reg_no, owner, hours, battery_kwh):
        ElectricCar.__init__(self, reg_no, owner, hours, battery_kwh)

    # Calculate total bill
    def bill(self, units):
        return self.parking_charge() + self.charging_cost(units) + self.valet_fee()


# Create ValetElectricCar Object
valet_car = ValetElectricCar("GJ01GH3456", "Kartik", 2, 60)


# Display Valet Electric Car Details
print("\n===== Valet Electric Car Details =====")
print("Registration No:", valet_car.reg_no)
print("Owner:", valet_car.owner)
print("Parking Hours:", valet_car.hours)
print("Battery Capacity:", valet_car.battery_kwh, "kWh")
print("Parking Charge: ₹", valet_car.parking_charge())
print("Charging Cost: ₹", valet_car.charging_cost(10))
print("Valet Fee: ₹", valet_car.valet_fee())
print("Total Bill: ₹", valet_car.bill(10))


# ==========================================
# Task 4: Day-End Parking Report
# ==========================================

# Create List of 8 Vehicles
vehicles = [
    car,
    bike,
    electric_car,
    valet_car,
    Vehicle("GJ01XY1111", "Jay", 2, 20),
    TwoWheeler("GJ01XY2222", "Jiya", 4),
    FourWheeler("GJ01XY3333", "Mishka", 1),
    ValetElectricCar("GJ01XY4444", "Khushi", 3, 70)
]


# Display Day-End Report
print("\n===== Day-End Parking Report =====")

total_revenue = 0

for vehicle in vehicles:

    print("\nClass Name:", type(vehicle).__name__)
    print("Registration No:", vehicle.reg_no)
    print("Parking Charge: ₹", vehicle.parking_charge())

    total_revenue += vehicle.parking_charge()


# Display Total Parking Revenue
print("\nTotal Parking Revenue: ₹", total_revenue)
