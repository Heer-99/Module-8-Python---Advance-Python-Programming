# ==========================================
# Task 3: Generate Unique Bill Numbers
# ==========================================

import random


# Store Generated Bill Numbers
generated_numbers = []


# Function to Generate New Bill Number
def new_bill_number():

    while True:

        number = random.randint(1000, 9999)

        if number not in generated_numbers:

            generated_numbers.append(number)

            return "HW-" + str(number)