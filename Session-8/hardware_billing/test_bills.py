# ==========================================
# Task 3: Test Unique Bill Numbers
# ==========================================

from hardware_shop.bill_numbers import new_bill_number


# Generate 20 Bill Numbers
bill_numbers = []

for i in range(20):

    bill = new_bill_number()

    bill_numbers.append(bill)

    print(bill)


# Check Duplicate Numbers
if len(bill_numbers) == len(set(bill_numbers)):
    print("Duplicates: 0")
else:
    print("Duplicates found!")