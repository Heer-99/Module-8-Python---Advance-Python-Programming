
# ==========================================
# Task 1: Fest Passes
# ==========================================

# Create Parent Class
class FestPass:

    def __init__(self, holder_name):
        self.holder_name = holder_name

    # Return pass price
    def price(self):
        return 500

    # Return pass perks
    def perks(self):
        return "Basic fest entry"

    # Calculate group pass price with discount
    def group_price(self, count=1, discount_percent=0):
        total = self.price() * count
        discount = total * discount_percent / 100
        return total - discount


# Create StudentPass Child Class
class StudentPass(FestPass):

    # Override price method
    def price(self):
        return 300

    # Override perks method
    def perks(self):
        return "Student discount and fest entry"


# Create AlumniPass Child Class
class AlumniPass(FestPass):

    # Override price method
    def price(self):
        return 800

    # Override perks method
    def perks(self):
        return "Alumni entry and refreshment"


# Create VIPPass Child Class
class VIPPass(FestPass):

    # Override price method
    def price(self):
        return 2000

    # Override perks method
    def perks(self):
        return "VIP seating, food and special entry"


# Create Objects
student = StudentPass("Jiya")
alumni = AlumniPass("Priya")
vip = VIPPass("Avinash")


# Display Student Pass Details
print("===== Student Pass =====")
print("Holder Name:", student.holder_name)
print("Price: ₹", student.price())
print("Perks:", student.perks())


# Display Alumni Pass Details
print("\n===== Alumni Pass =====")
print("Holder Name:", alumni.holder_name)
print("Price: ₹", alumni.price())
print("Perks:", alumni.perks())


# Display VIP Pass Details
print("\n===== VIP Pass =====")
print("Holder Name:", vip.holder_name)
print("Price: ₹", vip.price())
print("Perks:", vip.perks())


# ==========================================
# Task 2: Pass Receipts and Total
# ==========================================

# Print Pass Receipt
def print_receipt(pass_obj):

    print("\nHolder Name:", pass_obj.holder_name)
    print("Price: ₹", pass_obj.price())
    print("Perks:", pass_obj.perks())


# Create List of 8 Passes
passes = [

    StudentPass("Rahul"),
    StudentPass("Neha"),
    StudentPass("Krish"),

    AlumniPass("Riya"),
    AlumniPass("Mehul"),

    VIPPass("Aarav"),

    FestPass("Diya"),
    FestPass("Karan")

]


# Print All Receipts
print("\n===== All Pass Receipts =====")

total = 0

for pass_obj in passes:

    print_receipt(pass_obj)

    total += pass_obj.price()


# Display Total Amount
print("\nTotal Pass Amount: ₹", total)


# ==========================================
# Task 3: Group Pass Price
# ==========================================

# Create StudentPass Object
student_group = StudentPass("Jiya")


# Test Student Group Price
print("\n===== Student Group Price =====")
print("Single Pass Price: ₹", student_group.group_price())
print("4 Passes Price: ₹", student_group.group_price(4))
print("4 Passes with 10% Discount: ₹", student_group.group_price(4, 10))


# Create AlumniPass Object
alumni_group = AlumniPass("Priya")


# Test Alumni Group Price
print("\n===== Alumni Group Price =====")
print("2 Passes with 25% Discount: ₹", alumni_group.group_price(2, 25))




# ==========================================
# Task 4: Registration Menu
# ==========================================

# Dictionary to select pass class
pass_types = {
    "G": FestPass,
    "S": StudentPass,
    "A": AlumniPass,
    "V": VIPPass
}

# Dictionary to store per-type totals
type_totals = {
    "G": 0,
    "S": 0,
    "A": 0,
    "V": 0
}

# List to store registrations
registrations = []

# Get number of registrations
total_registrations = int(input("\nEnter number of registrations: "))


# Registration Menu
for i in range(total_registrations):

    print("\n===== Registration", i + 1, "=====")

    holder_name = input("Enter holder name: ")

    pass_type = input("Enter pass type (G/S/A/V): ").upper()

    while pass_type not in pass_types:
        print("Invalid pass type! Please enter G, S, A or V.")
        pass_type = input("Enter pass type (G/S/A/V): ").upper()

    count = int(input("Enter number of passes: "))
    discount_percent = float(input("Enter discount percent: "))

    # Create object using dictionary
    pass_class = pass_types[pass_type]
    pass_obj = pass_class(holder_name)

    # Calculate total price
    amount = pass_obj.group_price(count, discount_percent)

    # Store registration details
    registrations.append((pass_obj, count, discount_percent, amount, pass_type))

    # Update per-type total
    type_totals[pass_type] += amount


# Display Registration Details
print("\n===== Registration Details =====")

for pass_obj, count, discount_percent, amount, pass_type in registrations:

    print("\nHolder Name:", pass_obj.holder_name)
    print("Pass Type:", pass_type)
    print("Number of Passes:", count)
    print("Discount:", discount_percent, "%")
    print("Total Amount: ₹", amount)


# Display Per-Type Total
print("\n===== Per-Type Total =====")
print("General Pass Total: ₹", type_totals["G"])
print("Student Pass Total: ₹", type_totals["S"])
print("Alumni Pass Total: ₹", type_totals["A"])
print("VIP Pass Total: ₹", type_totals["V"])


# Calculate Grand Total
grand_total = sum(type_totals.values())

print("\nGrand Total: ₹", grand_total)
